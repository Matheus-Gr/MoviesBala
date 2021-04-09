import os
import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from lib import utils, movies_bala

mb = movies_bala.MoviesBala()

show_text = False
movie_list_items = {}
watched_tree_items = {}


def init_data():
    update_user_list()
    movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
    update_movie_list(movies_list)
    watched_list = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)
    update_watched_list(watched_list)


def update_movie_list(movies_list: list):
    movie_list_items.clear()
    ui.listMovies.clear()
    user_list = mb.get_column(utils.NAME_COLUMN, utils.USERS_TABLE)
    for movie in movies_list:
        movie_row = mb.get_row_by_title(movie, utils.MOVIES_TABLE)
        movie_id = movie_row[0]
        global show_text
        item_text = "{0}\n{1}".format(movie, user_list[movie_row[1] - 1])
        if show_text:
            item = QListWidgetItem(item_text)
        else:
            item = QListWidgetItem()

            mb.download_poster(movie_id)
        try:
            item.setIcon(
                QIcon(r"./images/posters/{0}.jpg".format(movie_id)))
        except:
            print('Was no cover')
        movie_list_items[str(item)] = movie_id

        ui.listMovies.addItem(item)


def update_watched_list(watched_list: list):
    watched_tree_items.clear()
    ui.watchedTree.clear()
    user_list = mb.get_column(utils.NAME_COLUMN, utils.USERS_TABLE)
    for movie in watched_list:
        movie_row = mb.get_row_by_title(movie, utils.WATCHED_TABLE)
        movie_id = movie_row[0]
        item_movie = QTreeWidgetItem()

        mb.download_poster(movie_id)
        try:
            item_movie.setIcon(0,
                               QIcon(r"./images/posters/{0}.jpg".format(
                                   movie_id)))
        except:
            print('Was no poster')

        if movie_row[3] is not None:
            item_movie.setText(0,
                               "{0}\nRotten:{1}%".format(movie,
                                                         round(movie_row[3])))
        else:
            item_movie.setText(0, "{0}".format(movie))
        index = 4
        for user in user_list:
            if movie_row[index] is not None:
                item_grade = QTreeWidgetItem()
                item_grade.setText(0, "{0}: {1}".format(user, movie_row[index]))
                item_movie.addChild(item_grade)
            index += 1

        watched_tree_items[str(item_movie)] = movie_id

        ui.watchedTree.addTopLevelItem(item_movie)

    ui.movieCounterLabel.setText(str(len(watched_list)))


def update_user_list():
    user_list = mb.get_column(utils.NAME_COLUMN, utils.USERS_TABLE)

    # Page 1
    ui.movieFilter.clear()
    ui.movieFilter.addItem('None')
    ui.movieFilter.addItems(user_list)

    ui.userPicker.clear()
    ui.userPicker.addItem('None')
    ui.userPicker.addItems(user_list)

    ui.listUser.clear()
    ui.listUser.addItems(user_list)

    # Page 2
    user_id_list = mb.get_column(utils.USERS_ID_COLUMN, utils.MOVIES_TABLE)
    new_user_list = []
    for user in user_list:
        user_id = mb.get_user_id_by_name(user)
        if user_id in user_id_list:
            new_user_list.append(user)

    ui.whoWillWatchComboBox.clear()
    ui.whoWillWatchComboBox.addItem('None')
    ui.whoWillWatchComboBox.addItems(new_user_list)

    # Page 3
    ui.userRating.clear()
    ui.userRating.addItem('None')
    ui.userRating.addItems(user_list)

    ui.ratingColumnPicker.clear()
    ui.ratingColumnPicker.addItem('Rotten')
    ui.ratingColumnPicker.addItems(user_list)


def show_page_1():
    ui.appPages.setCurrentIndex(0)


def show_page_2():
    ui.appPages.setCurrentIndex(1)


def show_page_3():
    ui.appPages.setCurrentIndex(2)


# Page 1
def filter_movie_list():
    user = ui.movieFilter.currentText()

    if user != 'None':
        user_id = mb.get_user_id_by_name(user)

        data = mb.get_movies_title_by_user_id(user_id, utils.MOVIES_TABLE)

        movies_list = []
        for item in data:
            movies_list.append(item[0])
        update_movie_list(movies_list)
    else:
        movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
        update_movie_list(movies_list)


def add_movie():
    title = ui.movieLineEdit.text()

    if title != '':
        user = ui.userPicker.currentText()
        if user != 'None':
            ui.movieLineEdit.setText('')
            user_id = mb.get_user_id_by_name(user)

            mb.add_movie(title, user_id)
            movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
            update_movie_list(movies_list)
            update_user_list()


def delete_movie():
    item = ui.listMovies.currentItem()

    if item:
        global movie_list_items
        movie_id = movie_list_items.get(str(item))

        mb.delete_movie(movie_id)

        movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
        update_movie_list(movies_list)
        update_user_list()

        try:
            os.remove("./images/posters/" + str(movie_id) + ".jpg")
        except:
            print('Was no poster')


def add_user():
    user = ui.registerUserLineEdit.text()
    if user != '':
        ui.registerUserLineEdit.setText('')
        mb.add_user(user)
        update_user_list()


def delete_user():
    item = ui.listUser.selectedItems()
    if item:
        item_index = ui.listUser.row(item[0])
        mb.delete_user(item_index + 1)
        update_user_list()


