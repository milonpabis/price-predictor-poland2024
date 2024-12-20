import asyncio
from functools import wraps
import math
import time
import random
from typing import List

MAIN_URI = "https://www.otodom.pl"
ENDPOINT = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?viewType=listing&limit=72&page="

def generate_headers():
    return {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': random.choice(['en-US,en;q=0.8', 'pl-PL,pl;q=0.9', 'de-DE,de;q=0.9']),
        'user-agent': f'Mozilla/5.0 (Windows NT {random.choice(["10.0", "11.0"])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 130)}.0.0.0 Safari/537.36 OPR/{random.randint(110, 115)}.0.0.0',
        'cookie': f'PHPSESSID={random.randint(100000, 999999)}random_session_id; dfp_user_id=random_user_{random.randint(1000, 9999)};',
        'sec-ch-ua': f'"Not)A;Brand";v="99", "Opera";v="{random.randint(110, 115)}", "Chromium";v="{random.randint(100, 130)}"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': random.choice(['"Windows"', '"Linux"', '"macOS"']),
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'}



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
    TEXT = f"{prefix:<30} | {time:<5.2f} s. |"
    if length:
        TEXT += f" Returned {length:<8} elements |"
    return TEXT



def get_batches(l: int, r: int, batch_size: int) -> List[List[int]]:
    n_batches = math.ceil((r-l)/batch_size)
    return [[l+i*batch_size, l+(i+1)*batch_size if i != n_batches-1 else r] for i in range(n_batches)]




Q_GET_DISTINCT_URLS = """
SELECT u.url, u.id
FROM urls u
LEFT JOIN offers o ON u.id = o.url_id
WHERE u.id IN (
  SELECT DISTINCT ON(prefix) id
    FROM (
      SELECT SUBSTRING(url FROM '^(.*)-[^-]+$') prefix, id
      FROM urls
    ) AS subquery
) AND o.url_id IS NULL
ORDER BY u.id DESC;
"""

Q_GET_RAW_OFFERS = """
SELECT *
FROM offers
WHERE url_id NOT IN (
  SELECT DISTINCT url_id
  FROM offers_clean
);
"""