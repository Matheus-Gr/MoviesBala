from lib import utils, movies_bala
from collections import Counter
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

import os
import random

mb = movies_bala.MoviesBala()

show_text = False
movie_list_items = {}
watched_tree_items = {}
last_movie_draw = ''
draw_movie_id = -1
arrow_up = True

# TABLES
users_table = []
movies_table = []
watched_table = []
scraping_table = []

# LISTS
global_users_list = []
global_movies_list = []
global_watched_list = []


def init_data():
    build_users_table()
    build_user_list()

    build_movies_table()
    build_movies_list()

    build_watched_table()
    build_watched_list()

    update_user_list_ui()
    update_movie_list_ui()
    update_watched_list_ui()

    update_statistics()

    ui.confirmButton.setVisible(False)

    if not os.path.exists(utils.PASSWORD_FILE):
        ui.drawButton.setEnabled(False)


def build_users_table():
    users_table.clear()
    data = mb.get_table(utils.USERS_TABLE)
    for user in data:
        user_dict = {
            'user_id': user[0],
            'name': user[1]
        }
        users_table.append(user_dict)


def build_movies_table():
    movies_table.clear()
    data = mb.get_table(utils.MOVIES_TABLE)
    for movie in data:
        movie_dict = {
            'movie_id': movie[0],
            'user_id': movie[1],
            'title': movie[2]
        }
        movies_table.append(movie_dict)


def build_watched_table():
    watched_table.clear()
    data = mb.get_table(utils.WATCHED_TABLE)
    for watched in data:
        movie_dict = {
            'movie_id': watched[0],
            'user_id': watched[1],
            'title': watched[2],
            'rotten': watched[3],
        }
        index = 4
        for user in global_users_list:
            movie_dict[user] = watched[index]
            index += 1

        watched_table.append(movie_dict)


def build_scraping_table():
    scraping_table.clear()
    data = mb.get_table(utils.SCRAPING_TABLE)
    for movie in data:
        movie_dict = {
            'movie_id': movie[0],
            'url': movie[1],
            'time': movie[2]
        }
        scraping_table.append(movie_dict)


def build_user_list():
    global_users_list.clear()
    for user in users_table:
        global_users_list.append(user[utils.NAME_COLUMN])


def build_movies_list():
    global_movies_list.clear()
    for movie in movies_table:
        global_movies_list.append(movie[utils.TITLE_COLUMN])


def build_watched_list():
    global_watched_list.clear()
    for movie in watched_table:
        global_watched_list.append(movie[utils.TITLE_COLUMN])


def update_movie_list_ui(movies_list=None):
    build_scraping_table()
    if movies_list is None:
        movies_list = global_movies_list

    movie_list_items.clear()
    ui.listMovies.clear()

    for movie in movies_table:
        title = movie[utils.TITLE_COLUMN]
        if title in movies_list:
            movie_id = movie[utils.MOVIE_ID_COLUMN]
            user_id = movie[utils.USERS_ID_COLUMN]
            user_name = mb.get_user_name_by_id(user_id, users_table)
            movie_time = mb.get_movie_time_by_id(movie_id, scraping_table)
            item_text = "{0}\n{1}\n{2}".format(title,
                                               str(movie_time),
                                               user_name)
            if show_text:
                item = QListWidgetItem(item_text)
            else:
                item = QListWidgetItem()

            try:
                mb.download_poster(movie_id, scraping_table)
                item.setIcon(
                    QIcon(r"./public/posters/{0}.jpg".format(movie_id)))
            except:
                print('Was no cover')
            movie_list_items[str(item)] = movie_id

            ui.listMovies.addItem(item)


