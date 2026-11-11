from collections.abc import Callable
from functools import wraps
from time import perf_counter


def timed(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - started
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper


@timed
def work() -> int:
    return sum(range(100_000))


if __name__ == "__main__":
    print(work())
