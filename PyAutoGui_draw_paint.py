import pyautogui

#pyautogui.PAUSE = 2.5
#pyautogui.FAILSAFE = False

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 25
    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 25
    pyautogui.dragRel(0, -distance, duration=0.5)  # move up