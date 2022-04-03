from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def parce_name(URL):
    global ua
    global HEADERS
    URL = URL.strip()
    response = requests.get(URL, headers=HEADERS)
    try:
        soup = BeautifulSoup(response.content, 'lxml')
        global name
        name = soup.find('div', class_='content-page anime-page').find('h1').text.strip()
        voices = soup.find('ul', class_='animeVoices').find_all('li', recursive=False)

        return name, voices
    except AttributeError:
        return response, 0


def parce_new(name, k, voice):
    global ua
    global HEADERS
    URL_news = 'https://yummyanime.club/anime-updates'
    response = requests.get(URL_news, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    blocks = soup.find_all('span', class_='update-list-block')
    titles = []
    for block in blocks:
        titles.append({
            'name': block.find('span', class_='update-title').text.strip(),
            'update': block.find('span', class_='update-info').text.strip()
        })
    for title in titles:
        number_of_ser = ''
        if name == title['name'] and voice in title['update']:
            while title['update'][0].isdigit() == False:
                title['update'] = title['update'][1:]
            for i in title['update']:
                if i.isdigit():
                    number_of_ser += i
                else:
                    break
            number_of_ser = int(number_of_ser)
            if k < number_of_ser:
                return title['update'], number_of_ser
                break
            else:
                return '0', k
                break
        else:
            continue
    return '0', k


ua = UserAgent(cache=False)

HEADERS = {
    'User-Agent': ua.random
}
