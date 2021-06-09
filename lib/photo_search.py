from bs4 import BeautifulSoup
from lib import data_base
from PIL import Image
import requests
import json
import time
import os


class PhotoSearch:
    def __init__(self):
        self.IMDB_URL = 'https://www.imdb.com'
        self.SAVE_FOLDER = './public/posters'
        self.SLEEP_TIME = 0
        self.DATA_BASE = data_base.DataBase()
        self.WIDTH = 182
        self.HEIGHT = 268
        if not os.path.exists(self.SAVE_FOLDER):
            os.mkdir(self.SAVE_FOLDER)

    def scraping(self, movie_title: str, movie_id: int) -> int:
        print('\nStart searching for {0}...'.format(movie_title))

        movie_title = self.__treat_string(movie_title)
        search_url = self.IMDB_URL + '/find?q=' + movie_title

        # SEARCHING MOVIE
        print("Searched url: " + search_url)

        time.sleep(self.SLEEP_TIME)
        response = requests.get(search_url)
        html = response.text
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        link = {}
        for result in soup.findAll('td', {'class': 'primary_photo'}, limit=1):
            link = result.find('a', href=True)

        try:
            search_url = self.IMDB_URL + link['href']
        except:
            print('Movie not found! :/')
            return 1

        # SEARCHING POSTER AND TIME
        print("Sub searched url: " + search_url)

        time.sleep(self.SLEEP_TIME)
        response = requests.get(search_url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        scrap = soup.find('script', type='application/ld+json')

        movie_time = ''
        image_link = ''
        if scrap:
            image_link = json.loads(scrap.string)['image']
            movie_time = json.loads(scrap.string)['duration']
            movie_time = str(movie_time).replace("PT", " ")
            movie_time = movie_time.replace("H", "h ")
            movie_time = movie_time.replace("M", "min")

        print("Image Link: " + image_link)
        print("Image Duration: " + movie_time)

        if image_link != '' and movie_time != '':
            try:
                self.DATA_BASE.insert_a_data('scraping(movie_id,url,time)',
                                             str(movie_id) + ',"' +
                                             image_link + '","' +
                                             movie_time + '"')
            except:
                return 1
        else:
            return 1

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

    def download_image(self, url: str, movie_id: int):
        image_name = self.SAVE_FOLDER + '/' + str(movie_id) + '.jpg'

        if not os.path.exists(image_name):
            print("Starting download...")

            try:
                response = requests.get(url, timeout=5)
                time.sleep(self.SLEEP_TIME)
            except requests.exceptions.Timeout:
                print('################################ TIME OUT')
                return 1
            except:
                print('################################ Movie not found! :/')
                return 1

            with open(image_name, 'wb') as file:
                file.write(response.content)
                print("Download finished!")

            img = Image.open(image_name)
            img = img.resize((self.WIDTH, self.HEIGHT))
            img.save(image_name)
        # else:
        #     print('Already downloaded')
