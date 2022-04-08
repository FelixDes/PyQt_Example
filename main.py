import sys

from PyQt5.QtWidgets import QApplication

from MainWidget import MainWidget


def main():  # инициализация и отрисовка окна приложения
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
