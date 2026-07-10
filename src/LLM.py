
from abc import ABC, abstractmethod

from transformers import AutoModelForCausalLM, AutoTokenizer
from src.models.DataModels import AnsweredQuestion, MinimalSearchResults

class LLMGenerationError(Exception):
    pass

class BaseLLM(ABC):
    """
    Abstract class for an LLM for RAG
    """
    @abstractmethod
    def generate_answer(
            self,
            query: MinimalSearchResults) -> AnsweredQuestion:
        """
        Generates the answer to a
        query using the LLM
        """
        pass

class LLM(BaseLLM):
    def __init__(
            self,
            model_name: str = 'Qwen/Qwen3-0.6B') -> None:
        # Load model & tokenizer for inference
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype="auto"
            )
        return None

    def generate_answer(
            self,
            query: MinimalSearchResults) -> AnsweredQuestion:
        """
        Generates the answer to a
        query using the LLM
        """
        # Create a string prompt for the given query
        prompt = self._minimal_search_result_to_prompt(query)

        # Create context for the LLM
        messages = [
            {"role": "system",
             "content": "You are a helpful assistant that gives "
                        "concise but high quality answers from a "
                        "given answer and given sources. The "
                        "output must be non-markdown string.",},
            {"role": "user", "content": prompt}
        ]

        # Tokenize the created context
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False # Switches between thinking and non-thinking modes. Default is True.
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        # Start generating answer
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=32768
        )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

        # Decode content
        answer = self.tokenizer.decode(output_ids, skip_special_tokens=True).strip("\n")

        answered_question = AnsweredQuestion(
            question_id=query.question_id,
            question=query.question,
            sources=query.retrieved_sources,
            answer=answer
        )

        return answered_question

    @staticmethod
    def _minimal_search_result_to_prompt(
        query: MinimalSearchResults
        ) -> str:
        """
        Converts a MinimalSearchResults into a string prompt
        """
        # Format prompt
        prompt = f'[Question]: {query.question}\n\n'

        # Format sources
        sources = ''
        for index, source in enumerate(query.retrieved_sources):
            try:
                # Open file to extract the source
                with open(source.file_path) as f:
                    source_data = f.read()
                    source_data_stripped = source_data[source.first_character_index:source.last_character_index]
                    sources = sources + f'[Source {index}]: ' + source_data_stripped + '\n'
            except BaseException:
                raise LLMGenerationError(f'Could not open/read the file in {source.file_path}.')
        sources = sources + '\n'

        # Concatenate formatted data
        final_prompt = prompt + sources + '[Answer]: '

        return final_prompt