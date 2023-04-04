# InvisibilityCloak (https://github.com/hamdivazim/InvisibilityCloak)
# This project is licnensed under the Apache License 2.0
# Do not claim as your own
#
# © Hamd Waseem 2023

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(5)

while True:
    return_val, background = cap.read()
    if return_val == True:
        break

background = cv2.resize(background, (720, 640))
bg = background.copy()

while cap.isOpened():
    return_val, frame = cap.read()

    if not return_val:
        break
    frame = cv2.resize(frame, (720, 640))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 125, 50])
    upper = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower, upper)

    lower = np.array([170, 120, 70])
    upper = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv, lower, upper)

    lower = np.array([110, 50, 50])
    upper = np.array([130, 255, 255])

    mask3 = cv2.inRange(hsv, lower, upper)

    lower = np.array([28, 39, 100])
    upper = np.array([42, 100, 62])

    mask4 = cv2.inRange(hsv, lower, upper)

    mask = mask1+mask2+mask3+mask4

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((5, 5), np.uint8))

    frame[np.where(mask==255)] = 0

    background = bg.copy()
    background[np.where(mask==0)] = 0

    out = cv2.addWeighted(background, 1, frame, 1, 0)

    cv2.imshow('Invisibility', out)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
