import time
import asyncio
from functools import wraps


def timelog(prefix: str = "Time elapsed: ") -> None:
    def decorator(func):
        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = await func(*args, **kwargs)
                end = time.perf_counter()
                text = text_format(prefix, end-start, len(result) if hasattr(result, "__len__") else None)
                print(text)
                return result
        else:
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                text = text_format(prefix, end-start, len(result) if hasattr(result, "__len__") else None)
                print(text)
                return result
        return wrapper
    return decorator


def text_format(prefix: str, time: float, length: int = None) -> str:
    TEXT = f"{prefix:<30} | {time:<4.2f} s. |"
    if length:
        TEXT += f" Returned {length:<8} elements |"
    return TEXT