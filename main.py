import sys
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QLabel, QSpinBox, \
    QTableWidget


class SecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.spinbox_columns = QSpinBox(self)
        self.spinbox_rows = QSpinBox(self)
        self.table = QTableWidget(self)

        self.font = QtGui.QFont("ttf", 16)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("Determinant Example")


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.text = QTextEdit(self)
        self.new_page_button = QPushButton(self)
        self.link_to_documentation = QPushButton(self)
        self.label = QLabel(self)

        self.font = QtGui.QFont("ttf", 16)  # устанавливаем шрифт
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(800, 800)  # задаём размеры окна
        self.setWindowTitle("PyQt5 Example")

        self.text.setFont(self.font)

        self.new_page_button.setFont(self.font)
        self.new_page_button.setText("To table page")
        self.new_page_button.resize(150, 40)
        self.new_page_button.move(170, 10)
        self.new_page_button.clicked.connect(self.redirect_to_second_page)

        self.link_to_documentation.setFont(self.font)
        self.link_to_documentation.setText("Documentation")
        self.link_to_documentation.resize(150, 40)
        self.link_to_documentation.move(10, 10)
        self.link_to_documentation.clicked.connect(self.redirect_to_website)

        self.label.setFont(self.font)
        self.label.setText("Lable example")

    def redirect_to_second_page(self):
        self.second_page = SecondWidget()
        self.second_page.show()

    def redirect_to_website(self):
        webbrowser.open("https://doc.qt.io/qtforpython-5/")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
