from tkinter import *
from tkinter import ttk
from pynput import mouse
import pyautogui


root = Tk()
root.title("마우스 좌표 찾기")
root.geometry("400x300")
x1 = 0
y1 = 0

########################################
lblX1 = Label(root, text="X1")
lblX1.grid(row=1, column=1)

entryX1 = Entry(root, width=10)
entryX1.grid(row=1, column=2)

lblY1 = Label(root, text="Y1")
lblY1.grid(row=1, column=3)

entryY1 = Entry(root, width=10)
entryY1.grid(row=1, column=4)

BtnLeftTop = Button(root, text="상단위치", command=lambda: aim(BtnLeftTop))
BtnLeftTop.grid(row=1, column=5)

lblX2 = Label(root, text="X2")
lblX2.grid(row=2, column=1)

entryX2 = Entry(root, width=10)
entryX2.grid(row=2, column=2)

lblY2 = Label(root, text="Y2")
lblY2.grid(row=2, column=3)

entryY2 = Entry(root, width=10)
entryY2.grid(row=2, column=4)

BtnRightBottom = Button(root, text="하단위치", command=lambda: aim(BtnRightBottom))
BtnRightBottom.grid(row=2, column=5)

# Color Extraction
############################################

BtnSetColor = Button(root, text="색상추출", command=lambda: colorClick())
BtnSetColor.grid(row=3, column=1)

entry4 = Entry(root, width=35)
entry4.grid(row=3, column=2)

############################################

label3 = Label(root, text="반복횟수")
label3.grid(row=4, column=1)

entry3 = Entry(root, width=10)
entry3.grid(row=4, column=2)
entry3.insert('end', '100')

###########################################

button2 = Button(root, text="클릭 시작", command=lambda: click_m())
button2.grid(row=4, column=3)

########################################


def colorClick():
    with mouse.Listener(
        on_click=isClicked
    ) as listener:
        listener.join()
        xyColor()


def isClicked(x, y, button, pressed):
    if pressed:

        global x1
        global y1
        x1 = x
        y1 = y

    if not pressed:
        return False


def xyColor():
    RGB = pyautogui.screenshot().getpixel((x1, y1))
#     print('x : {}, y : {}, RGB = {}     '.format(
#         x1, y1, RGB), end='\r')
    entry4.insert('end', "("+str(x1)+","+str(y1)+"), RGB = ("+str(RGB)+")")


def aim(btnSel: Button):
    with mouse.Listener(
        on_click=aimOnClick
    ) as listener:
        listener.join()
        xyPosition(btnSel)


def aimOnClick(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y

    if not pressed:
        return False


def xyPosition(btnSel: Button):
    if(btnSel['text'] == '상단위치'):
        entryX1.delete(0, 'end')
        entryX1.insert('end', x1)
        entryY1.delete(0, 'end')
        entryY1.insert('end', y1)
    else:
        entryX2.delete(0, 'end')
        entryX2.insert('end', x1)
        entryY2.delete(0, 'end')
        entryY2.insert('end', y1)


def click_m():
    click_num = int(entry3.get())

    # 반복시작
    for a in range(0, click_num):
        pyautogui.click(x1, y1)


root.mainloop()
