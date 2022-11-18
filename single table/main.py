import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("PyDoKu")
        self.setGeometry(300, 300, 500, 500)

        h_layout = QHBoxLayout()
        h_layout_2 = QHBoxLayout()

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout_2)

        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setRowCount(9)
        self.table.horizontalHeader().hide()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.verticalHeader().hide()
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.table.cellChanged.connect(self.is_cell_changed)

        check_btn = QPushButton("Check")
        clear_btn = QPushButton("Clear")
        check_btn.clicked.connect(self.is_btn_clicked)
        clear_btn.clicked.connect(self.is_btn_clicked)
        h_layout_2.addWidget(check_btn)
        h_layout_2.addWidget(clear_btn)

        self.table.setItem(0, 0, QTableWidgetItem())
        self.table.item(0, 0).setBackground(QBrush(Qt.yellow))

        h_layout.addWidget(self.table)
        self.setLayout(v_layout)
        self.show()



    def is_btn_clicked(self):
        sender = self.sender()
        if sender.text() == "Check":
            pass
        elif sender.text() == "Clear":
            self.table.clear()

    def is_cell_changed(self, row, column):
        item = self.table.item(row, column)
        text = item.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()
    sys.exit()
