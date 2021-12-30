import cv2
import numpy as np
import HandDetectModule as hdm
import dalgona_result as dr
import random
from threading import Thread
import time

#######################
brushThickness = 15
display_size_width = 500
display_size_height = 500
startlist = [[250,143],[250,122],[250,108],[250,117],[250,117]] #1. 삼각형, 2.원, 3.별, 4. 트리, 5. 우산
imglist = ["img/tri.jpg", "img/circle.jpg", "img/star.jpg", "img/tree.jpg", "img/um.jpg"]
########################

global start_condition
start_condition = False
global starttimer
starttimer= False


color = (0, 0, 0)  # 컬러지정

cap = cv2.VideoCapture(1)  # 웹캠 번호 지정
cap.set(3, display_size_width)  # 가로 크기 수정
cap.set(4, display_size_height)  # 세로 크기 수정

detector = hdm.MPHands(detectionCon=0.85, maxHands=1)
xp, yp = 0, 0


def timer(startlist, shape_num):
    global start_condition
    global starttimer
    time_limit = time.time() + 3
    while time.time() < time_limit:
        print(time_limit-time.time())
        if start_condition == False and startlist[shape_num][0] - 10 < x1 < startlist[shape_num][0] + 10 and \
            startlist[shape_num][1] - 10 < y1 < startlist[shape_num][1] + 10 :
            pass

        else:
            starttimer = False
            return

    start_condition = True


# 달고나 모양 랜덤 선택
# shape_num = random.randrange(0,5)
shape_num = 4

# 달고나 모양 좌표 추출
imgCanvas = cv2.imread(imglist[shape_num])
imgray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(len(contours[1]))

# 비교를 위한 결과값
imgCanvas1 = np.ones((500, 500, 3), np.uint8) * 255


log = []
while True:
    # 웹캠
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if start_condition == False:
        imgCanvas = cv2.imread(imglist[shape_num])

    # 손인식, 손가락 좌표 검출
    img = detector.DetectHand(img)
    hand_co = detector.DetectCoordi(img, draw=False)

    if len(hand_co) != 0:

        # 8, 12번 x,y값
        global x1, y1
        x1, y1 = hand_co[8][1:]
        x2, y2 = hand_co[12][1:]

        # 손가락업 판별
        fingers = detector.Up()

        # 손가락 2개 업일 때
        if fingers[1] and fingers[2] and start_condition == False:
            xp, yp = 0, 0
            cv2.circle(imgCanvas, (x1, y1), 8, color, cv2.FILLED)

            # 처음 시작 타이머
            if starttimer == False and startlist[shape_num][0] - 10 < x1 < startlist[shape_num][0] + 10 and \
                startlist[shape_num][1] - 10 < y1 < startlist[shape_num][1] + 10 :
                print("game start----------------")
                starttimer = True
                thread = Thread(target=timer, args=(startlist,shape_num))
                thread.start()


        # 손가락 1개 업일 때
        if fingers[1] and fingers[2] == False and start_condition == True:
            cv2.circle(img, (x1, y1), 15, color, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(imgCanvas, (xp, yp), (x1, y1), color, brushThickness)
            cv2.line(imgCanvas1, (xp, yp), (x1, y1), color, brushThickness)
            xp, yp = x1, y1
            # 좌표 비교(채점)
            correct = False
            for i in range(len(contours[1])):
                if (contours[1][i][0][0] - 10 < x1 < contours[1][i][0][0] + 10) and \
                    (contours[1][i][0][1] - 10 < y1 < contours[1][i][0][1] + 10):
                    correct = True
                    print("ALIVE")
                    log.append(1)
                    break

            if correct == False:
                print("*********************die***********************")
                log.append(0)
            print(len(log))
            if correct == True and startlist[shape_num][0] - 10 < x1 < startlist[shape_num][0] + 10 and \
                startlist[shape_num][1] - 10 < y1 < startlist[shape_num][1] + 10 :
                print("game complete----------------")
                break
# and len(contours[1]) < len(log)


    cv2.imshow('dd', imgCanvas1)
    cv2.imshow("CAM", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)


dr.score(contours[1], imgCanvas1, shape_num)