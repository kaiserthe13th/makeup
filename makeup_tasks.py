from typing import Optional
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
