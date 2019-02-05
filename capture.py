import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
import pyautogui
import time


hwnd = win32gui.FindWindow(None, r'DRL Simulator')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)

i = 1
while True:
	image = ImageGrab.grab(dimensions)
	# image.show()
	image.save("./Images/" + str(i) + ".jpg", "JPEG")
	time.sleep(0.01)
	i+=1