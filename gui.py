from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import server
import threading
import time


class Label:
    static_label = QtWidgets
class text:
    static_text=""
class scroll:
    static_scroll = QScrollArea
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 500)
    win.setWindowTitle("Server")
    Label.static_label = QtWidgets.QLabel(win)
    win.show()
    sys.exit(app.exec_())
    scroll.static_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    scroll.static_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.static_scroll.setWidgetResizable(True)
    scroll.static_scroll.setWidget(win)

def bring_message():
    for message in server.all_messages:
        text.static_text += message +"\n"
        server.all_messages.remove(message)
    return(text.static_text)


def show_message():
    while True:
        Label.static_label.setText(str(bring_message()))
        Label.static_label.adjustSize()
def start_all():
    gui_code = threading.Thread(target=window, args=())
    gui_code.start()
    server_code = threading.Thread(target=(server.start), args=())
    server_code.start()
    time.sleep(1)
    show_messages = threading.Thread(target=show_message)
    show_messages.start()
start_all()