def update_watched_list_ui(watched_list=None):
    if watched_list is None:
        watched_list = global_watched_list

    watched_tree_items.clear()
    ui.watchedTree.clear()

    position = 1
    for title in watched_list:
        for movie in watched_table:
            if title == movie[utils.TITLE_COLUMN]:
                movie_id = movie[utils.MOVIE_ID_COLUMN]
                rotten = movie[utils.ROTTEN_COLUMN]

                item_movie = QTreeWidgetItem()
                try:
                    mb.download_poster(movie_id, scraping_table)
                    item_movie.setIcon(0,
                                       QIcon(r"./public/posters/{0}.jpg".format(
                                           movie_id)))
                except:
                    print('Was no poster')

                if rotten is not None:
                    item_movie.setText(0,
                                       "{0}#  {1}\n"
                                       "Rotten:{2}%".format(position, title,
                                                            round(rotten)))
                else:
                    item_movie.setText(0, "{0}#  {1}".format(position, title))

                for user in global_users_list:
                    if movie[user] is not None:
                        item_grade = QTreeWidgetItem()
                        item_grade.setText(0,
                                           "{0}: {1}".format(user, movie[user]))
                        item_movie.addChild(item_grade)

                watched_tree_items[str(item_movie)] = movie_id

                ui.watchedTree.addTopLevelItem(item_movie)
                position += 1


def update_user_list_ui():
    # Page 1
    ui.movieFilter.clear()
    ui.movieFilter.addItem('None')
    ui.movieFilter.addItems(global_users_list)

    ui.userPicker.clear()
    ui.userPicker.addItem('None')
    ui.userPicker.addItems(global_users_list)

    ui.listUser.clear()
    ui.listUser.addItems(global_users_list)

    # Page 2
    users_with_movies = []
    users_id_list = []
    for movie in movies_table:
        users_id_list.append(movie[utils.USERS_ID_COLUMN])

    for user in users_table:
        if user[utils.USERS_ID_COLUMN] in users_id_list:
            users_with_movies.append(user[utils.NAME_COLUMN])

    ui.whoWillWatchComboBox.clear()
    ui.whoWillWatchComboBox.addItem('None')
    ui.whoWillWatchComboBox.addItems(users_with_movies)

    # Page 3
    ui.userRating.clear()
    ui.userRating.addItem('None')
    ui.userRating.addItems(global_users_list)

    ui.ratingColumnPicker.clear()
    ui.ratingColumnPicker.addItem('Rotten')
    ui.ratingColumnPicker.addItems(global_users_list)

    # Page 4
    ui.userStatistics.clear()
    ui.userStatistics.addItem('None')
    ui.userStatistics.addItems(global_users_list)


def users_updates():
    build_users_table()
    build_user_list()
    update_user_list_ui()


def movies_updates():
    build_movies_table()
    build_movies_list()
    update_movie_list_ui()


def watched_updates():
    build_watched_table()
    build_watched_list()
    update_watched_list_ui()


def show_page_1():
    ui.appPages.setCurrentIndex(0)


def show_page_2():
    ui.appPages.setCurrentIndex(1)


def show_page_3():
    ui.appPages.setCurrentIndex(2)


def show_page_4():
    ui.appPages.setCurrentIndex(3)


def reset_feedbacks():
    ui.feedBackAdded.setText('')
    ui.feedBackUsers.setText('')
    ui.gradeFeedBackLabel.setText('')


# Page 1
def filter_movie_list():
    user = ui.movieFilter.currentText()

    if user != 'None':
        movies_titles = mb.get_movies_title_by_name(user, users_table,
                                                    movies_table)
        update_movie_list_ui(movies_titles)
    else:
        movies_updates()


def add_movie():
    reset_feedbacks()
    title = ui.movieLineEdit.text()

    if title != '':
        user = ui.userPicker.currentText()
        if user != 'None':
            ui.movieLineEdit.setText('')
            user_id = mb.get_user_id_by_name(user, users_table)

            not_on_list = True
            for movie in movies_table:
                if movie[utils.TITLE_COLUMN] == title:
                    not_on_list = False
            for movie in watched_table:
                if movie[utils.TITLE_COLUMN] == title:
                    not_on_list = False

            if not_on_list:
                added = mb.add_movie(title, user_id)
                if added:
                    print('Uai')
                    ui.feedBackAdded.setText('Movie added successfully! ')
                    ui.feedBackAdded.setStyleSheet('QLabel#feedBackAdded{'
                                                   'color: rgb(51, 228, 154);}')
                elif not added:
                    ui.feedBackAdded.setText('Movie not found!')
                    ui.feedBackAdded.setStyleSheet('QLabel#feedBackAdded{'
                                                   'color: rgb(255, 9, 9);}')
            else:
                ui.feedBackAdded.setText('Movie already on Movies Bala!')
                ui.feedBackAdded.setStyleSheet('QLabel#feedBackAdded{'
                                               'color: rgb(255, 9, 9);}')
            # UPDATES
            build_scraping_table()
            movies_updates()
            users_updates()
    else:
        ui.feedBackAdded.setText('')


