import time
from functools import wraps

def timer(prefix="Execution time"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{prefix}: {end - start:.4f}s")
            return result
        return wrapper
    return decorator

@timer(prefix="Sorting took")
def slow_function():
    return sorted([x for x in range(1000000, 0, -1)])

slow_function()
