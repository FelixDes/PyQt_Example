import sys

from PyQt5.QtWidgets import QApplication

import MainWidget


def main():  # инициализация и отрисовка окна приложения
    app = QApplication(sys.argv)
    ex = MainWidget.MainWidget()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