def delete_movie():
    reset_feedbacks()
    item = ui.listMovies.currentItem()

    if item:
        movie_id = movie_list_items.get(str(item))

        mb.delete_movie(movie_id)

        ui.feedBackAdded.setText('Movie deleted successfully! ')
        ui.feedBackAdded.setStyleSheet('QLabel#feedBackAdded{'
                                       'color: rgb(51, 228, 154);}')
        # UPDATES
        movies_updates()
        users_updates()
        build_scraping_table()
        try:
            os.remove("./public/posters/" + str(movie_id) + ".jpg")
        except:
            print('Was no poster')
    else:
        ui.feedBackAdded.setText('')


def add_user():
    reset_feedbacks()
    user = ui.registerUserLineEdit.text()
    if user != '':
        ui.registerUserLineEdit.setText('')
        if ' ' not in user:
            user = str(user)
            if not user.isdecimal():
                mb.add_user(user)

                # UPDATES
                build_users_table()
                build_user_list()
                watched_updates()
                update_user_list_ui()

                ui.feedBackUsers.setText('User added successfully! ')
                ui.feedBackUsers.setStyleSheet('QLabel#feedBackUsers{'
                                               'color: rgb(51, 228, 154);}')
            else:
                ui.feedBackUsers.setText('Invalid input!')
                ui.feedBackUsers.setStyleSheet('QLabel#feedBackUsers{'
                                               'color: rgb(255, 9, 9);}')
        else:
            ui.feedBackUsers.setText('Invalid input!')
            ui.feedBackUsers.setStyleSheet('QLabel#feedBackUsers{'
                                           'color: rgb(255, 9, 9);}')


def delete_user():
    reset_feedbacks()
    if os.path.exists(utils.PASSWORD_FILE):
        item = ui.listUser.selectedItems()
        if item:
            user_name = item[0].text()
            user_id = mb.get_user_id_by_name(user_name, users_table)
            movies_list = mb.get_movies_title_by_user_id(user_id, movies_table)
            if movies_list:
                for movie in movies_list:
                    movie_id = mb.get_movie_id_by_title(movie, movies_table)
                    mb.delete_movie(movie_id)
                    try:
                        os.remove("./public/posters/" + str(movie_id) + ".jpg")
                    except:
                        print('Was no poster')

            mb.delete_user(user_id)
            ui.feedBackUsers.setText('User and movies deleted successfully! ')
            ui.feedBackUsers.setStyleSheet('QLabel#feedBackUsers{'
                                           'color: rgb(51, 228, 154);}')
            # UPDATES
            movies_updates()
            users_updates()
    else:
        ui.feedBackUsers.setText('You do not have permission!')
        ui.feedBackUsers.setStyleSheet('QLabel#feedBackUsers{'
                                       'color: rgb(255, 9, 9);}')


def set_list_mode():
    reset_feedbacks()
    ui.listMovies.setFlow(QListWidget.TopToBottom)
    ui.listMovies.setWrapping(False)
    global show_text
    show_text = True

    update_movie_list_ui()


def set_grid_mode():
    reset_feedbacks()
    ui.listMovies.setFlow(QListWidget.LeftToRight)
    ui.listMovies.setWrapping(True)
    global show_text
    show_text = False

    update_movie_list_ui()


# Page 2
def add_who_watch():
    user = ui.whoWillWatchComboBox.currentText()

    if user != 'None':
        ui.whoWillWatchList.addItem(user)
        ui.whoWillWatchComboBox.setCurrentText('None')


def delete_who_watch():
    user = ui.whoWillWatchList.selectedItems()

    if user:
        ui.whoWillWatchList.takeItem(ui.whoWillWatchList.row(user[0]))


