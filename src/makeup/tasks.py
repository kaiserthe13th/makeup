from typing import Optional
import pydantic


class TaskInfo(pydantic.BaseModel):
    """
    Stores information about tasks
    """

    name: str
    doc: Optional[str] = None


@pydantic.validate_arguments
def task(*, name: Optional[str] = None, **kwargs):
    """
    A decorator to enable task creation much more easily

    Arguments:
      Keyword-Only:
        name: str | None =
            an alternative name for the task
    """

    def wrapper(wrapped):
        wrapped = pydantic.validate_arguments(wrapped)
        wrapped._makeup_task = TaskInfo(
            name=name if name is not None else wrapped.__name__, doc=wrapped.__doc__
        )
        return wrapped

    return wrapper
