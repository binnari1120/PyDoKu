import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.first_row_tables = []
        self.second_row_tables = []
        self.third_row_tables = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyDoKu")

        v_layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_3 = QHBoxLayout()
        h_layout_4 = QHBoxLayout()

        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)
        v_layout.addLayout(h_layout_4)

        for i in range(3):
            table = QTableWidget()
            table.setColumnCount(3)
            table.setRowCount(3)
            table.horizontalHeader().hide()
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().hide()
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            table.cellChanged.connect(self.is_valid_cell_value)
            h_layout_1.addWidget(table)
            self.first_row_tables.append(table)

        for i in range(3):
            table = QTableWidget()
            table.setColumnCount(3)
            table.setRowCount(3)
            table.horizontalHeader().hide()
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().hide()
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            table.resizeColumnsToContents()
            table.resizeRowsToContents()
            h_layout_2.addWidget(table)
            self.second_row_tables.append(table)

        for i in range(3):
            table = QTableWidget()
            table.setColumnCount(3)
            table.setRowCount(3)
            table.horizontalHeader().hide()
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().hide()
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            h_layout_3.addWidget(table)
            self.third_row_tables.append(table)

        for table in self.first_row_tables:
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    table.setItem(i, j, QTableWidgetItem())
        for table in self.second_row_tables:
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    table.setItem(i, j, QTableWidgetItem())
        for table in self.third_row_tables:
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    table.setItem(i, j, QTableWidgetItem())


        reset_btn = QPushButton("Reset")
        h_layout_4.addWidget(reset_btn)

        check_btn = QPushButton("Check")
        check_btn.clicked.connect(self.is_check_btn_clicked)
        h_layout_4.addWidget(check_btn)

        self.setLayout(v_layout)
        self.show()

    def is_valid_cell_value(self, row, column):
        sender = self.sender()
        if sender.item(row, column).text().isdigit() != True or int(sender.item(row, column).text()) >= 10:
            sender.item(row, column).setText("")

    def is_check_btn_clicked(self):
        if self.are_all_cell_values_filled():
            self.check_each_table()
        else:
            print("Not all values are filled")


    def are_all_cell_values_filled(self):
        for table in self.first_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if table.item(i, j).text().isdigit() != True:
                        return False
        for table in self.second_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if table.item(i, j).text().isdigit() != False:
                        result = False
                        return result
        for table in self.third_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if table.item(i, j).text().isdigit() != False:
                        result = False
                        return result
        return True


    def check_each_table(self):
        for table in self.first_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    value = value + int(table.item(i, j).text())
            if value == sum(x for x in range(1, 10)):
                continue
            else:
                print("Individual table condition is not met!")
        for table in self.second_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    value = value + int(table.item(i, j).text())
            if value == sum(x for x in range(1, 10)):
                continue
            else:
                print("Individual table condition is not met!")
        for table in self.third_row_tables:
            value = 0
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    value = value + int(table.item(i, j).text())
            if value == sum(x for x in range(1, 10)):
                continue
            else:
                print("Individual table condition is not met!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()
    sys.exit()
