import pyautogui
import time
import pyttsx3 
import os

# pyttsx3 - gives audo output

def screenshottaker(finemane):
    try:
        pyttsx3.speak("Go to the window of which you will take screenshot.")
        print("Go to the window of which you will take screenshot.")
        time.sleep(5)
        pyautogui.screenshot(filename)
        pyttsx3.speak("Screenshot Taken!")
        print("Screenshot Taken!")
        os.system(filename)
    except:
        pyttsx3.speak(filename + " already exsists!")
        print(filename + " already exsists!")

while True:
    pyttsx3.speak('Enter filename')
    filename = input("Enter filename : ")
    screenshottaker(filename)
