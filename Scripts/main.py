import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures


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
    '_ga_PEFEWHRN38': 'GS1.1.1696334904.3.1.1696334905.0.0.0',
}
headers = {
    'authority': 'dom.mingkh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.361993225.1696326727; _ym_uid=1696326727380789723; _ym_d=1696326727; _ym_isad=1; usercitycode=moskva; usercityname=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; usercitynamegenitive=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B; usercitynameprepositional=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5; userregionname=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; userregionnamegenitive=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B; userregionnameprepositional=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5; userregioncode=77; userregionurl=moskva; PHPSESSID=3apb7l8bss3l79j0nu1d1ds4e3; _ga_PEFEWHRN38=GS1.1.1696334904.3.1.1696334905.0.0.0',
    'referer': 'https://dom.mingkh.ru/novosibirskaya-oblast/novosibirsk/?page=343',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
response = requests.get('https://dom.mingkh.ru/novosibirskaya-oblast/novosibirsk/streets/', cookies=cookies, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Создаем пустой список для хранения названий улиц
    street_names = []

    # Находим все блоки <ul> с классом "list-unstyled list-columns"
    ul_blocks = soup.find_all('ul', class_='list-unstyled list-columns')

    for ul_block in ul_blocks:
        # Внутри каждого блока <ul> находим все элементы <a> (ссылки)
        links = ul_block.find_all('a')

        for link in links:
            href = link.get('href')  # Извлекаем значение атрибута "href" (ссылки)
            text = link.text  # Извлекаем текст ссылки

            # Добавьте условие для фильтрации ненужных ссылок
            if not href.startswith('#'):
                # Извлекаем название улицы (последний элемент после последнего слеша)
                parts = href.split('/')
                if len(parts) > 3:
                    street_name = parts[-1]
                    street_names.append(street_name)

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

    start_time = time.time()  # Запускаем таймер


    def fetch_street_data(street_name):
        response = requests.get(
            'https://dom.mingkh.ru/api/map/house/street/novosibirskaya-oblast/novosibirsk/' + street_name,
            cookies=cookies,
            headers=headers,
        )
        if response.status_code == 200:
            data = response.json()



    start_time = time.time()  # Запускаем таймер

    # Создаем пул потоков с использованием ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=80) as executor:
        # Запускаем задачи для каждой улицы в отдельном потоке
        futures = [executor.submit(fetch_street_data, street_name) for street_name in street_names]

        # Ожидаем завершения всех задач
        concurrent.futures.wait(futures)

    end_time = time.time()  # Останавливаем таймер
    elapsed_time = end_time - start_time  # Вычисляем время выполнения
    print(f'Время выполнения: {elapsed_time} секунд')

else:
    print("Не удалось загрузить страницу. Код состояния:", response.status_code)

