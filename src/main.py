from PySide6.QtWidgets import QApplication
from app import log_app

if __name__ == "__main__":
    app = QApplication()
    app.setStyleSheet("QMainWindow { background-color: #3B3331; } QPushButton { border-radius: 5px }")
    main_window = log_app()
    main_window.showMaximized()
    app.exec()