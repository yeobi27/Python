import sys
from PyQt5.QtWidgets import *
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        x = 0
        y = 0

        btn1 = QPushButton('좌상단', self)
        btn1.move(20, 20)
        btn2 = QPushButton('우하단', self)
        btn2.move(20, 50)

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.ltPoint = QLabel(self.text, self)
        self.ltPoint.move(100, 30)

        text = 'x: {0}, y: {1}'.format(x, y)
        self.rbPoint = QLabel(self.text, self)
        self.rbPoint.move(100, 60)

        self.setMouseTracking(True)

        # global qleX
        self.qle = QLineEdit(str(pyautogui.position()), self)
        self.qle.move(20, 120)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 600)
        self.show()

    def mousePressEvent(self, e):

        xPos = e.globalX()
        yPos = e.globalY()

        text = 'x: {0}, y: {1}'.format(xPos, yPos)
        self.ltPoint.setText(text)
        self.ltPoint.adjustSize()
        self.ltPoint.update()

        self.rbPoint.setText(str(pyautogui.position()))
        self.rbPoint.adjustSize()
        self.rbPoint.update()

        self.qle.setText(str(pyautogui.position()))

    def mouseMoveEvent(self, e):

        xPos = e.globalX()
        yPos = e.globalY()

        text = 'x: {0}, y: {1}'.format(xPos, yPos)
        self.ltPoint.setText(text)
        self.ltPoint.adjustSize()
        self.ltPoint.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
