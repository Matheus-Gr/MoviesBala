from lib import data_base, utils, photo_search


# -*- coding: utf-8 -*-

class MoviesBala:
    def __init__(self):
        self.__data_base = data_base.DataBase()
        self.__photo_search = photo_search.PhotoSearch()

    def add_user(self, user_name: str):
        self.__data_base.insert_a_data(utils.USERS_TABLE + '(name)',
                                       "'" + user_name + "'")
        self.__data_base.create_column(user_name)

    def add_movie(self, title: str, user_id: int):
        self.__data_base.insert_a_data(utils.MOVIES_TABLE + '(user_id,title)',
                                       str(user_id) + ',"' + title + '"')
        movie_id = self.__data_base.get_data_where(utils.MOVIE_ID_COLUMN,
                                                   utils.MOVIES_TABLE,
                                                   utils.TITLE_COLUMN,
                                                   "'" + title + "'")[0][0]
        self.__photo_search.get_image(title, movie_id)

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

    def move_to_watched(self, movie_id: int):
        user_id = self.__data_base.get_data_where(utils.USERS_ID_COLUMN,
                                                  utils.MOVIES_TABLE,
                                                  utils.MOVIE_ID_COLUMN,
                                                  str(movie_id))[0][0]
        title = self.__data_base.get_data_where(utils.TITLE_COLUMN,
                                                utils.MOVIES_TABLE,
                                                utils.MOVIE_ID_COLUMN,
                                                str(movie_id))[0][0]

        self.__data_base.insert_a_data(utils.WATCHED_TABLE +
                                       "(user_id,movie_id,title)",
                                       str(user_id) + "," +
                                       str(movie_id) + ",'" +
                                       title + "'")
        self.__data_base.delete_data(utils.MOVIES_TABLE,
                                     utils.MOVIE_ID_COLUMN, str(movie_id))

    def add_rating(self, user_id: int, movie_id, rating: float):
        user_name = self.__data_base.get_data_where(utils.NAME_COLUMN,
                                                    utils.USERS_TABLE,
                                                    utils.USERS_ID_COLUMN,
                                                    str(user_id))[0][0]

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
