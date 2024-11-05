import aiohttp
from typing import List
from tqdm.asyncio import tqdm
from utils import *


async def fetch_html(url: str) -> List[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=generate_headers()) as response:
            html = await response.text()
            return html

@timelog("Fetching HTMLs")
async def fetch_all_htmls(urls: List[str]) -> List[List[str]]:
    tasks = [fetch_html(url) for url in urls]
    return await tqdm.gather(*tasks, desc="Fetching HTMLs", leave=False)

        










