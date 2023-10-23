from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import pyqtgraph as pg

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle("лаб 1")

    def get(self):
        print("get")