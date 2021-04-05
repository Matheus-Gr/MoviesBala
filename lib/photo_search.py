import os
import requests
from bs4 import BeautifulSoup
import time


class PhotoSearch:
    def __init__(self):
        self.IMDB_URL = 'https://www.imdb.com/'
        self.SAVE_FOLDER = '../posters'
        self.SLEEP_TIME = 0
        if not os.path.exists(self.SAVE_FOLDER):
            os.mkdir(self.SAVE_FOLDER)

    def get_image(self, movie_title: str, movie_id: int) -> int:
        print('\nStart searching for {0}...'.format(movie_title))

        movie_title = self.__treat_string(movie_title)
        search_url = self.IMDB_URL + 'find?q=' + movie_title
        print("Searched url: " + search_url)

        response = requests.get(search_url)
        time.sleep(self.SLEEP_TIME)

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        link = {}
        for result in soup.findAll('td', {'class': 'primary_photo'}, limit=1):
            link = result.find('a', href=True)

        try:
            search_url = self.IMDB_URL + link['href']
        except:
            print('################################ Movie not found! :/')
            return 1

        print("Sub searched url: " + search_url)
        response = requests.get(search_url)
        time.sleep(self.SLEEP_TIME)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        image_link = ''
        for result in soup.findAll('div', {'class': 'poster'}):
            image = result.find('img', src=True)
            image_link = image['src']

        print("Image Link: " + image_link)
        print("Starting download...")

        try:
            response = requests.get(image_link, timeout=5)
            time.sleep(self.SLEEP_TIME)
        except requests.exceptions.Timeout:
            print('################################ TIME OUT')
            return 1
        except:
            print('################################ Movie not found! :/')
            return 1

        image_name = self.SAVE_FOLDER + '/' + str(movie_id) + '.jpg'
        with open(image_name, 'wb') as file:
            file.write(response.content)

        print("Download finished!")
        return 0

    @staticmethod
    def __treat_string(movie_title: str) -> str:
        string_list = list(movie_title)
        i = 0
        for char in string_list:
            if char == ' ':
                string_list[i] = '+'
            elif char == ',':
                string_list[i] = '%2C'
            i += 1
        return ''.join(string_list)
