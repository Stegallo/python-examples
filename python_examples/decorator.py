"""Decorator module."""
from typing import Any, Callable


def log(message: str) -> None:
    """Logs message."""
    print(message)


def my_decorator(func: Callable) -> Any:
    """Generic decorator example."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        log("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        log("Something is happening after the function is called.")
        return result

    return wrapper


def log_hi(person_name: str) -> None:
    """Prints hi."""
    log(f"hi {person_name}")


# alternative way of decorating the function
decorated_log_hi = my_decorator(log_hi)


@my_decorator
def decorated_log_hello(person_name: str) -> None:
    """Prints hello."""
    log(f"hello {person_name}")


def main() -> None:
    """Main func."""
    decorated_log_hi("John")
    decorated_log_hello("Doe")


if __name__ == "__main__":
    main()