def draw_movie():
    if os.path.exists(utils.PASSWORD_FILE):
        users_count = ui.whoWillWatchList.count()

        if users_count != 0:
            who_watching = []
            user_name_list = []
            for i in range(users_count):
                user = ui.whoWillWatchList.takeItem(0).text()
                user_id = mb.get_user_id_by_name(user, users_table)
                who_watching.append(user_id)
                user_name_list.append(user)

            for user in user_name_list:
                ui.whoWillWatchList.addItem(user)

            last_user_id = mb.get_last_movie_user_id()
            if last_user_id in who_watching:
                who_watching.remove(last_user_id)

            if not who_watching:
                return

            movies_list = []
            for user_id in who_watching:
                user_movies = mb.get_movies_title_by_user_id(user_id,
                                                             movies_table)
                for movie in user_movies:
                    movies_list.append(movie)

            user_index_draw = -1
            stop = False
            while not stop:
                try:
                    user_index_draw = random.randrange(len(who_watching))
                    stop = True
                except:
                    print('Invalid draw')

            user_draw = who_watching[user_index_draw]

            movies_list.clear()
            movies_list = mb.get_movies_title_by_user_id(user_draw,
                                                         movies_table)

            stop = False
            global last_movie_draw
            movie_draw = ''
            while not stop:
                movie_index = random.randrange(len(movies_list))
                movie_draw = movies_list[movie_index]
                if last_movie_draw != '' and len(movies_list) > 1:
                    if movie_draw != last_movie_draw:
                        last_movie_draw = movie_draw
                        stop = True
                else:
                    last_movie_draw = movie_draw
                    stop = True

            ui.titleLabel.setText(movie_draw)
            user_name = mb.get_user_name_by_id(user_draw, users_table)
            global draw_movie_id
            draw_movie_id = mb.get_movie_id_by_title(movie_draw, movies_table)
            poster_path = './public/posters/' + str(draw_movie_id) + '.jpg'
            ui.posterLabel.setPixmap(QtGui.QPixmap(poster_path))
            ui.confirmButton.setVisible(True)

            movie_time = ''
            for movie in scraping_table:
                if movie[utils.MOVIE_ID_COLUMN] == draw_movie_id:
                    movie_time = movie[utils.TIME_COLUMN]

            ui.userNameLabel.setText("{0} - {1}".format(user_name, movie_time))


def confirm_draw():
    global draw_movie_id
    if draw_movie_id != -1:
        mb.move_to_watched(draw_movie_id, movies_table)

        draw_movie_id = -1
        ui.confirmButton.setVisible(False)
        users_count = ui.whoWillWatchList.count()
        ui.posterLabel.setPixmap(QtGui.QPixmap(''))
        ui.titleLabel.setText('')
        ui.userNameLabel.setText('')
        for i in range(users_count):
            ui.whoWillWatchList.takeItem(0).text()

        # UPDATES
        movies_updates()
        watched_updates()
        users_updates()
        update_statistics()


# Page 3
def rating():
    reset_feedbacks()
    item = ui.watchedTree.selectedItems()
    if item:
        move_id = watched_tree_items.get(str(item[0]))
        user_name = ui.userRating.currentText()

        grade = ui.gradeLineEdit.text()

        if grade != '' and user_name != 'None' and move_id is not None:
            if '.' in grade:
                if '.5' not in grade and '.0' not in grade:
                    ui.gradeFeedBackLabel.setText('Invalid input!')
                    ui.gradeFeedBackLabel.setStyleSheet(
                        'QLabel#gradeFeedBackLabel{'
                        'color: rgb(255, 5, 5);}')
                    return
            try:
                grade = float(grade)
            except:
                ui.gradeFeedBackLabel.setText('Invalid input!')
                ui.gradeFeedBackLabel.setStyleSheet('QLabel#gradeFeedBackLabel{'
                                                    'color: rgb(255, 5, 5);}')
                return

            if grade > 5 or grade < 0 or grade % 0.5 != 0:
                ui.gradeFeedBackLabel.setText('Invalid input!')
                ui.gradeFeedBackLabel.setStyleSheet('QLabel#gradeFeedBackLabel{'
                                                    'color: rgb(255, 5, 5);}')
                return

            if mb.has_grade(move_id, user_name):
                ui.gradeFeedBackLabel.setText('Edited successfully!')
                ui.gradeFeedBackLabel.setStyleSheet(
                    'QLabel#gradeFeedBackLabel{'
                    'color: rgb(51, 228, 154);}')
            else:
                ui.gradeFeedBackLabel.setText('Added successfully!')
                ui.gradeFeedBackLabel.setStyleSheet(
                    'QLabel#gradeFeedBackLabel{'
                    'color: rgb(51, 228, 154);}')
            mb.add_rating(user_name, move_id, grade)

            watched_updates()
            update_statistics()
            ui.userRating.setCurrentText('None')
            ui.gradeLineEdit.setText('')


