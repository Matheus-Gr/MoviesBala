import json
from lib import data_base, photo_search, movies_bala

data_base = data_base.DataBase()
# photo_downloader = photo_search.PhotoSearch()
app = movies_bala.MoviesBala()

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
file.close()

# app.move_to_watched(41)
# app.get_watched_list_ordered(True,'Apu')
# print(app.get_last_movie_user_id())

data_base.reset_table('users')
data_base.reset_table('movies')
data_base.reset_table('watched')

users_list = ['Apu', 'Pikeno', 'Zero', 'John', 'Rei', 'Curu', 'Beto', 'Juuj']

for user in users_list:
    data_base.remove_column(user)
    app.add_user(user)


for title in data['ViewedList']:
    user_id = 0

    if title['user'] == 'Apu':
        user_id = 1
    elif title['user'] == 'Pikeno':
        user_id = 2
    elif title['user'] == 'Zero':
        user_id = 3
    elif title['user'] == 'John':
        user_id = 4
    elif title['user'] == 'Rei':
        user_id = 5
    elif title['user'] == 'Curu':
        user_id = 6

    app.add_movie(title['title'], user_id)

for name in data['names']:
    user_id = int(name['_id']) + 1
    for title in name['movies']:
        app.add_movie(title, user_id)

for i in range(1, 36):
    app.move_to_watched(i)

movie_id = 0
user_id = 100000
for movie in data['ViewedList']:
    movie_id += 1
    for grade in movie['rating']:
        app.add_rating(grade['name'], movie_id, float(grade['grade']))

