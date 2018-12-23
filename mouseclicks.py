import pyautogui
import keyboard
import time

loopNum = 0
while True:
    try:
        startTime = time.time()
        if keyboard.is_pressed('Home'):
            x, y = pyautogui.position()
            pyautogui.click(x,y)

            endTime = time.time()
            execTime = endTime - startTime
            execTimeInMS = 1000 * execTime
            execPerSec = execTimeInMS / loopNum
            loopNum = loopNum + 1
            print(loopNum)
            print(execPerSec)
        elif keyboard.ispressed('End'):
            break
        else:
            pass
    except:
        pass