def order_watched():
    reset_feedbacks()
    order = ui.orderComboBox.currentText()
    user = ui.ratingColumnPicker.currentText()
    global arrow_up

    if order == 'Highest grade':
        watched_list = mb.get_watched_list_ordered(True, user)
        update_watched_list_ui(watched_list)
    elif order == 'Lowest grade':
        watched_list = mb.get_watched_list_ordered(False, user)
        update_watched_list_ui(watched_list)
    elif order == 'Indicated by' and user != 'Rotten':
        watched_list = mb.get_movies_title_by_name(user, users_table,
                                                   watched_table)
        update_watched_list_ui(watched_list)
    elif order == 'A-Z':
        if user != 'Rotten':
            watched_list = mb.get_movies_title_by_name(user, users_table,
                                                       watched_table)
        else:
            watched_list = global_watched_list
        watched_list = sorted(watched_list, key=str.lower)
        update_watched_list_ui(watched_list)
    elif order == 'Z-A':
        if user != 'Rotten':
            watched_list = mb.get_movies_title_by_name(user, users_table,
                                                       watched_table)
        else:
            watched_list = global_watched_list
        watched_list = sorted(watched_list, key=str.lower, reverse=True)
        update_watched_list_ui(watched_list)
    elif order == 'Date ↑':
        if user != 'Rotten':
            watched_list = mb.get_movies_title_by_name(user, users_table,
                                                       watched_table)
        else:
            watched_list = global_watched_list

        if arrow_up:
            arrow_up = False
            watched_list.reverse()
        update_watched_list_ui(watched_list)
    elif order == 'Date ↓':
        if user != 'Rotten':
            watched_list = mb.get_movies_title_by_name(user, users_table,
                                                       watched_table)
        else:
            watched_list = global_watched_list

        if not arrow_up:
            arrow_up = True
            watched_list.reverse()
        update_watched_list_ui(watched_list)


def search_watched():
    watched_updates()
    reset_feedbacks()
    ui.watchedTree.sortItems(0, 0)
    text = ui.search_watchedLineEdit.text()
    if text != '':
        watched_list = []
        for movie in global_watched_list:
            if text.lower() in movie.lower():
                watched_list.append(movie)
    else:
        watched_list = global_watched_list
    try:
        update_watched_list_ui(watched_list)
    except:
        print('Not found')
    ui.search_watchedLineEdit.setText('')


