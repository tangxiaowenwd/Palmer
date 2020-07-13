# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTextEdit例子

'''

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton,QLineEdit
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300, 270)
        self.e1 = QLineEdit()
        self.textEdit2 = QTextEdit()
        self.btnPress1 = QPushButton("清空")
        self.btnPress2 = QPushButton("提交")

        layout = QVBoxLayout()
        layout.addWidget(self.e1)
        layout.addWidget(self.textEdit2)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.e1.setEchoMode(QLineEdit.Normal)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.e1.clear()
        self.textEdit2.clear()

    def btnPress2_Clicked(self):
        dd = self.e1.text()
        dd = dd.split(",")
        self.textEdit2.setPlainText(str(dd))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
