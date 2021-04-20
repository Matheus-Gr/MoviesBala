import mysql.connector
from lib import utils


class DataBase:
    def __init__(self):
        self.data_base = mysql.connector.connect(
            host="mysqlserver.clud8bxqayre.sa-east-1.rds.amazonaws.com",
            user="apubala",
            passwd="Marte123-",
            database="movies_bala"

            # host="localhost",
            # user="root",
            # passwd="",
            # database="movies_bala"
        )
        self.CURSOR = self.data_base.cursor()

    def insert_a_data(self, table_with_parameters: str, data: str):
        sql_code = 'INSERT INTO ' + table_with_parameters + \
                   ' VALUES(' + data + ');'
        self.__sql_executor(sql_code)

    def create_column(self, user_name: str):
        sql_code = "ALTER TABLE " + utils.WATCHED_TABLE + \
                   " ADD " + user_name + " FLOAT NULL DEFAULT NULL;"
        self.__sql_executor(sql_code)

    def remove_column(self, column: str):
        sql_code = "ALTER TABLE " + utils.WATCHED_TABLE + \
                   " DROP " + column + ";"
        self.__sql_executor(sql_code)

    def get_column_data(self, wanted_field: str, table: str) -> list:
        sql_code = 'SELECT ' + wanted_field + ' FROM ' + table + ";"
        self.__sql_executor(sql_code)
        return self.CURSOR.fetchall()

    def get_data_where(self, wanted_field: str, table: str,
                       query_field: str, query_value: str) -> list:
        sql_code = 'SELECT ' + wanted_field + ' FROM ' + table + \
                   ' WHERE ' + query_field + ' = ' + query_value + ";"
        self.__sql_executor(sql_code)
        return self.CURSOR.fetchall()

    def update_data(self, table: str, wanted_field: str, new_value: str,
                    query_field: str, query_value: str):
        sql_code = 'UPDATE ' + table + \
                   ' SET ' + wanted_field + ' = "' + new_value + \
                   '" WHERE ' + query_field + ' = ' + query_value + ';'
        self.__sql_executor(sql_code)

    def delete_data(self, table: str, query_field: str, query_value: str):
        sql_code = "DELETE FROM " + table + \
                   " WHERE " + table + \
                   "." + query_field + " = " + query_value + ";"
        self.__sql_executor(sql_code)

    def reset_table(self, table: str):
        sql_code = 'TRUNCATE ' + table + ";"
        self.__sql_executor(sql_code)

    def get_data_limited(self, wanted_field: str, table: str,
                         start: str, end: str) -> list:
        sql_code = 'SELECT ' + wanted_field + ' FROM  ' + table + \
                   ' LIMIT ' + start + ',' + end + ';'
        self.__sql_executor(sql_code)
        return self.CURSOR.fetchall()

    def get_data_ordered(self, wanted_field: str, table: str,
                         user_name: str, order: str) -> list:
        sql_code = 'SELECT ' + wanted_field + ' FROM  ' + table + \
                   ' WHERE ' + user_name + ' IS NOT NULL  ORDER BY ' \
                   + user_name + ' ' + order + ';'
        self.__sql_executor(sql_code)
        return self.CURSOR.fetchall()

    def __sql_executor(self, sql_code: str):
        print("> {0}".format(sql_code))
        # try:
        self.CURSOR.execute(sql_code)
        # except:
        #     print('Connection error')