# Page 4
def update_statistics():
    rotten_list = []
    for movie in watched_table:
        if movie[utils.ROTTEN_COLUMN] is not None:
            rotten_list.append(movie[utils.ROTTEN_COLUMN])

    average_general_grades = 0
    for rotten in rotten_list:
        average_general_grades += rotten

    average_general_grades /= len(rotten_list)

    all_grades = []

    for movie in watched_table:
        for user in global_users_list:
            if movie[user] is not None:
                all_grades.append(movie[user])

    occurrence_count = Counter(all_grades)

    # AUDIENCE VARIABLES
    most_audience = 0
    most_audience_title = ''

    for movie in watched_table:
        audience = 0
        # GETTING AUDIENCE
        for user in global_users_list:
            if movie[user] is not None:
                audience += 1

        if audience > most_audience:
            most_audience = audience
            most_audience_title = movie[utils.TITLE_COLUMN]

    general_time = get_time_data(watched_table, True)

    ui.generalStatistic.setText("Rotten average:    {0}%\n"
                                "Grade most given:    {1},   {2} times\n\n"
                                "Bigger audience:    {3}\n\n"
                                "Shortest:    {4},   {5}\n"
                                "Longest:    {6},   {7}\n"
                                "Total watch time:    {8}"
                                "".format(round(average_general_grades),
                                          occurrence_count.most_common(1)[0][0],
                                          occurrence_count.most_common(1)[0][1],
                                          most_audience_title,
                                          general_time[0]['title'],
                                          general_time[0]['time'],
                                          general_time[1]['title'],
                                          general_time[1]['time'],
                                          general_time[2]))

    user = ui.userStatistics.currentText()

    if user != 'None' and user != '':
        users_movies = mb.get_movies_title_by_name(user, users_table,
                                                   watched_table)

        user_grades = []
        for movie in watched_table:
            if movie[user] is not None:
                user_grades.append(movie[user])

        if users_movies or user_grades:
            rotten_average = 0
            movies_not_null = 0
            for title in users_movies:
                rotten = mb.get_rotten(title, watched_table)
                if rotten is not None:
                    rotten_average += rotten
                    movies_not_null += 1

            if users_movies and movies_not_null != 0:
                rotten_average /= movies_not_null
                rotten_average = round(rotten_average)
                rotten_average = str(rotten_average) + '%'
            else:
                rotten_average = 'None'

            occurrence_count = Counter(user_grades)

            grades_average_other = 0
            movies_watched = 0

            # GETTING GRADES IN ALL MOVIES YOU HAVE RATED
            movies_this_user_watched = []
            for movie in watched_table:
                if movie[user] is not None:
                    movies_watched += 1
                    grades_average_other += movie[user]
                    movies_this_user_watched.append(movie)

            user_time = get_time_data(movies_this_user_watched)

            if grades_average_other:
                grades_average_other /= movies_watched
                grades_average_other = round(grades_average_other, 1)
            else:
                grades_average_other = 'None'

            grades_average_yours = 0
            movies_watched = 0
            for movie in watched_table:
                for user_movie in users_movies:
                    if movie[utils.TITLE_COLUMN] == user_movie and \
                            movie[user] is not None:
                        movies_watched += 1
                        grades_average_yours += movie[user]

            if grades_average_yours:
                grades_average_yours /= movies_watched
                grades_average_yours = round(grades_average_yours, 1)
            else:
                grades_average_yours = 'None'

            all_movies_not_null = 0
            for movie in watched_table:
                if movie[utils.ROTTEN_COLUMN] is not None:
                    all_movies_not_null += 1

            sort_average = (movies_not_null * 100) / all_movies_not_null
            sort_average = round(sort_average, 2)
            if user_grades:
                sort_average_watched = (movies_not_null * 100) / len(
                    user_grades)
                sort_average_watched = round(sort_average_watched, 2)
                sort_average_watched = str(sort_average_watched) + "%"
                average_give = occurrence_count.most_common(1)[0][0]
                average_got = occurrence_count.most_common(1)[0][1]
                shortest_movie = user_time[0]['title']
                shortest_time = user_time[0]['time']
                longest_movie = user_time[1]['title']
                longest_time = user_time[1]['time']
                watched_time = user_time[2]
            else:
                shortest_movie = 'None'
                shortest_time = 'None'
                longest_movie = 'None'
                longest_time = 'None'
                watched_time = 'None'
                average_give = 'None'
                average_got = 'None'
                sort_average_watched = 'None'

            ui.usersStaticsLabel.setText(
                "Rotten average your movies get:    {0}\n"
                "Average of grades that you give:    {1}\n"
                "Average of grades that you give to your movies:    {2}\n"
                "Grade that you most give:    {3},   {4} times\n\n"
                "Average your movies is drawn:    {5}%\n"
                "Average that you watch your movies:    {6}\n\n"
                "Shortest:    {7},   {8}\n"
                "Longest:    {9},   {10}\n"
                "Total watch time:    {11}"
                    .format(rotten_average, grades_average_other,
                            grades_average_yours, average_give, average_got,
                            sort_average, sort_average_watched, shortest_movie,
                            shortest_time, longest_movie, longest_time,
                            watched_time))
        else:
            ui.usersStaticsLabel.setText('')
    else:
        ui.usersStaticsLabel.setText('')


