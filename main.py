# main.py
import cv2
import pickle
import cvzone
import numpy as np
import datetime

# Load video
cap = cv2.VideoCapture('carPark.mp4')

# Load saved parking positions
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Slot size
width, height = 107, 48

def checkParkingSpace(imgPro):
    freeCount = 0
    totalSlots = len(posList)

    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)  # Green
            thickness = 3
            freeCount += 1
        else:
            color = (0, 0, 255)  # Red
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    # Show Free / Occupied using cvzone
    cvzone.putTextRect(img, f'Free: {freeCount}', (20, 30), scale=2,
                       thickness=2, offset=5, colorR=(0, 255, 0))
    cvzone.putTextRect(img, f'Occupied: {totalSlots - freeCount}', (20, 80), scale=2,
                       thickness=2, offset=5, colorR=(255, 0, 0))

    # Show Date and Time (simple top-right corner)
    now = datetime.datetime.now()
    date_str = now.strftime("%d-%m-") + "2024"
    time_str = now.strftime("%H:%M:%S")

    # Display like CCTV style in white/yellow
    cv2.putText(img, f'{date_str}', (820, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    cv2.putText(img, f'{time_str}', (820, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

while True:
    success, img = cap.read()
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Preprocessing
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThres, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow("Smart Parking System", img)
    if cv2.waitKey(10) == ord('q'):
        break
