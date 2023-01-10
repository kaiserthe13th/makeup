from typing import Optional
import pydantic


class TaskInfo(pydantic.BaseModel):
    """
    Stores information about the tasks
    """

    name: str


@pydantic.validate_arguments
def task(*, name: Optional[str] = None, **kwargs):
    """
    A decorator to enable task wrapping
    """

    def wrapper(wrapped):
        wrapped = pydantic.validate_arguments(wrapped)
        wrapped._makeup_task = TaskInfo(
            name=name if name is not None else wrapped.__name__
        )
        return wrapped

    return wrapper
