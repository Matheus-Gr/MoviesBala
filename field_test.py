from lib import utils, data_base
from reload import movies_bala

db = data_base.DataBase()
rmb = movies_bala.MoviesBala()

data = db.get_column_data('user_id, name', utils.USERS_TABLE)
user_list = []
for user in data:
    user_list.append(user)

data = db.get_column_data('user_id, title', utils.WATCHED_TABLE)
movies_list = []
for movie in data:
    movies_list.append(movie)
data = db.get_column_data('user_id, title', utils.MOVIES_TABLE)
for movie in data:
    movies_list.append(movie)

for user in user_list:
    print(user)
    rmb.add_user(user[1])

for movie in movies_list:
    rmb.add_movie(movie[1], movie[0])

movies_table = []
data = rmb.get_table(utils.MOVIES_TABLE)
for movie in data:
    movie_dict = {
        'movie_id': movie[0],
        'user_id': movie[1],
        'title': movie[2]
    }
    movies_table.append(movie_dict)

for i in range(1, 56):
    rmb.move_to_watched(i, movies_table)

watched_list = []
data = db.get_column_data('*', utils.WATCHED_TABLE)
for movie in data:
    watched_list.append(movie)

print(data)

movie_id = 1
for movie in watched_list:
    user_id = 4
    for user in user_list:
        if movie[user_id] is not None:
            rmb.add_rating(user[1], movie_id, movie[user_id])
        user_id += 1
    movie_id += 1
