import sys
import webbrowser
from enum import Enum

from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QStyledItemDelegate, QLineEdit

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() // 2 - 2 * PADDING, 400)

RUN_MODES = ["Обратная матрица", "Гаусс", "Крамор"]


def main():
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())


# класс для выполнения математических операций
class MatrixSolver:
    left_values = list(list())
    right_values = list()

    def __init__(self, left_values, right_values):
        self.left_values = left_values
        self.right_values = right_values

    def solve_for_opposite_matrix_method(self):
        pass

    def solve_for_gauss_method(self):
        pass

    def solve_for_kramor_method(self):
        pass


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
        # инициализация графических элементов
        self.number_of_cols_label = QLabel(self)
        self.link_to_documentation = QPushButton(self)
        self.link_to_github = QPushButton(self)
        self.number_of_cols_spinner = QSpinBox(self)
        self.run_mode_setter = QComboBox(self)
        self.run_button = QPushButton(self)
        self.table_left_values = QTableWidget(self)
        self.table_right_values = QTableWidget(self)

        self.init_ui()

        self.set_listeners()
        self.set_only_numeric_input_to_tables()

    # настройка графических элементов
    def init_ui(self):
        self.setFixedSize(WINDOW_SIZE)  # задаём размеры окна
        self.setWindowTitle("PyQt5 Example")  # задаём название окна

        # Лейбл под кол-во строк/столбцов
        self.number_of_cols_label.setFont(self.font)
        self.number_of_cols_label.setText("Размер:")
        self.number_of_cols_label.resize(ELEMENT_SIZE)
        self.number_of_cols_label.move(PADDING, PADDING)

        # Спиннер под установки размеров
        self.number_of_cols_spinner.setFont(self.font)
        self.number_of_cols_spinner.resize(ELEMENT_SIZE)
        self.number_of_cols_spinner.move(2 * PADDING + ELEMENT_SIZE.width(), PADDING)

        # Таблица под правые значения
        self.table_left_values.resize(INPUT_CONTAINER_SIZE)
        self.table_left_values.move(PADDING, 2 * PADDING + ELEMENT_SIZE.height())

        # Таблица под левые значения
        self.table_right_values.resize(INPUT_CONTAINER_SIZE)
        self.table_right_values.move(2 * PADDING + INPUT_CONTAINER_SIZE.width(), 2 * PADDING + ELEMENT_SIZE.height())

        # Выбор метода расчёта
        self.run_mode_setter.setFont(self.font)
        self.run_mode_setter.addItems(RUN_MODES)
        self.run_mode_setter.resize(LONG_ELEMENT_SIZE)
        self.run_mode_setter.move(PADDING, 3 * PADDING + ELEMENT_SIZE.height() + INPUT_CONTAINER_SIZE.height())

        # Запуск расчёта
        self.run_button.setFont(self.font)
        self.run_button.setText("Решить")
        self.run_button.resize(ELEMENT_SIZE)
        self.run_button.move(2 * PADDING + LONG_ELEMENT_SIZE.width(),
                             3 * PADDING + ELEMENT_SIZE.height() + INPUT_CONTAINER_SIZE.height())

        # Кнопка - ссылка на документацию
        self.link_to_documentation.setFont(self.font)
        self.link_to_documentation.setText("Документация")
        self.link_to_documentation.resize(ELEMENT_SIZE)
        self.link_to_documentation.move(PADDING, WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())

        # Кнопка - ссылка на github
        self.link_to_github.setFont(self.font)
        self.link_to_github.setText("Github")
        self.link_to_github.resize(ELEMENT_SIZE)
        self.link_to_github.move(2 * PADDING + ELEMENT_SIZE.width(),
                                 WINDOW_SIZE.height() - PADDING - ELEMENT_SIZE.height())

    def set_only_numeric_input_to_tables(self):
        delegate1 = NumericDelegate(self.table_left_values)
        self.table_left_values.setItemDelegate(delegate1)
        delegate2 = NumericDelegate(self.table_right_values)
        self.table_right_values.setItemDelegate(delegate2)

    def set_listeners(self):
        self.number_of_cols_spinner.valueChanged.connect(lambda x: self.change_number_of_cols(x))
        self.run_button.clicked.connect(self.on_run)
        self.link_to_documentation.clicked.connect(lambda: self.redirect_to_website("https://doc.qt.io/qtforpython-5/"))
        self.link_to_github.clicked.connect(
            lambda: self.redirect_to_website("https://github.com/FelixDes/PyQt_Example"))

    def redirect_to_website(self, url):
        webbrowser.open(url)

    def change_number_of_cols(self, number):
        self.table_left_values.setRowCount(number)
        self.table_left_values.setColumnCount(number)
        self.table_right_values.setRowCount(number)
        self.table_right_values.setColumnCount(1)

    def on_run(self):
        left_values = self.get_element_list_from_table(self.table_left_values)
        right_values = self.get_element_list_from_table(self.table_right_values)
        m_solver = MatrixSolver()
        # result_values = m_solver.

    def get_element_list_from_table(self, table):
        pass


if __name__ == '__main__':
    main()
