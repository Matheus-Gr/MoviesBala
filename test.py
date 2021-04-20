from lib import utils, temp_mb, data_base, movies_bala

real_mb = movies_bala.MoviesBala()
mb = temp_mb.MoviesBala()
real_db = data_base.DataBase()
movies_table = []
user_table = []

data = mb.get_table(utils.USERS_TABLE)
for user in data:
    user_dict = {
        'user_id': user[0],
        'name': user[1]
    }
    user_table.append(user_dict)

# data = mb.get_table(utils.WATCHED_TABLE)
# for movie in data:
#     movie_dict = {
#         'movie_id': movie[0],
#         'user_id': movie[1],
#         'title': movie[2]
#     }
#     movies_table.append(movie_dict)
#
# data = mb.get_table(utils.MOVIES_TABLE)
# for movie in data:
#     movie_dict = {
#         'movie_id': movie[0],
#         'user_id': movie[1],
#         'title': movie[2]
#     }
#     movies_table.append(movie_dict)
#
# # real_db.reset_table(utils.USERS_TABLE)
# real_db.reset_table(utils.MOVIES_TABLE)
# real_db.reset_table(utils.WATCHED_TABLE)
# real_db.reset_table(utils.SCRAPING_TABLE)
#
# # for user in user_table:
# #     real_mb.add_user(user[utils.NAME_COLUMN])
#
# for movie in movies_table:
#     real_mb.add_movie(movie[utils.TITLE_COLUMN], movie[utils.USERS_ID_COLUMN])
#
# real_movies_table = []
# data = real_mb.get_table(utils.MOVIES_TABLE)
# for movie in data:
#     movie_dict = {
#         'movie_id': movie[0],
#         'user_id': movie[1],
#         'title': movie[2]
#     }
#     real_movies_table.append(movie_dict)
#
# for i in range(1, 43):
#     real_mb.move_to_watched(i, real_movies_table)

movies_table.clear()
data = mb.get_table(utils.WATCHED_TABLE)
movie_id = 1
for movie in data:
    m_dict = {
        'movie_id': movie_id,
        'user_id': movie[1],
        'title': movie[2],
        'Apu': movie[4],
        'Pikeno': movie[5],
        'Zero': movie[6],
        'John': movie[7],
        'Reizin': movie[8],
        'Curu': movie[9],
        'Beto': movie[10],
        'Juuj': movie[11],
    }
    movie_id += 1
    movies_table.append(m_dict)

print(movies_table)

for movie in movies_table:
    for user in user_table:
        if movie[user[utils.NAME_COLUMN]] is not None:
            real_mb.add_rating(user[utils.NAME_COLUMN],
                               movie[utils.MOVIE_ID_COLUMN],
                               movie[user[utils.NAME_COLUMN]])

# timelist = ['1:20', '2:52', '18']
#
# sec = 0
#
# for time in timelist:
#     if ':' in time:
#         elements = time.split(':')
#         sec += int(elements[0]) * 60 * 60
#         sec += int(elements[1]) * 60
#     else:
#         sec += int(time) * 60
#
# hours = (sec / 60) / 60
# minutes = (sec / 60) % 60
#
# print('{0}:{1}'.format(round(hours), round(minutes)))
