from lib import data_base, utils
from misc import localhostDataBase, moviesBALA

serverDB = data_base.DataBase()
localDB = localhostDataBase.LHDataBase()

localDB.reset_table(utils.USERS_TABLE)
localDB.reset_table(utils.MOVIES_TABLE)
localDB.reset_table(utils.WATCHED_TABLE)
localDB.reset_table(utils.POSTER_TABLE)

app = moviesBALA.MoviesBalaC()

user_data = serverDB.get_column_data(utils.NAME_COLUMN, utils.USERS_TABLE)

userList = []
for user in user_data:
    userList.append(user[0])

for user in userList:
    localDB.remove_column(user)
    app.add_user(user)

watchedData = serverDB.get_column_data(utils.TITLE_COLUMN, utils.WATCHED_TABLE)

moviesList = []
for movie in watchedData:
    moviesList.append(movie[0])

for movie in moviesList:
    user_id = serverDB.get_data_where(utils.USERS_ID_COLUMN,
                                      utils.WATCHED_TABLE, utils.TITLE_COLUMN,
                                      "'" + movie + "'")[0][0]
    app.add_movie(movie, user_id)

user_data = serverDB.get_column_data(utils.NAME_COLUMN, utils.USERS_TABLE)

userList = []
for user in user_data:
    userList.append(user[0])

for i in range(1, 37):
    app.move_to_watched(i)
    movie_id = app.get_movie_id_by_title(moviesList[i - 1], utils.WATCHED_TABLE)
    for user in userList:
        grade = serverDB.get_data_where(user, utils.WATCHED_TABLE,
                                        utils.MOVIE_ID_COLUMN, str(movie_id))[
            0][0]
        if grade is not None:
            app.add_rating(user, movie_id, float(grade))

moviesData = serverDB.get_column_data(utils.TITLE_COLUMN, utils.MOVIES_TABLE)

moviesList = []
for movie in moviesData:
    moviesList.append(movie[0])

for movie in moviesList:
    user_id = serverDB.get_data_where(utils.USERS_ID_COLUMN,
                                      utils.MOVIES_TABLE, utils.TITLE_COLUMN,
                                      "'" + movie + "'")[0][0]
    app.add_movie(movie, user_id)
