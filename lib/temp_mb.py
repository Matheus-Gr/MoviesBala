from lib import temp_db, utils, photo_search


# -*- coding: utf-8 -*-


class MoviesBala:
    def __init__(self):
        self.__data_base = temp_db.DataBase()
        self.__photo_search = photo_search.PhotoSearch()

    def add_user(self, user_name: str):
        self.__data_base.insert_a_data(utils.USERS_TABLE + '(name)',
                                       "'" + user_name + "'")
        self.__data_base.create_column(user_name)

    def add_movie(self, title: str, user_id: int) -> bool:
        self.__data_base.insert_a_data(utils.MOVIES_TABLE + '(user_id,title)',
                                       str(user_id) + ',"' + title + '"')
        movie_id = self.__data_base.get_data_where(utils.MOVIE_ID_COLUMN,
                                                   utils.MOVIES_TABLE,
                                                   utils.TITLE_COLUMN,
                                                   '"' + title + '"')[0][0]

        error = self.__photo_search.scraping(title, movie_id)
        print('ERRO ============ ' + str(error))
        if error:
            self.delete_movie(movie_id)
            return False
        return True

    def delete_user(self, user_id: int):
        column = self.__data_base.get_data_where(utils.NAME_COLUMN,
                                                 utils.USERS_TABLE,
                                                 utils.USERS_ID_COLUMN,
                                                 str(user_id))[0][0]
        self.__data_base.delete_data(utils.USERS_TABLE,
                                     utils.USERS_ID_COLUMN,
                                     str(user_id))
        self.__data_base.remove_column(column)

    def delete_movie(self, movie_id: int):
        self.__data_base.delete_data(utils.MOVIES_TABLE,
                                     utils.MOVIE_ID_COLUMN, str(movie_id))
        self.__data_base.delete_data(utils.SCRAPING_TABLE,
                                     utils.MOVIE_ID_COLUMN,
                                     str(movie_id))

    def move_to_watched(self, movie_id: int, movies_table: list):
        user_id = -1
        title = ''
        for movie in movies_table:
            if movie[utils.MOVIE_ID_COLUMN] == movie_id:
                user_id = movie[utils.USERS_ID_COLUMN]
                title = movie[utils.TITLE_COLUMN]

        self.__data_base.insert_a_data(utils.WATCHED_TABLE +
                                       "(user_id,movie_id,title)",
                                       str(user_id) + "," +
                                       str(movie_id) + ",'" +
                                       title + "'")
        self.__data_base.delete_data(utils.MOVIES_TABLE,
                                     utils.MOVIE_ID_COLUMN, str(movie_id))

    def add_rating(self, user_name: str, movie_id: int, rating: float):
        self.__data_base.update_data(utils.WATCHED_TABLE, user_name,
                                     str(round(rating, 1)),
                                     utils.MOVIE_ID_COLUMN,
                                     str(movie_id))
        self.calculate_rotten(movie_id)

    def calculate_rotten(self, movie_id: int):
        row = list(self.__data_base.get_data_where(utils.ALL_COLUMNS,
                                                   utils.WATCHED_TABLE,
                                                   utils.MOVIE_ID_COLUMN,
                                                   str(movie_id))[0])

        for pop in range(4):
            row.pop(0)

        sum_of_grades = 0
        rating_quantity = 0
        for value in row:
            if value is not None:
                sum_of_grades += value
                rating_quantity += 1

        rotten = round((sum_of_grades * 100) / (rating_quantity * 5))

        self.__data_base.update_data(utils.WATCHED_TABLE, utils.ROTTEN_COLUMN,
                                     str(rotten), utils.MOVIE_ID_COLUMN,
                                     str(movie_id))

    def get_last_movie_user_id(self) -> int:
        total = self.__data_base.get_column_data('count(*)',
                                                 utils.WATCHED_TABLE)[0][0]

        user_id = self.__data_base.get_data_limited(utils.USERS_ID_COLUMN + ","
                                                    + utils.TITLE_COLUMN,
                                                    utils.WATCHED_TABLE,
                                                    str(total - 1),
                                                    '1')[0][0]
        return user_id

    def get_watched_list_ordered(self, highest: bool, user) -> list:
        if highest:
            order = 'DESC'
        else:
            order = 'ASC'

        data = self.__data_base.get_data_ordered(utils.ALL_COLUMNS,
                                                 utils.WATCHED_TABLE,
                                                 user, order)
        data_list = []
        for item in data:
            data_list.append(item[2])
        return data_list

    def get_poster_url(self, movie_id: int):
        return self.__data_base.get_data_where(utils.URL_COLUMN,
                                               utils.SCRAPING_TABLE,
                                               utils.MOVIE_ID_COLUMN,
                                               str(movie_id))[0][0]

    def download_poster(self, movie_id: int, scraping_table: list):
        url = None
        for poster in scraping_table:
            if poster[utils.MOVIE_ID_COLUMN] == movie_id:
                url = poster[utils.URL_COLUMN]
        if url is not None:
            self.__photo_search.download_image(url, movie_id)

    def has_grade(self, movie_id: int, user: str) -> bool:
        grade = self.__data_base.get_data_where(user, utils.WATCHED_TABLE,
                                                utils.MOVIE_ID_COLUMN,
                                                str(movie_id))[0][0]

        if grade is not None:
            return True
        return False

    def get_table(self, table: str) -> list:
        return self.__data_base.get_column_data(utils.ALL_COLUMNS, table)

    def get_movies_title_by_name(self, name: str, users_table: list,
                                 movies_table: list) -> list:
        user_id = self.get_user_id_by_name(name, users_table)
        return self.get_movies_title_by_user_id(user_id, movies_table)

    @staticmethod
    def get_movie_time_by_id(movie_id: int,
                             scraping_table: list) -> str:
        for movie in scraping_table:
            if movie[utils.MOVIE_ID_COLUMN] == movie_id:
                return movie[utils.TIME_COLUMN]

    @staticmethod
    def get_movie_id_by_title(title: str, table: list) -> int:
        for movie in table:
            if movie[utils.TITLE_COLUMN] == title:
                return movie[utils.MOVIE_ID_COLUMN]

    @staticmethod
    def get_user_name_by_id(user_id: int, user_table: list) -> str:
        for user in user_table:
            if user[utils.USERS_ID_COLUMN] == user_id:
                return user[utils.NAME_COLUMN]

    @staticmethod
    def get_rotten(title: str, table: list) -> list:
        for movie in table:
            if movie[utils.TITLE_COLUMN] == title:
                return movie[utils.ROTTEN_COLUMN]

    @staticmethod
    def get_user_id_by_name(name: str, users_table: list) -> int:
        for user in users_table:
            if user[utils.NAME_COLUMN] == name:
                return user[utils.USERS_ID_COLUMN]

    @staticmethod
    def get_movies_title_by_user_id(user_id: int, table: list) -> list:
        movies_titles = []
        for movie in table:
            if movie[utils.USERS_ID_COLUMN] == user_id:
                movies_titles.append(movie[utils.TITLE_COLUMN])
        return movies_titles
