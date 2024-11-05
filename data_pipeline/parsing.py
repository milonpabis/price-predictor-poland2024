from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
from typing import Set, List, Callable
from multiprocessing import cpu_count
import json
from utils import *
from functools import partial

@timelog("HTMLs Parsing")
def parse_all_htmls(parse_fun: Callable, htmls: List[str], *args) -> Set[str]:
    urls = set()

    with ProcessPoolExecutor(max_workers=cpu_count()-1) as executor: # Process because of GIL
        results = executor.map(parse_fun, htmls, *args)

        for result in results:
            urls |= result
    return urls

def url_parser(html: str) -> Set[str]:
    soup = BeautifulSoup(html, 'html.parser')
    urls = set(MAIN_URI + a["href"] for a in soup.find_all("a") if "/pl/oferta" in a["href"] and a["href"].startswith("/pl"))
    return urls

def info_parser(html: str, url_idx: str) -> Set[tuple]:
    def get_info(d: dict) -> tuple:
        try:
            created_at = d["createdAt"] if "createdAt" in d else "-1"
            modified_at = d["modifiedAt"] if "modifiedAt" in d else "-1"
            
            target = d["target"]
            area = target["Area"] if "Area" in target else "-1"
            build_year = target["Build_year"] if "Build_year" in target else "-1"
            ownership = target["Building_ownership"][0] if "Building_ownership" in target else "-1"
            floor_num = target["Building_floors_num"] if "Building_floors_num" in target else "-1"
            floor = target["Floor_no"][0] if "Floor_no" in target else "-1"
            status = target["Construction_status"][0] if "Construction_status" in target else "-1"
            price = target["Price"] if "Price" in target else "-1"
            rooms = target["Rooms_num"][0] if "Rooms_num" in target else "-1"
            market = target["MarketType"] if "MarketType" in target else "-1"
            offer_type = target["ProperType"] if "ProperType" in target else "-1"

            loc = d["location"]
            longitude = loc["coordinates"]["longitude"] if "coordinates" in loc else "-1"
            latitude = loc["coordinates"]["latitude"] if "coordinates" in loc else "-1"
            city = loc["address"]["city"]["name"] if "address" in loc and "city" in loc["address"] else "-1"
            voivodeship = loc["address"]["province"]["name"] if "address" in loc and "province" in loc["address"] else "-1"

            extras = target["Extras_types"] if "Extras_types" in target else []
            balcony = str(int("balcony" in extras))
            terrace = str(int("terrace" in extras))
            lift = str(int("lift" in extras))
            garage = str(int("garage" in extras))

            result = set()
            result.add((url_idx, price, area, rooms, floor, floor_num,
                    status, ownership, build_year, balcony, terrace, lift, garage, market, offer_type,
                    city, voivodeship, longitude, latitude,
                    created_at, modified_at))

            return result
        except Exception as exception_parsing_info:
            print(exception_parsing_info)
            print(url_idx)
            raise ValueError("Error while parsing info")
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # get the stuff from info to tuple and return the tuple
        json_text = soup.find("script", {"id": "__NEXT_DATA__"})
        js = json.loads(json_text.contents[0])
        info = js["props"]["pageProps"]["ad"]
        result = get_info(info)
        return result
    except AttributeError as exception_rate_limit:
        print(exception_rate_limit)
        print("Rate limit reached")
    except Exception as exception:
        print(exception)

    result_exception = set()
    result_exception.add((url_idx, *["-1"]*20))
    return result_exception
    


