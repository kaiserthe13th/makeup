from functools import reduce
from typing import Optional, Union
from makeup import *

@task()
def hello(name: Optional[str] = None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

@task()
def say_hey():
    print("Hey!")

@task()
def check_env(name: str):
    val = get_env(name)
    if val is not None:
        print(f"{name} = {val}")
    else:
        print(f"{name} not found!")

@task()
def add(*args: Union[int, float]):
      print(reduce(lambda x, y: x + y, args, 0))
