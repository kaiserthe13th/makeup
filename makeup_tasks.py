from functools import reduce
from typing import Union
from makeup import *

@task()
def add(*args: Union[int, float]):
    """
    Adds numbers together
    """
    print(reduce(lambda x, y: x + y, args, 0))
