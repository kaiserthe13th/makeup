from functools import wraps
from typing import Optional
import pydantic


class TaskInfo(pydantic.BaseModel):
    name: Optional[str] = None


@pydantic.validate_arguments
def task(*, name: Optional[str] = None, **kwargs):
    def wrapper(wrapped):
        wrapped = pydantic.validate_arguments(wrapped)        
        wrapped._makeup_task = TaskInfo(name=name)
        return wrapped

    return wrapper
