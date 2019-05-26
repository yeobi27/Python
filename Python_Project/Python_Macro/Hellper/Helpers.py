import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.open_btn = QPushButton('Open Image')
        self.label = []
        self.x_le = QLineEdit()
        self.y_le = QLineEdit()
        self.n_le = QLineEdit()
        self.t_le = QLineEdit()
        self.click_btn = QPushButton('Click')
        self.fname = []
        self.hbox_label = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):

        hbox_xy = QHBoxLayout()
        hbox_xy.addWidget(QLabel('x: '))
        hbox_xy.addWidget(self.x_le)
        hbox_xy.addWidget(QLabel('y: '))
        hbox_xy.addWidget(self.y_le)

        hbox_nt = QHBoxLayout()
        hbox_nt.addWidget(QLabel('횟수: '))
        hbox_nt.addWidget(self.n_le)
        hbox_nt.addWidget(QLabel('딜레이: '))
        hbox_nt.addWidget(self.t_le)

        self.vbox.addWidget(self.open_btn)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox_label)
        self.vbox.addStretch(1)
        self.vbox.addLayout(hbox_xy)
        self.vbox.addLayout(hbox_nt)
        self.vbox.addWidget(self.click_btn)
        self.setLayout(self.vbox)

        self.open_btn.clicked.connect(self.show_dialog)
        self.click_btn.clicked.connect(self.click_btn_clicked)

        self.setWindowTitle('Image')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_dialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.append(QLabel())
            self.label[-1].setPixmap(pixmap.scaledToWidth(pixmap.width()*1.1))
            self.fname.append(fname[0])
            self.hbox_label.addWidget(self.label[-1])

    def click_btn_clicked(self):
        n = int(self.n_le.text())
        t = float(self.t_le.text())

        if self.x_le.text() and self.y_le.text():
            x_pos = int(self.x_le.text())
            y_pos = int(self.y_le.text())
            pyautogui.click(x_pos, y_pos, clicks=n, interval=t)
        elif len(self.fname):
            print(self.fname)
            for i in range(n):
                for j in range(len(self.fname)):
                    center = pyautogui.locateCenterOnScreen(self.fname[j])
                    pyautogui.click(center, interval=t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
