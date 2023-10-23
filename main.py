import sys
from PyQt6.QtWidgets import *
from View.mainView import Window


app = QApplication(sys.argv)
app.setStyle('fusion')
window = Window()
window.show()
sys.exit(app.exec())