import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLineEdit


class AddWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.addButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()
        some = QLineEdit()
        id = self.idTextBox.text()
        name = self.lineEdit_2.text()
        roasting = self.lineEdit_3.text()
        groundgraint = self.lineEdit_4.text()
        taste = self.lineEdit_5.text()
        volume = self.lineEdit_6.text()
        cost = self.lineEdit_7.text()

        data = cur.execute(f'SELECT * FROM Coffee WHERE ID = {id}').fetchall()
        if len(data) == 0:
            cur.execute(
                f'INSERT INTO Coffee ([ID], [название сорта], [степень обжарки], [молотый/зерна], [описание вкуса], [цена], [объём упаковки]) VALUES ({id}, "{name}", "{roasting}", "{groundgraint}", "{taste}", "{cost}", "{volume}")')
        else:
            cur.execute(
                f'UPDATE Coffee SET [название сорта] = "{name}", [степень обжарки] = "{roasting}", [молотый/зерна] = "{groundgraint}", [описание вкуса] = "{taste}", [цена] = "{cost}", [объём упаковки] = "{volume}" WHERE ID = {id}')
        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddWidget()
    ex.show()
    sys.exit(app.exec())
