import aiohttp
from typing import List
from tqdm.asyncio import tqdm
from utils import timelog


HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'lang=pl; laquesisff=euads-4389#gre-12226#rer-165#rer-166#rst-73#rst-74; dfp_user_id=43c7f907-e9fb-4f73-ac51-172615941f23; _gcl_au=1.1.421783841.1712652353; st_userID=GA1.2.1804371638.1712652353__unlogged; OptanonAlertBoxClosed=2024-04-09T08:45:54.308Z; eupubconsent-v2=CP8zBjAP8zBjAAcABBENAvE8AP_gAAAAAAYgJ9NX_H_fbX9j8Xp0aft0eY1f99j7rsQxBhfJk-4FyLvW_JwX32EzNA16pqYKmRIEu3bBIQFlHIDUDUigaogVrTDMakWMgTNKJ6BEiFMRe2dYCF5vmQFD-QKY5tpvd3d52Te9_dv83dzyz4Vnn3Kp_-e1WJCdA5cgAAAAAAAAAAAAAAAQAAAAAAAAAQAIAAAAAAAAAAAAAAAAAAAAA_cBf78AAABgSCEAAgABcAFAAVAA4AB4AEEALwAwgBkAGoAPAAiABMACqAGYAN4AegA_ACEgEMARIAjgBLACaAGAAMOAZQBlgDZAHPAO4A74B7AHxAPsA_YB_gIAARSAi4CMAEagJEAksBPwFBgKgAq4BcwC9AGKANEAbQA3ABxIEegSIAnYBQ4CjwFIgLYAXIAu8BeYDBgGGwMjAyQBk4DMwGcwNXA1kBt4DcwG6gOCAcmA5cCbgQAuAA4AEgARwCDgEcAJoAX0BKwCbQFIAK5AWEAsQBbgC8gGIAMWAZCA0YBqYDaAG3AN0HALAAEQAOAA8AC4AJAAfgBHACgAGgARwA5ACAQEHAQgAiIBHACaAFQAOOAdIBKwCYgEygJtAUnArkCuwFiALUAW4AugBggDEAGLAMhAZMA0YBqYDXgG0ANsAbdA3MDdAHHgOWgc6Bz4E2x0E4ABcAFAAVAA4ACCAFwAagA8ACIAEwAKsAXABdADEAGYAN4AegA_QCGAIkASwAmgBRgDAAGGAMoAaIA2QBzwDuAO8Ae0A-wD9AH_ARQBGICOgJLAT8BQYCogKuAWIAucBeQF6AMUAbQA3ABxADqAH2ARfAj0CRAEyAJ2AUPAo8CkAFNAKsAWLAtgC2QFugLgAXIAu0Bd4C8wF9AMGAYaAx6BkYGSAMnAZUAywBmYDOQGmwNXA1gBt4DdQHFgOTAcuBNwCbwE4SABYABAADwA0ADkAI4AWIAvoCbQFJgK5AWIAvIBggDPAGjANTAbYA24BugDlgHPgTbIQIgAFgAUABcADEAGoATAAqgBcADEAG8APQAjgBgADngHcAd4A_wCKAEpAKDAVEBVwC5gGKANoAdQBHoCmgFWALFAWiAuABcgDIwGTgM5JQJQAEAALAAoAByAGAAYgA8ACIAEwAKoAXAAxQCGAIkARwAowBgADZAHeAPyAqICrgFzAMUAdQBEwCL4EegSIAo8BTQCxQFsALzgZGBkgDJwGcgNYAbeBNwCcJIAkABcAI4A7gCAAEHAI4AVABKwCYgE2gKTAW4AxYBlgDPAG6AOWAm2UARgAKAAuACQAFwARwAtgCOAHIAO4AfYBAACDgFiALqAa8A7YB_wExAJtAVIArsBbgC6AF5AMEAYsAyYBngDRgGpgNegbmBugDlgJtgThKQPAAFwAUABUADgAIIAYABqADwAIgATAAqgBiADMAH6AQwBEgCjAGAAMoAaIA2QBzgDvgH4AfoBFgCMQEdASUAoMBUQFXALmAXkAxQBtADcAHUAPaAfYBEwCL4EegSIAnYBQ4CkAFNAKsAWKAtgBcAC5AF2gLzAX0Aw2BkYGSAMnAZYAzmBrAGsgNvAbqA4IByYE3i0AoAGoAjgBgADuAL0AfYBTQCrAGZgTcLACgBlgEcAR6AmIBNoCuQGjANTAboA5YAA.f_wAAAAAAAAA; laquesissu=666@pin_click|1#666@zoom_map|1#666@pan_map|1; PHPSESSID=rmb36bnalblmn4g7bbar16lnd6; mobile_default=desktop; ninja_user_status=unlogged; smcx_430910767_last_shown_at=1715524368033; _gid=GA1.2.932160579.1716542441; laquesis=eure-19653@b#eure-19720@b#eure-25578@b#eure-25610@a#eure-26485@a#resl-427@b#resl-648@a#seore-998@b#sfs-1183@a#smr-3411@a; lqstatus=1716547712|18fa9e7044cx294e3764|eure-19720#resl-648#smr-3411#sfs-1183#eure-26485#eure-25578#eure-19653||; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+24+2024+12%3A34%3A44+GMT%2B0200+(czas+%C5%9Brodkowoeuropejski+letni)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1add18f4-8ac2-4629-9787-a862c4ed7a1e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2Cgad%3A1&geolocation=%3B&AwaitingReconsent=false; _ga=GA1.1.1804371638.1712652353; _ga_20T1C2M3CQ=GS1.1.1716542441.20.1.1716546885.58.0.0; _ga_6PZTQNYS5C=GS1.1.1716544661.21.1.1716546885.58.0.0; onap=18ec208f9bcx4af0f441-16-18fa9e7044cx294e3764-301-1716549068; __gads=ID=8697554daeb46e78:T=1712652354:RT=1716547266:S=ALNI_MbVJygBMTOjQ9oRQ1l-kRF8vSzxfQ; __gpi=UID=00000de810a1f421:T=1712652354:RT=1716547266:S=ALNI_MbNDORPHcmuZrna2Ff3jVOdjiBu1g; __eoi=ID=0bb58e9662bc0efe:T=1713095891:RT=1716547266:S=AA-AfjbirfVdeNo6-j0PeaMkbRt4',
  'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'
}

ENDPOINT = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?viewType=listing&limit=72&page="
MAIN_URI = "https://www.otodom.pl"

async def fetch_urls_from_page(url: str) -> List[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            html = await response.text()
            return html
        
@timelog("Fetching URLs")
async def fetch_all_urls(idx_range: List[int]) -> List[List[str]]:
    urls = [ENDPOINT + str(i) for i in range(idx_range[0], idx_range[1]+1)]
    tasks = [fetch_urls_from_page(url) for url in urls]
    return await tqdm.gather(*tasks, desc="Fetching URLs", leave=False)

        










