import pyautogui

# print(pyautogui.position())
# print(pyautogui.size())

# pyautogui.moveTo(500, 500)
# pyautogui.click()

# pyautogui.click(600, 600, button='right')
# pyautogui.moveRel(0,10)
# pyautogui.doubleClick()

# pyautogui.dragTo(600,600, button='left')
# pyautogui.dragTo(600,800, 2, button='left')
# pyautogui.dragRel(30,0,2, button='right')
# pyautogui.click(600,600)
# pyautogui.typewrite('Hello World!', interval=0.1)

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('my_screenshot.png')
# im3 = pyautogui.screenshot('my_region.png', region=(0,0,300,300))

# five_btn = pyautogui.locateOnScreen('five.png')
# print(five_btn)

# five_btn = pyautogui.locateOnScreen('five.png')
# center = pyautogui.center(five_btn)
# print(center)
center = pyautogui.locateCenterOnScreen('five.png')
pyautogui.click(center)