def get_time_data(movie_table: list, is_general=False) -> list:
    # TIME VARIABLES
    general_sec = 0
    this_movie_sec = 0
    longest_movie = {
        'title': '',
        'sec': 0,
        'time': ''
    }
    shortest_movie = {
        'title': '',
        'sec': 86400,
        'time': ''
    }
    for movie in movie_table:
        for scrap in scraping_table:
            if scrap[utils.MOVIE_ID_COLUMN] == movie[utils.MOVIE_ID_COLUMN]:
                movie_time = str(scrap[utils.TIME_COLUMN])
                if 'h' in movie_time and 'min' in movie_time:
                    movie_time = movie_time.replace("min", "").replace(" ",
                                                                       "")
                    values = movie_time.split('h')
                    this_movie_sec += int(values[0]) * 60 * 60
                    this_movie_sec += int(values[1]) * 60
                elif 'h' in movie_time and 'min' not in movie_time:
                    movie_time = movie_time.replace("h", "")
                    this_movie_sec += int(movie_time) * 60 * 60
                else:
                    movie_time = movie_time.replace("min", "")
                    this_movie_sec += int(movie_time) * 60

                add_sec = True
                if is_general:
                    if movie[utils.ROTTEN_COLUMN] is None:
                        add_sec = False
                if add_sec:
                    general_sec += this_movie_sec
                if this_movie_sec > longest_movie['sec']:
                    longest_movie['title'] = movie[utils.TITLE_COLUMN]
                    longest_movie['sec'] = this_movie_sec

                if this_movie_sec < shortest_movie['sec']:
                    shortest_movie['title'] = movie[utils.TITLE_COLUMN]
                    shortest_movie['sec'] = this_movie_sec

                this_movie_sec = 0

    # CALCULATING SHORTEST MOVIE TIME
    shortest_sec = shortest_movie['sec']
    shortest_hours = str((shortest_sec / 60) / 60)
    shortest_hours = int(shortest_hours.split('.')[0])
    shortest_minutes = str((shortest_sec / 60) % 60)
    shortest_minutes = int(shortest_minutes.split('.')[0])
    shortest_movie['time'] = '{0}h {1}min'.format(shortest_hours,
                                                  shortest_minutes)

    # CALCULATING LONGEST MOVIE TIME
    longest_sec = longest_movie['sec']
    longest_hours = str((longest_sec / 60) / 60)
    longest_hours = int(longest_hours.split('.')[0])
    longest_minutes = str((longest_sec / 60) % 60)
    longest_minutes = int(longest_minutes.split('.')[0])
    longest_movie['time'] = '{0}h {1}min'.format(longest_hours,
                                                 longest_minutes)

    # CALCULATING GENERAL WATCH TIME
    general_hours = str((general_sec / 60) / 60)
    general_hours = int(general_hours.split('.')[0])
    general_minutes = str((general_sec / 60) % 60)
    general_minutes = int(general_minutes.split('.')[0])
    general_watch_time = '{0}h {1}min'.format(general_hours,
                                              general_minutes)

    return [shortest_movie, longest_movie, general_watch_time]


app = QtWidgets.QApplication([])
ui = uic.loadUi("./style/interface.ui")
init_data()
sshFile = "./style/style.css"
with open(sshFile, "r") as fh:
    app.setStyleSheet(fh.read())
# MENU
ui.actionMovies_List.triggered.connect(show_page_1)
ui.actionDraw.triggered.connect(show_page_2)
ui.actionRating.triggered.connect(show_page_3)
ui.actionStatistics.triggered.connect(show_page_4)

# PAGE 1
ui.movieFilter.currentTextChanged.connect(filter_movie_list)
ui.filterButton.clicked.connect(filter_movie_list)
ui.addMovieButton.clicked.connect(add_movie)
ui.deleteMovieButton.clicked.connect(delete_movie)
ui.addUserButton.clicked.connect(add_user)
ui.deleteUserButton.clicked.connect(delete_user)
ui.listModeButton.clicked.connect(set_list_mode)
ui.gridModeButton.clicked.connect(set_grid_mode)

# PAGE 2
ui.addWhoWatchButton.clicked.connect(add_who_watch)
ui.deleteWhoWatchButton.clicked.connect(delete_who_watch)
ui.drawButton.clicked.connect(draw_movie)
ui.confirmButton.clicked.connect(confirm_draw)

# PAGE 3
ui.ratingButton.clicked.connect(rating)
ui.orderButton.clicked.connect(order_watched)
ui.searchWatchedButton.clicked.connect(search_watched)

# PAGE 4
ui.userStatistics.currentTextChanged.connect(update_statistics)

ui.show()
app.exec()
