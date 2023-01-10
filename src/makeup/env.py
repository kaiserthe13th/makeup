import os
from typing import List, Optional, Union
import dotenv
from makeup.utils import Store

options = Store(
    envfile=[".env"],
)


def env(
    name: str,
    default: Optional[str] = None,
    envfile: Union[str, List[str], None] = None,
) -> str:
    """
    Gets a variable from the environment

    Arguments:
        name: str =
            The name of the environment variable
        default: str | None =
            If the environment variable wasn't found
            returns a default instead of raising an Exception
        envfile: str | list[str] | None =
            Temporarily changes the loaded .env files

    Exceptions:
        KeyError:
            Raised if the environment variable was not found
            and there wasn't a default specified
    """
    # prepare envfile
    if envfile is None:
        envfile = options.envfile if isinstance(options.envfile, list) else []
    elif isinstance(envfile, str):
        envfile = [envfile]

    l = {}
    for ef in envfile:
        l.update(dotenv.dotenv_values(ef))
    l.update(os.environ)

    v = l.get(name)
    if v is not None:
        return v
    elif default is not None:
        return default
    else:
        raise KeyError(f"env var '{name}' not found")


def get_env(name: str, envfile: Union[str, List[str], None] = None) -> Optional[str]:
    """
    Gets a variable from the environment, returning `None` if it can't find it

    Arguments:
        name: str =
            The name of the environment variable
        envfile: str | list[str] | None =
            Temporarily changes the loaded .env files
    """
    try:
        return env(name, envfile=envfile)
    except KeyError:
        return None


def set_env(name: str, value: str) -> None:
    """
    Sets a variable in the environment

    Arguments:
        name: str =
            The name of the environment variable
        value: str =
            The value to set the variable to
    """
    os.environ[name] = value
