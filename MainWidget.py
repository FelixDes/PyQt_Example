from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSpinBox, \
    QTableWidget, QComboBox, QStyledItemDelegate, QLineEdit, QTableWidgetItem

import webbrowser

import MatrixSolver

PADDING = 10

ELEMENT_SIZE = QSize(150, 30)
LONG_ELEMENT_SIZE = QSize(210, 30)
WINDOW_SIZE = QSize(800, 800)
INPUT_CONTAINER_SIZE = QSize(WINDOW_SIZE.width() // 2 - 2 * PADDING, 325)

RUN_MODES = ["Обратная матрица", "Крамер", "Гаусс"]


class MainWidget(QWidget):  # класс виджета (view + controller)
    font = QtGui.QFont("ttf", 16)  # устанавливаем шрифт

    def __init__(self):  # конструктор
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
        self.table_result = QTableWidget(self)

        self.set_ui_and_listeners()

    def set_ui_and_listeners(self):
        self.init_ui()
        self.set_listeners()

        self.set_only_read_mode_to_table(self.table_result)
        self.set_only_numeric_input_to_tables()

    # настройка графических элементов
    def init_ui(self):
        self.setFixedSize(WINDOW_SIZE)  # задаём размеры окна
        self.setWindowTitle("PyQt5 Matrix Example")  # задаём название окна

        # Поле под кол-во строк/столбцов
        self.number_of_cols_label.setFont(self.font)
        self.number_of_cols_label.setText("Размер:")
        self.number_of_cols_label.resize(ELEMENT_SIZE)  # изменить размер
        self.number_of_cols_label.move(PADDING, PADDING)  # переместить на экране

        # Спиннер под установки размеров
        self.number_of_cols_spinner.setFont(self.font)
        self.number_of_cols_spinner.resize(ELEMENT_SIZE)
        self.number_of_cols_spinner.move(2 * PADDING + ELEMENT_SIZE.width(), PADDING)
        self.number_of_cols_spinner.setMinimum(2)

        # Таблица под правые значения
        self.table_left_values.resize(INPUT_CONTAINER_SIZE)
        self.table_left_values.move(PADDING, 2 * PADDING + ELEMENT_SIZE.height())

        # Таблица под левые значения
        self.table_right_values.resize(INPUT_CONTAINER_SIZE)
        self.table_right_values.move(2 * PADDING + INPUT_CONTAINER_SIZE.width(), 2 * PADDING + ELEMENT_SIZE.height())

        # Таблица под ответ
        self.table_result.resize(INPUT_CONTAINER_SIZE)
        self.table_result.move(PADDING,
                               4 * PADDING + ELEMENT_SIZE.height() + INPUT_CONTAINER_SIZE.height() + LONG_ELEMENT_SIZE.height())

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

    def set_only_numeric_input_to_tables(self):  # Запрет на ввод не цифр
        self.delegate_numeric_to_table(self.table_left_values)
        self.delegate_numeric_to_table(self.table_right_values)

    def delegate_numeric_to_table(self, table):
        delegate = NumericDelegate(table)
        table.setItemDelegate(delegate)

    # запрет на изменение таблицы с результатом
    def set_only_read_mode_to_table(self, table):
        table.setEditTriggers(QTableWidget.NoEditTriggers)

    def set_listeners(self):
        # лямбда функция используется для того, чтобы привязать другую функцию на нажатие
        self.number_of_cols_spinner.valueChanged.connect(lambda x: self.set_size_of_all_tables(x))
        self.run_button.clicked.connect(self.on_run)
        self.link_to_documentation.clicked.connect(lambda: self.redirect_to_website("https://doc.qt.io/qtforpython-5/"))
        self.link_to_github.clicked.connect(
            lambda: self.redirect_to_website("https://github.com/FelixDes/PyQt_Example"))

    def redirect_to_website(self, url):
        webbrowser.open(url)

    def set_size_of_all_tables(self, number):  # установить размеры всех таблиц
        self.set_sizes_of_table(self.table_left_values, number, number)
        self.set_sizes_of_table(self.table_right_values, number, 1)
        self.set_sizes_of_table(self.table_result, number, 1)

    def set_sizes_of_table(self, table, row, column):  # установить размер конкретной таблицы
        table.setRowCount(row)
        table.setColumnCount(column)

    # Запустить решение с выбранным методом
    def on_run(self):
        self.fill_nulls_cells_for_zeroes()  # заполняем нулями пустые ячейки

        # получаем данные из таблиц
        left_values = self.get_element_list_from_table(self.table_left_values)
        right_values = self.get_element_list_from_table(self.table_right_values)

        self.table_result.clear()

        result_values = list()

        m_solver = MatrixSolver.MatrixSolver(left_values, right_values)

        match self.run_mode_setter.currentIndex():  # (Python с версии 3.9 поддерживает switch-case блоки)
            case 0:
                result_values = m_solver.solve_for_opposite_matrix_method()
            case 1:
                result_values = m_solver.solve_for_kramer_method()
            case 2:
                result_values = m_solver.solve_for_gauss_method()

        self.put_elements_to_table_from_list(self.table_result, result_values)

    def fill_nulls_cells_for_zeroes(self):
        self.fill_empty_cells_with_zeroes(self.table_left_values)
        self.fill_empty_cells_with_zeroes(self.table_right_values)

    def fill_empty_cells_with_zeroes(self, table):  # пустые ячейки заполяем нулями
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                if not (table.item(i, j) is not None) or not (table.item(i, j).text() != ''):
                    table.setItem(i, j, QTableWidgetItem("0"))

    # Получить данные из QTableWidget
    def get_element_list_from_table(self, table):
        lst = list()
        for i in range(table.rowCount()):
            sub_lst = list()
            for j in range(table.columnCount()):
                sub_lst.append(float(table.item(i, j).text()))
            lst.append(sub_lst)
        return lst

    # Записать данные в QTableWidget
    def put_elements_to_table_from_list(self, table, lst):
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                table.setItem(i, j, QTableWidgetItem("{:10.4f}".format(lst[i][j])))


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("([+-]?\d+(?:\.\d+)?)")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor
