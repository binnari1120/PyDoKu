from PyQt5.QtWidgets import *
import sys
import os
import numpy

example_tables = [
 5, 3, 4, 6, 7, 8, 9, 1, 2,
 6, 7, 2, 1, 9, 5, 3, 4, 8,
 1, 9, 8, 3, 4, 2, 5, 6, 7,
 8, 5, 9, 7, 6, 1, 4, 2, 3,
 4, 2, 6, 8, 5, 3, 7, 9, 1,
 7, 1, 3, 9, 2, 4, 8, 5, 6,
 9, 6, 1, 5, 3, 7, 2, 8, 4,
 2, 8, 7, 4, 1, 9, 6, 3, 5,
 3, 4, 5, 2, 8, 6, 1, 7, 9
]

base_table = numpy.zeros(81)
# self.base_table = [
#  5, 3, 4, 6, 7, 8, 9, 1, 2,
#  6, 7, 2, 1, 9, 5, 3, 4, 8,
#  1, 9, 8, 3, 4, 2, 5, 6, 7,
#  8, 5, 9, 7, 6, 1, 4, 2, 3,
#  4, 2, 6, 8, 5, 3, 7, 9, 1,
#  7, 1, 3, 9, 2, 4, 8, 5, 6,
#  9, 6, 1, 5, 3, 7, 2, 8, 4,
#  2, 8, 7, 4, 1, 9, 6, 3, 5,
#  3, 4, 5, 2, 8, 6, 1, 7, 9
# ]
base_table = numpy.array(base_table)



