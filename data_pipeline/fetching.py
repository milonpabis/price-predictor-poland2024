import aiohttp
from typing import List
from tqdm.asyncio import tqdm
from utils import *


async def fetch_html(url: str) -> List[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            html = await response.text()
            return html
        
@timelog("Fetching HTMLs")
async def fetch_all_htmls(idx_range: List[int]) -> List[List[str]]:
    urls = [ENDPOINT + str(i) for i in range(idx_range[0], idx_range[1]+1)]
    tasks = [fetch_html(url) for url in urls]
    return await tqdm.gather(*tasks, desc="Fetching HTMLs", leave=False)


@timelog("Fetching HTMLs")
async def fetch_all_htmls2(urls: List[str]) -> List[List[str]]:
    tasks = [fetch_html(url) for url in urls]
    return await tqdm.gather(*tasks, desc="Fetching HTMLs", leave=False)

        










