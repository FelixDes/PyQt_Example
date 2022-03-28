import sys
import webbrowser
from enum import Enum

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QHBoxLayout, QFrame, QScrollArea, QVBoxLayout, QStyledItemDelegate, QLineEdit

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() - 2 * PADDING, 400)

RUN_MODES = ["Обратная матрица", "Гаусс", "Крамор"]


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor


class MainWidget(QWidget):
    font = QtGui.QFont("ttf", 16)  # устанавливаем шрифт

    def __init__(self):
        super().__init__()
        self.number_of_cols_label = QLabel(self)
        self.link_to_documentation = QPushButton(self)
        self.link_to_github = QPushButton(self)
        self.number_of_cols_spinner = QSpinBox(self)
        self.run_mode_setter = QComboBox(self)
        self.run_button = QPushButton(self)
        self.input_table = QTableWidget(self)

        self.number_of_cols = 0

        self.init_ui()
        self.set_listeners()
        self.set_only_numeric_input_to_table()

    def set_only_numeric_input_to_table(self):
        delegate = NumericDelegate(self.input_table)
        self.input_table.setItemDelegate(delegate)

    def set_listeners(self):
        self.number_of_cols_spinner.valueChanged.connect(lambda x: self.change_number_of_cols(x))
        self.link_to_documentation.clicked.connect(lambda: self.redirect_to_website("https://doc.qt.io/qtforpython-5/"))
        self.link_to_github.clicked.connect(
            lambda: self.redirect_to_website("https://github.com/FelixDes/PyQt_Example"))

    # инициализация графических компонентов
    def init_ui(self):
        self.setFixedSize(WINDOW_SIZE)  # задаём размеры окна
        self.setWindowTitle("PyQt5 Example")  # задаём название окна

        # Лейбл под кол-во строк/столбцов
        self.number_of_cols_label.setFont(self.font)
        self.number_of_cols_label.setText("Строки:")
        self.number_of_cols_label.resize(ELEMENT_SIZE)
        self.number_of_cols_label.move(PADDING, PADDING)

        self.number_of_cols_spinner.setFont(self.font)
        self.number_of_cols_spinner.resize(ELEMENT_SIZE)
        self.number_of_cols_spinner.move(2 * PADDING + ELEMENT_SIZE.width(), PADDING)

        self.input_table.resize(INPUT_CONTAINER_SIZE)
        self.input_table.move(PADDING, 2 * PADDING + ELEMENT_SIZE.height())

        # Выбор метода расчёта
        self.run_mode_setter.setFont(self.font)
        self.run_mode_setter.addItems(RUN_MODES)
        # self.run_mode_setter.activated[str].connect(self.onRun)
        self.run_mode_setter.resize(LONG_ELEMENT_SIZE)
        self.run_mode_setter.move(PADDING, 3 * PADDING + ELEMENT_SIZE.height() + INPUT_CONTAINER_SIZE.height())

        # Запуск расчёта
        self.run_button.setFont(self.font)
        self.run_button.setText("Решить")
        self.run_button.resize(ELEMENT_SIZE)
        self.run_button.move(2 * PADDING + LONG_ELEMENT_SIZE.width(),
                             3 * PADDING + ELEMENT_SIZE.height() + INPUT_CONTAINER_SIZE.height())
        self.run_button.clicked.connect(self.run)

        # Кнопка с документацией
        self.link_to_documentation.setFont(self.font)
        self.link_to_documentation.setText("Документация")
        self.link_to_documentation.resize(ELEMENT_SIZE)
        self.link_to_documentation.move(PADDING, WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())

        # Кнопка с гитхабом
        self.link_to_github.setFont(self.font)
        self.link_to_github.setText("Github")
        self.link_to_github.resize(ELEMENT_SIZE)
        self.link_to_github.move(2 * PADDING + ELEMENT_SIZE.width(),
                                 WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())

    def redirect_to_website(self, url):
        webbrowser.open(url)

    def change_number_of_cols(self, number):
        self.input_table.setRowCount(number)
        self.input_table.setColumnCount(number)

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