class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.base_table = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyDoKu")
        self.setGeometry(300, 300, 800, 800)

        self.init_tables()

        main_layout = QVBoxLayout()

        row_1_table_layout = QHBoxLayout()
        row_1_table_layout.addWidget(self.tables[0])
        row_1_table_layout.addWidget(self.tables[1])
        row_1_table_layout.addWidget(self.tables[2])

        row_2_table_layout = QHBoxLayout()
        row_2_table_layout.addWidget(self.tables[3])
        row_2_table_layout.addWidget(self.tables[4])
        row_2_table_layout.addWidget(self.tables[5])

        row_3_table_layout = QHBoxLayout()
        row_3_table_layout.addWidget(self.tables[6])
        row_3_table_layout.addWidget(self.tables[7])
        row_3_table_layout.addWidget(self.tables[8])

        main_layout.addLayout(row_1_table_layout)
        main_layout.addLayout(row_2_table_layout)
        main_layout.addLayout(row_3_table_layout)

        button_layout = QHBoxLayout()
        load_btn = QPushButton("Load")
        clear_btn = QPushButton("Clear")
        check_btn = QPushButton("Check")
        load_btn.clicked.connect(self.is_load_btn_clicked)
        clear_btn.clicked.connect(self.is_clear_btn_clicked)
        check_btn.clicked.connect(self.is_check_btn_clicked)
        button_layout.addWidget(load_btn)
        button_layout.addWidget(clear_btn)
        button_layout.addWidget(check_btn)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.show()

    def init_tables(self):
        table_11 = QTableWidget()
        table_12 = QTableWidget()
        table_13 = QTableWidget()
        table_21 = QTableWidget()
        table_22 = QTableWidget()
        table_23 = QTableWidget()
        table_31 = QTableWidget()
        table_32 = QTableWidget()
        table_33 = QTableWidget()

        self.tables = []
        self.tables.append(table_11)
        self.tables.append(table_12)
        self.tables.append(table_13)
        self.tables.append(table_21)
        self.tables.append(table_22)
        self.tables.append(table_23)
        self.tables.append(table_31)
        self.tables.append(table_32)
        self.tables.append(table_33)

        for table in self.tables:
            table.setRowCount(3)
            table.setColumnCount(3)
            table.horizontalHeader().hide()
            table.verticalHeader().hide()
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.cellChanged.connect(self.is_valid_cell_value)

    def is_valid_cell_value(self, row, column):
        sender = self.sender()
        if sender.item(row, column).text().isdigit() != True or int(sender.item(row, column).text()) >= 10:
            sender.item(row, column).setText("")

    def is_clear_btn_clicked(self):
        for table in self.tables:
            table.clear()


    def is_load_btn_clicked(self):
        self.tables[0].setItem(0, 0, QTableWidgetItem("5"))
        self.tables[0].setItem(0, 1, QTableWidgetItem("3"))
        self.tables[0].setItem(0, 2, QTableWidgetItem("4"))
        self.tables[0].setItem(1, 0, QTableWidgetItem("6"))
        self.tables[0].setItem(1, 1, QTableWidgetItem("7"))
        self.tables[0].setItem(1, 2, QTableWidgetItem("2"))
        self.tables[0].setItem(2, 0, QTableWidgetItem("1"))
        self.tables[0].setItem(2, 1, QTableWidgetItem("9"))
        self.tables[0].setItem(2, 2, QTableWidgetItem("8"))

        self.tables[1].setItem(0, 0, QTableWidgetItem("6"))
        self.tables[1].setItem(0, 1, QTableWidgetItem("7"))
        self.tables[1].setItem(0, 2, QTableWidgetItem("8"))
        self.tables[1].setItem(1, 0, QTableWidgetItem("1"))
        self.tables[1].setItem(1, 1, QTableWidgetItem("9"))
        self.tables[1].setItem(1, 2, QTableWidgetItem("5"))
        self.tables[1].setItem(2, 0, QTableWidgetItem("3"))
        self.tables[1].setItem(2, 1, QTableWidgetItem("4"))
        self.tables[1].setItem(2, 2, QTableWidgetItem("2"))

        self.tables[2].setItem(0, 0, QTableWidgetItem("9"))
        self.tables[2].setItem(0, 1, QTableWidgetItem("1"))
        self.tables[2].setItem(0, 2, QTableWidgetItem("2"))
        self.tables[2].setItem(1, 0, QTableWidgetItem("3"))
        self.tables[2].setItem(1, 1, QTableWidgetItem("4"))
        self.tables[2].setItem(1, 2, QTableWidgetItem("8"))
        self.tables[2].setItem(2, 0, QTableWidgetItem("5"))
        self.tables[2].setItem(2, 1, QTableWidgetItem("6"))
        self.tables[2].setItem(2, 2, QTableWidgetItem("7"))

        self.tables[3].setItem(0, 0, QTableWidgetItem("8"))
        self.tables[3].setItem(0, 1, QTableWidgetItem("5"))
        self.tables[3].setItem(0, 2, QTableWidgetItem("9"))
        self.tables[3].setItem(1, 0, QTableWidgetItem("4"))
        self.tables[3].setItem(1, 1, QTableWidgetItem("2"))
        self.tables[3].setItem(1, 2, QTableWidgetItem("6"))
        self.tables[3].setItem(2, 0, QTableWidgetItem("7"))
        self.tables[3].setItem(2, 1, QTableWidgetItem("1"))
        self.tables[3].setItem(2, 2, QTableWidgetItem("3"))

        self.tables[4].setItem(0, 0, QTableWidgetItem("7"))
        self.tables[4].setItem(0, 1, QTableWidgetItem("6"))
        self.tables[4].setItem(0, 2, QTableWidgetItem("1"))
        self.tables[4].setItem(1, 0, QTableWidgetItem("8"))
        self.tables[4].setItem(1, 1, QTableWidgetItem("5"))
        self.tables[4].setItem(1, 2, QTableWidgetItem("3"))
        self.tables[4].setItem(2, 0, QTableWidgetItem("9"))
        self.tables[4].setItem(2, 1, QTableWidgetItem("2"))
        self.tables[4].setItem(2, 2, QTableWidgetItem("4"))

        self.tables[5].setItem(0, 0, QTableWidgetItem("4"))
        self.tables[5].setItem(0, 1, QTableWidgetItem("2"))
        self.tables[5].setItem(0, 2, QTableWidgetItem("3"))
        self.tables[5].setItem(1, 0, QTableWidgetItem("7"))
        self.tables[5].setItem(1, 1, QTableWidgetItem("9"))
        self.tables[5].setItem(1, 2, QTableWidgetItem("1"))
        self.tables[5].setItem(2, 0, QTableWidgetItem("8"))
        self.tables[5].setItem(2, 1, QTableWidgetItem("5"))
        self.tables[5].setItem(2, 2, QTableWidgetItem("6"))

        self.tables[6].setItem(0, 0, QTableWidgetItem("9"))
        self.tables[6].setItem(0, 1, QTableWidgetItem("6"))
        self.tables[6].setItem(0, 2, QTableWidgetItem("1"))
        self.tables[6].setItem(1, 0, QTableWidgetItem("2"))
        self.tables[6].setItem(1, 1, QTableWidgetItem("8"))
        self.tables[6].setItem(1, 2, QTableWidgetItem("7"))
        self.tables[6].setItem(2, 0, QTableWidgetItem("3"))
        self.tables[6].setItem(2, 1, QTableWidgetItem("4"))
        self.tables[6].setItem(2, 2, QTableWidgetItem("5"))

        self.tables[7].setItem(0, 0, QTableWidgetItem("5"))
        self.tables[7].setItem(0, 1, QTableWidgetItem("3"))
        self.tables[7].setItem(0, 2, QTableWidgetItem("7"))
        self.tables[7].setItem(1, 0, QTableWidgetItem("4"))
        self.tables[7].setItem(1, 1, QTableWidgetItem("1"))
        self.tables[7].setItem(1, 2, QTableWidgetItem("9"))
        self.tables[7].setItem(2, 0, QTableWidgetItem("2"))
        self.tables[7].setItem(2, 1, QTableWidgetItem("8"))
        self.tables[7].setItem(2, 2, QTableWidgetItem("6"))

        self.tables[8].setItem(0, 0, QTableWidgetItem("2"))
        self.tables[8].setItem(0, 1, QTableWidgetItem("8"))
        self.tables[8].setItem(0, 2, QTableWidgetItem("4"))
        self.tables[8].setItem(1, 0, QTableWidgetItem("6"))
        self.tables[8].setItem(1, 1, QTableWidgetItem("3"))
        self.tables[8].setItem(1, 2, QTableWidgetItem("5"))
        self.tables[8].setItem(2, 0, QTableWidgetItem("1"))
        self.tables[8].setItem(2, 1, QTableWidgetItem("7"))
        self.tables[8].setItem(2, 2, QTableWidgetItem("9"))


    def is_check_btn_clicked(self):
        if self.are_all_cell_values_filled() == True:
            self.save_tables_in_base_table()

            if self.is_individual_table_condition_valid() == True and self.is_inter_table_condition_valid() == True and self.is_whole_table_condition_valid() == True:
                print("Mission Sucess!")
            else:
                print("Wrong combination!")


    def are_all_cell_values_filled(self):
        for table in self.tables:
            for i in range(3):
                for j in range(3):
                    if table.item(i, j) == None:
                        print("Not all cell values are filled!")
                        return False
        return True


    def save_tables_in_base_table(self):
        values = []
        for table in self.tables:
            for i in range(3):
                for j in range(3):
                    value = int(table.item(i, j).text())
                    values.append(value)
        self.base_table = values.copy()
        print(self.base_table)


    def is_individual_table_condition_valid(self):
        for i in range(9):
            sum_ = sum(self.base_table[9*i:9*(i+1)])
            if sum_ != 45:
                print("Individual condition is not valid!")
                return False
        return True


    def is_inter_table_condition_valid(self):
        if sum(self.base_table[0:3]) + sum(self.base_table[9:12]) + sum(self.base_table[18:21]) != 45 or \
            sum(self.base_table[3:6]) + sum(self.base_table[12:15]) + sum(self.base_table[21:24]) != 45 or \
            sum(self.base_table[6:9]) + sum(self.base_table[15:18]) + sum(self.base_table[24:27]) != 45 or \
            sum(self.base_table[27:30]) + sum(self.base_table[36:39]) + sum(self.base_table[45:48]) != 45 or \
            sum(self.base_table[30:33]) + sum(self.base_table[39:42]) + sum(self.base_table[48:51]) != 45 or \
            sum(self.base_table[33:36]) + sum(self.base_table[42:45]) + sum(self.base_table[51:54]) != 45 or \
            sum(self.base_table[54:57]) + sum(self.base_table[63:66]) + sum(self.base_table[72:75]) != 45 or \
            sum(self.base_table[57:60]) + sum(self.base_table[66:69]) + sum(self.base_table[75:78]) != 45 or \
            sum(self.base_table[60:63]) + sum(self.base_table[69:72]) + sum(self.base_table[78:81]) != 45:
            print("Inter-table condition is not valid!")
            return False

        if self.base_table[0] + self.base_table[3] + self.base_table[6] + self.base_table[27] + self.base_table[30] + self.base_table[33] + self.base_table[54] + self.base_table[57] + self.base_table[60] != 45 or \
            self.base_table[1] + self.base_table[4] + self.base_table[7] + self.base_table[28] + self.base_table[31] + self.base_table[34] + self.base_table[55] + self.base_table[58] + self.base_table[61] != 45 or \
            self.base_table[2] + self.base_table[5] + self.base_table[8] + self.base_table[29] + self.base_table[32] + self.base_table[35] + self.base_table[56] + self.base_table[59] + self.base_table[62] != 45 or \
            self.base_table[9] + self.base_table[12] + self.base_table[15] + self.base_table[36] + self.base_table[39] + self.base_table[42] + self.base_table[63] + self.base_table[66] + self.base_table[69] != 45 or \
            self.base_table[10] + self.base_table[13] + self.base_table[16] + self.base_table[37] + self.base_table[40] + self.base_table[43] + self.base_table[64] + self.base_table[67] + self.base_table[70] != 45 or \
            self.base_table[11] + self.base_table[14] + self.base_table[17] + self.base_table[38] + self.base_table[41] + self.base_table[44] + self.base_table[65] + self.base_table[68] + self.base_table[71] != 45 or \
            self.base_table[18] + self.base_table[21] + self.base_table[24] + self.base_table[45] + self.base_table[48] + self.base_table[51] + self.base_table[72] + self.base_table[75] + self.base_table[78] != 45 or \
            self.base_table[19] + self.base_table[22] + self.base_table[25] + self.base_table[46] + self.base_table[49] + self.base_table[52] + self.base_table[73] + self.base_table[76] + self.base_table[79] != 45 or \
            self.base_table[20] + self.base_table[23] + self.base_table[26] + self.base_table[47] + self.base_table[50] + self.base_table[53] + self.base_table[74] + self.base_table[77] + self.base_table[80] != 45:
            print("Inter-table condition is not valid!")
            return False

        # 00 01 02  09 10 11  18 19 20
        # 03 04 05  12 13 14  21 22 23
        # 06 07 08  15 16 17  24 25 26
        #
        # 27 28 29  36 37 38  45 46 47
        # 30 31 32  39 40 41  48 49 50
        # 33 34 35  42 43 44  51 52 53
        #
        # 54 55 56  63 64 65  72 73 74
        # 57 58 59  66 67 68  75 76 77
        # 60 61 62  69 70 71  78 79 80
        return True



    def is_whole_table_condition_valid(self):
        sum_ = sum(self.base_table)
        if sum_ != 405:
            print("Whole table condition is not valid!")
            return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec()
    sys.exit()
