import requests
from bs4 import BeautifulSoup
import json

cookies = {
    '_ga': 'GA1.1.361993225.1696326727',
    '_ym_uid': '1696326727380789723',
    '_ym_d': '1696326727',
    '_ym_isad': '1',
    'usercitycode': 'moskva',
    'usercityname': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
    'usercitynamegenitive': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B',
    'usercitynameprepositional': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5',
    'userregionname': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
    'userregionnamegenitive': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B',
    'userregionnameprepositional': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5',
    'userregioncode': '77',
    'userregionurl': 'moskva',
    'PHPSESSID': '3apb7l8bss3l79j0nu1d1ds4e3',
    '_ga_PEFEWHRN38': 'GS1.1.1696330815.2.1.1696331016.0.0.0',
}

headers = {
    'authority': 'dom.mingkh.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_ga=GA1.1.361993225.1696326727; _ym_uid=1696326727380789723; _ym_d=1696326727; _ym_isad=1; usercitycode=moskva; usercityname=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; usercitynamegenitive=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B; usercitynameprepositional=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5; userregionname=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; userregionnamegenitive=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B; userregionnameprepositional=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5; userregioncode=77; userregionurl=moskva; PHPSESSID=3apb7l8bss3l79j0nu1d1ds4e3; _ga_PEFEWHRN38=GS1.1.1696330815.2.1.1696331016.0.0.0',
    'referer': 'https://dom.mingkh.ru/novosibirskaya-oblast/novosibirsk/molodezhi-bulvar',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(
    'https://dom.mingkh.ru/api/map/house/street/novosibirskaya-oblast/novosibirsk/molodezhi-bulvar',
    cookies=cookies,
    headers=headers,
)

if response.status_code == 200:
    data = response.json()
    for i in range(len(data["features"])):
        print(data["features"][i]["properties"]["year"], data["features"][i]["geometry"]["coordinates"])

