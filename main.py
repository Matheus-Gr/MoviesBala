import os
import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from lib import utils, movies_bala
from PyQt5 import QtGui

mb = movies_bala.MoviesBala()

show_text = False


def init_data():
    update_user_list()
    movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
    update_movie_list(movies_list)


def update_movie_list(movies_list: list):
    ui.listMovies.clear()
    for movie in movies_list:
        user_id = mb.get_user_id_by_movie_title(movie)

        user = mb.get_user_name_by_id(user_id)

        movie_id = mb.get_movie_id_by_title(movie)

        global show_text
        item_text = movie + "\n" + user
        if show_text:
            item = QListWidgetItem(item_text)
        else:
            item = QListWidgetItem()
        item.setIcon(QIcon(r"./images/posters/" + str(movie_id) + ".jpg"))
        ui.listMovies.addItem(item)


def update_watched_list():
    movie_list = mb.get_column(utils.TITLE_COLUMN, utils.WATCHED_TABLE)

    for movie in movie_list:
        user_id = mb.get_user_id_by_movie_title(movie)
        user_name = mb.get_user_name_by_id(user_id)

        item = QListWidgetItem()


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

        data = mb.get_movies_title_by_user_id(user_id)

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
    item = ui.listMovies.selectedItems()
    if item:
        movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
        item_index = ui.listMovies.row(item[0])
        movie_id = mb.get_movie_id_by_title(movies_list[item_index])

        mb.delete_movie(movie_id)
        movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
        update_movie_list(movies_list)
        update_user_list()
        try:
            os.remove("./images/posters/" + str(movie_id) + ".jpg")
        except:
            print('Was no Cover')


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
            data = mb.get_movies_title_by_user_id(user_id)

            for item in data:
                movies_list.append(item[0])

        user_index_draw = random.randrange(len(who_watching))
        user_draw = who_watching[user_index_draw]

        movies_list.clear()
        data = mb.get_movies_title_by_user_id(user_draw)
        for item in data:
            movies_list.append(item[0])

        movie_index_draw = random.randrange(len(movies_list))
        movie_draw = movies_list[movie_index_draw]

        ui.titleLabel.setText(movie_draw)
        user_name = mb.get_user_name_by_id(user_draw)
        ui.userNameLabel.setText(user_name)
        movie_id = mb.get_movie_id_by_title(movie_draw)
        poster_path = './images/posters/' + str(movie_id) + '.jpg'
        ui.posterLabel.setPixmap(QtGui.QPixmap(poster_path))
        mb.move_to_watched(movie_id)

        movies_list = mb.get_column(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
        update_movie_list(movies_list)
        update_user_list()


# Page 3

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
ui.pushButtonB.clicked.connect(update_watched_list)

ui.show()
app.exec()