def set_list_mode():
    ui.listMovies.setFlow(QListWidget.TopToBottom)
    ui.listMovies.setWrapping(False)
    global show_text
    show_text = True

    movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
    update_movie_list(movies_list)


def set_grid_mode():
    ui.listMovies.setFlow(QListWidget.LeftToRight)
    ui.listMovies.setWrapping(True)
    global show_text
    show_text = False

    movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
    update_movie_list(movies_list)


# Page 2
def add_who_watch():
    user = ui.whoWillWatchComboBox.currentText()

    if user != 'None':
        ui.whoWillWatchList.addItem(user)
        ui.whoWillWatchComboBox.setCurrentText('None')


def delete_who_watch():
    user = ui.whoWillWatchList.selectedItems()

    if not user:
        return
    ui.whoWillWatchList.takeItem(ui.whoWillWatchList.row(user[0]))


def draw_movie():
    if os.path.exists('./GabiGolNoVasco.txt'):
        users_count = ui.whoWillWatchList.count()

        if users_count != 0:
            who_watching = []
            for i in range(users_count):
                user = ui.whoWillWatchList.takeItem(0).text()
                user_id = mb.get_user_id_by_name(user)
                who_watching.append(user_id)

            last_user_id = mb.get_last_movie_user_id()
            if last_user_id in who_watching:
                who_watching.remove(last_user_id)

            movies_list = []
            for user_id in who_watching:
                data = mb.get_movies_title_by_user_id(user_id,
                                                      utils.MOVIES_TABLE)

                for item in data:
                    movies_list.append(item[0])

            user_index_draw = random.randrange(len(who_watching))
            user_draw = who_watching[user_index_draw]

            movies_list.clear()
            data = mb.get_movies_title_by_user_id(user_draw, utils.MOVIES_TABLE)
            for item in data:
                movies_list.append(item[0])

            movie_index_draw = random.randrange(len(movies_list))
            movie_draw = movies_list[movie_index_draw]

            ui.titleLabel.setText(movie_draw)
            user_name = mb.get_user_name_by_id(user_draw)
            ui.userNameLabel.setText(user_name)
            movie_id = mb.get_movie_id_by_title(movie_draw, utils.MOVIES_TABLE)
            poster_path = './images/posters/' + str(movie_id) + '.jpg'
            ui.posterLabel.setPixmap(QtGui.QPixmap(poster_path))
            mb.move_to_watched(movie_id)

            movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
            update_movie_list(movies_list)
            update_user_list()
            watched_list = mb.get_column(utils.TITLE_COLUMN,
                                         utils.WATCHED_TABLE)
            update_watched_list(watched_list)


# Page 3
def rating():
    item = ui.watchedTree.selectedItems()
    if item:
        move_id = watched_tree_items.get(str(item[0]))
        user_name = ui.userRating.currentText()

        grade = ui.gradeLineEdit.text()
        if grade != '' and user_name != 'None' and move_id is not None:
            mb.add_rating(user_name, move_id, float(grade))
            watched_list = mb.get_column(utils.TITLE_COLUMN,
                                         utils.WATCHED_TABLE)
            update_watched_list(watched_list)
            ui.userRating.setCurrentText('None')
            ui.gradeLineEdit.setText('')


def order_watched():
    order = ui.orderComboBox.currentText()
    user = ui.ratingColumnPicker.currentText()

    if order == 'Highest grade':
        watched_list = mb.get_watched_list_ordered(True, user)
        update_watched_list(watched_list)
    elif order == 'Lowest grade':
        watched_list = mb.get_watched_list_ordered(False, user)
        update_watched_list(watched_list)
    elif order == 'Indicated by' and user != 'Rotten':
        user_id = mb.get_user_id_by_name(user)
        data = mb.get_movies_title_by_user_id(user_id, utils.WATCHED_TABLE)
        watched_list = []
        for movie in data:
            watched_list.append(movie[0])
        update_watched_list(watched_list)
    elif order == 'A-Z':
        watched_list = mb.get_watched_list_ordered(True, user)
        update_watched_list(watched_list)
        ui.watchedTree.sortItems(0, 0)
    elif order == 'Z-A':
        watched_list = mb.get_watched_list_ordered(True, user)
        update_watched_list(watched_list)
        ui.watchedTree.sortItems(0, 1)
    elif order == 'Date ↑':
        watched_list = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)
        watched_list.reverse()
        update_watched_list(watched_list)
    elif order == 'Date ↓':
        watched_list = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)
        update_watched_list(watched_list)


def search_watched():
    ui.watchedTree.sortItems(0, 0)
    text = ui.search_watchedLineEdit.text()
    if text != '':
        watched_data = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)
        watched_list = []
        for movie in watched_data:
            if text.lower() in movie.lower():
                watched_list.append(movie)
    else:
        watched_list = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)

    try:
        update_watched_list(watched_list)
    except:
        print('Not found')
    ui.search_watchedLineEdit.setText('')


app = QtWidgets.QApplication([])
ui = uic.loadUi("./ui/moviesBala.ui")
init_data()
sshFile = "style.css"
with open(sshFile, "r") as fh:
    app.setStyleSheet(fh.read())
# MENU
ui.actionMovies_List.triggered.connect(show_page_1)
ui.actionDraw.triggered.connect(show_page_2)
ui.actionRating.triggered.connect(show_page_3)

# PAGE 1
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

# PAGE 3
ui.ratingButton.clicked.connect(rating)
ui.orderButton.clicked.connect(order_watched)
ui.searchWatchedButton.clicked.connect(search_watched)

ui.show()
app.exec()
