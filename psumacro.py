import pygame
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

while True:
    try:
        events = pygame.event.get()
        for event in events:
            print("made it to for loop")
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                print("detected KEYDOWN")
                if event.key == pygame.K_LSHIFT:
                    print("detected LSHIFT")
                    if event.key == pygame.K_F1:
                        print("detected F1")
                        #keyboard.press(Key.shift)
                        #keyboard.press(Key.f1)
                        #time.sleep(0.25)
                        #keyboard.release(Key.shift)
                        #keyboard.release(Key.f1)
                        #time.sleep(1)

                        keyboard.press("a")
                        keyboard.release("a")
                        keyboard.press("b")
                        keyboard.release("b")

    except:
        pass
