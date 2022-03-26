import sys
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QHBoxLayout

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() - 2 * PADDING, 400)

INPUT_MODES = ["Матрицы", "Уравнения"]
RUN_MODES = ["Обратная матрица", "Гаусс", "Крамор"]


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.input_mode_label = QLabel(self)
        self.link_to_documentation = QPushButton(self)
        self.link_to_github = QPushButton(self)
        self.mode_setter = QComboBox(self)
        self.run_mode_setter = QComboBox(self)
        self.run_button = QPushButton(self)
        # self.input_frame = QtGui.QFrame()

        self.font = QtGui.QFont("ttf", 16)  # устанавливаем шрифт
        self.init_ui()

    # инициализация графических компонентов
    def init_ui(self):
        self.setFixedSize(WINDOW_SIZE)  # задаём размеры окна
        self.setWindowTitle("PyQt5 Example")  # задаём название окна

        # Кнопка с документацией
        self.link_to_documentation.setFont(self.font)
        self.link_to_documentation.setText("Документация")
        self.link_to_documentation.resize(ELEMENT_SIZE)
        self.link_to_documentation.move(PADDING, WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())
        self.link_to_documentation.clicked.connect(lambda: self.redirect_to_website("https://doc.qt.io/qtforpython-5/"))

        # Кнопка с гитхабом
        self.link_to_github.setFont(self.font)
        self.link_to_github.setText("Github")
        self.link_to_github.resize(ELEMENT_SIZE)
        self.link_to_github.move(2 * PADDING + ELEMENT_SIZE.width(),
                                 WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())
        self.link_to_github.clicked.connect(
            lambda: self.redirect_to_website("https://github.com/FelixDes/PyQt_Example"))

        # Лейбл под метод ввода
        self.input_mode_label.setFont(self.font)
        self.input_mode_label.setText("Метод ввода:")
        self.input_mode_label.resize(ELEMENT_SIZE)
        self.input_mode_label.move(PADDING, PADDING)

        # Выбор метода ввода
        self.mode_setter.setFont(self.font)
        self.mode_setter.addItems(INPUT_MODES)
        self.mode_setter.activated[str].connect(self.onChecked)
        self.mode_setter.resize(ELEMENT_SIZE)
        self.mode_setter.move(2 * PADDING + ELEMENT_SIZE.width(), PADDING)

        # Выбор метода расчёта
        self.run_mode_setter.setFont(self.font)
        self.run_mode_setter.addItems(RUN_MODES)
        self.run_mode_setter.activated[str].connect(self.onRun)
        self.run_mode_setter.resize(LONG_ELEMENT_SIZE)
        self.run_mode_setter.move(PADDING, 3 * PADDING + INPUT_CONTAINER_SIZE.height())

        # Запуск расчёта
        self.run_button.setFont(self.font)
        self.run_button.setText("Решить")
        self.run_button.resize(ELEMENT_SIZE)
        self.run_button.move(2 * PADDING + LONG_ELEMENT_SIZE.width(), 3 * PADDING + INPUT_CONTAINER_SIZE.height())
        # self.run_button.clicked.connect(
        #     lambda: self.redirect_to_website("https://github.com/FelixDes/PyQt_Example"))

    def redirect_to_website(self, url):
        webbrowser.open(url)

    def onChecked(self, mode):
        pass

    def onRun(self, mode):
        pass

    # def setFill


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
