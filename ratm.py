#!/usr/bin/python3

import fire


def index(name: str = "World") -> None:
    print(name)


if __name__ == '__main__':
    fire.Fire(index)
