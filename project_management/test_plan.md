# Test plan

Made by gtourdia

---

## Conventions

| Symbol | Meaning |
|---|---|
| ☐ | Not tested |
| ✅ | Tested and validated |
| ⚠️ | Tested but not behaving well enough |
| ❌ | Tested and invalid |

---

## 1. Launch and configuration

### 1.1 Nominal launch

| ID | Scenario | Command | Expected result | Status |
|---|---|---|---|---|
| L01 | | | | ☐ |
| L02 | | | | ☐ |
| L03 | | | | ☐ |
| L04 | | | | ☐ |
| L05 | | | | ☐ |

### 1.2 Configuration robustness

| ID | Scenario | Injected config | Expected result | Status |
|---|---|---|---|---|
| C01 | | | | ☐ |
| C02 | | | | ☐ |
| C03 | | | | ☐ |
| C04 | | | | ☐ |
| C05 | | | | ☐ |
| C06 | | | | ☐ |
| C07 | | | | ☐ |
| C08 | | | | ☐ |
| C09 | | | | ☐ |
| C10 | | | | ☐ |

---

## 2. General rules

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | Project written in python 3.10 or later | Yes | ☐ |
| 02 | Project lint is valid (flake8 + mypy) | Yes | ☐ |
| 03 | Project includes clear docstring on every function / class | Yes | ☐ |
| 04 | | | ☐ |

---

## 3. Makefile

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | `make install` rule install the project dependencies with uv | Yes | ☐ |
| 02 | `make run` rule runs the main script of the project | Yes | ☐ |
| 03 | `make debug` rule starts the debugger on the project's main script | Yes | ☐ |
| 04 | `make clean` rule removes temporary files, including \_\_pycache\_\_ and .mypy_cache  | | ☐ |
| 05 | `make lint` rule validates the flake8 and mypy standards | Yes | ☐ |
| 06 | `make lint-strict` rule validates the flake8 and mypy (strict) standards | Yes | ☐ |
| 07 | | | ☐ |
---

## 4. Performances

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | Indexing time | Less than 5 minutes | ☐ |
| 02 | Cold start latency | Less than 60 secondes | ☐ |
| 03 | Warm retrieval throughput | Less than 90 secondes for 1000 questions | ☐ |
| 04 | Recall@5 score on docs | 80% | ☐ |
| 05 | Recall@5 score on code | 50% | ☐ |
| 06 | | | ☐ |

---

## 5. Readme

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | Readme includes a description of the project | Yes | ☐ |
| 02 | Readme includes instructions to run the program | Yes | ☐ |
| 03 | Readme includes informations about the ressources used to make the project | Yes | ☐ |
| 04 | Readme includes informations about the system architecture (pipeline, etc.) | Yes | ☐ |
| 05 | Readme includes informations about the chunking strategy | Yes | ☐ |
| 06 | Readme includes informations about the retreival method and ranking mechanism | Yes | ☐ |
| 07 | Readme includes a section about performances analysis | Yes | ☐ |
| 08 | Readme includes a section explaining the key implementation choices | Yes | ☐ |
| 09 | Readme includes a section explaining the challenges faced | Yes | ☐ |
| 10 | Readme includes a section explaining example usage of this project | Yes | ☐ |
| 11 | Readme is written in english | Yes | ☐ |
| 00 | | | ☐ |

---

## 6. 

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | | | ☐ |
| 02 | | | ☐ |
| 03 | | | ☐ |
| 04 | | | ☐ |
| 05 | | | ☐ |

---

## 7.

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | | | ☐ |
| 02 | | | ☐ |
| 03 | | | ☐ |
| 04 | | | ☐ |
| 05 | | | ☐ |
| 06 | | | ☐ |
| 07 | | | ☐ |
| 08 | | | ☐ |
| 09 | | | ☐ |
| 10 | | | ☐ |
| 11 | | | ☐ |
| 12 | | | ☐ |
| 13 | | | ☐ |

---

## 8.

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | | | ☐ |
| 02 | | | ☐ |
| 03 | | | ☐ |
| 04 | | | ☐ |
| 05 | | | ☐ |
| 06 | | | ☐ |
| 07 | | | ☐ |

---

## 9.

| ID | Feature | Activation | Expected result | Status |
|---|---|---|---|---|
| 01 | | | | ☐ |
| 02 | | | | ☐ |
| 03 | | | | ☐ |
| 04 | | | | ☐ |
| 05 | | | | ☐ |
| 06 | | | | ☐ |
| 07 | | | | ☐ |

---

## 10.

| ID | Check | Command | Expected result | Status |
|---|---|---|---|---|
| 01 | | | | ☐ |
| 02 | | | | ☐ |
| 03 | | | | ☐ |
| 04 | | | | ☐ |
| 05 | | | | ☐ |
| 06 | | | | ☐ |

---

## 11.

| ID | Scenario | Expected result | Status |
|---|---|---|---|
| 01 | | | ☐ |
| 02 | | | ☐ |
| 03 | | | ☐ |
| 04 | | | ☐ |

---

## Bug tracking

| ID | Date | Description | Severity | Assigned | Status |
|---|---|---|---|---|---|
| | | | | | |

---
