import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from addEditCoffee import AddWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.updateButton.clicked.connect(self.run)
        self.addButton.clicked.connect(self.add)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM Coffee").fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", 'Название сорта', 'Степень обжарки', 'Молотый/зерна', "Описание вкуса", "Цена", "Объём упаковки"])
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
                print('s')

    def add(self):
        self.add_widget = AddWidget()
        self.add_widget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
