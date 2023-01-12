from typing import Any


class Store:
    """
    A class to store information like a dict
    but it is easier to access and modify

    Instead of `dict["var_name"] = ...`, it enables `store.var_name`

    You are still welcome to use the dict way if you want to though so don't worry
    """

    def __init__(self, **stores: Any) -> None:
        object.__setattr__(self, "_Store__store", stores)

    def __setitem__(self, __name: str, __value: Any) -> None:
        object.__getattribute__(self, "_Store__store")[__name] = __value

    __setattr__ = __setitem__

    def __getitem__(self, __name: str) -> Any:
        return object.__getattribute__(self, "_Store__store")[__name]

    def __getattr__(self, __name: str) -> Any:
        try:
            return object.__getattribute__(self, "_Store__store")[__name]
        except KeyError as e:
            raise AttributeError(*e.args)
