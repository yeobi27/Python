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

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label1 = QLabel(self.text, self)
        self.label1.move(20, 20)

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label2 = QLabel(self.text, self)
        self.label2.move(40, 40)

        self.setMouseTracking(True)

        # global qleX
        self.qle = QLineEdit(str(pyautogui.position()), self)
        self.qle.move(20, 120)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):

        xPos = e.globalX()
        yPos = e.globalY()

        text = 'x: {0}, y: {1}'.format(xPos, yPos)
        self.label1.setText(text)
        self.label1.adjustSize()
        self.label1.update()

        self.label2.setText(str(pyautogui.position()))
        self.label2.adjustSize()
        self.label2.update()

        self.qle.setText(str(pyautogui.position()))

    def mouseMoveEvent(self, e):

        xPos = e.globalX()
        yPos = e.globalY()

        text = 'x: {0}, y: {1}'.format(xPos, yPos)
        self.label1.setText(text)
        self.label1.adjustSize()
        self.label1.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
