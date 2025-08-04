from PySide6.QtCore import *
from PySide6.QtWidgets import *
from frames import *

class log_app(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        frame = QWidget()
        layout = QVBoxLayout(frame)
        label = QLabel()
        label.setText("AAAAAAAA")
        layout.addWidget(label)
        main_layout.addWidget(frame)
