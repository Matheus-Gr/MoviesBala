import mysql.connector


class DataBase:
    def __init__(self):
        self.data_base = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="movies_bala"
        )
        self.CURSOR = self.data_base.cursor()

    def add_user(self, name: str):
        sql_code = "INSERT INTO users(name) VALUES('" + name + "');"
        self.__sql_executor(sql_code)
        self.add_rating_column(name)

    def delete_user(self, user_id: int):
        sql_code = "DELETE FROM users WHERE " \
                   "users.user_id = " + str(user_id) + ";"
        self.__sql_executor(sql_code)

    def add_movie(self, title: str, user_id: int):
        sql_code = "INSERT INTO to_be_sorted(flag,title)" \
                   "VALUES(" + str(user_id) + ",'" + title + "');"
        self.__sql_executor(sql_code)

    def delete_movie(self, movie_id: int):
        sql_code = "DELETE FROM to_be_sorted WHERE " \
                   "to_be_sorted.movie_id = " + str(movie_id) + ";"
        self.__sql_executor(sql_code)

    def move_to_watched_list(self, movie_id: int):
        sql_code = "INSERT INTO watched SELECT * FROM to_be_sorted " \
                   "WHERE movie_id = " + str(movie_id) + ";"
        self.CURSOR.execute(sql_code)
        self.delete_movie(movie_id)

    def add_rating_column(self, name: str):
        sql_code = "ALTER TABLE watched " \
                   "ADD " + name + " FLOAT NULL DEFAULT NULL;"
        self.__sql_executor(sql_code)

    def remove_rating_column(self, name: str):
        sql_code = "ALTER TABLE watched DROP " + name + ";"
        self.__sql_executor(sql_code)

    def update_watched_movie(self, movie_id: int, column: str, new_value: str):
        sql_code = "UPDATE watched SET " + column + " = " + new_value + \
                   " WHERE movie_id = " + str(movie_id) + ";"
        self.__sql_executor(sql_code)

    def get_watched_row(self, movie_id: str) -> list:
        sql_code = "SELECT * FROM watched WHERE " \
                   "movie_id = " + str(movie_id) + ";"
        self.CURSOR.execute(sql_code)
        return list(self.CURSOR.fetchall()[0])

    def get_movie_name(self, movie_id: str) -> str:
        sql_code = "SELECT title FROM to_be_sorted " \
                   "WHERE movie_id = " + movie_id + ";"
        self.__sql_executor(sql_code)
        return self.CURSOR.fetchall()[0][0]

    def __sql_executor(self, sql_code: str):
        self.CURSOR.execute(sql_code)

    def rate(self, name: str, movie_id: int, grade: float):
        sql_code = "UPDATE watched SET " + name + " = " + str(grade) + \
                   " WHERE movie_id = " + str(movie_id) + ";"
        self.__sql_executor(sql_code)

    def calculate_rotten(self, movie_id):
        sql_code = "SELECT * FROM watched WHERE " \
                   "movie_id = " + str(movie_id) + ";"
        self.CURSOR.execute(sql_code)
        entire_row = list(self.CURSOR.fetchall()[0])

        for pop in range(4):
            entire_row.pop(0)

        sum_of_grades = 0
        rating_quantity = 0

        for value in entire_row:
            if value is not None:
                sum_of_grades += value
                rating_quantity += 1

        # rotten = round(sum_of_grades / rating_quantity, 1)
        rotten = round((sum_of_grades * 100) / (rating_quantity * 5))

        sql_code = "UPDATE watched SET rotten = " + str(rotten) + \
                   " WHERE movie_id = " + str(movie_id) + ";"
        self.__sql_executor(sql_code)
