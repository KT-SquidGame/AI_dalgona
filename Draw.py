import cv2
import numpy as np
import HandDetectModule as hdm
import dalgona_result as dr

#######################
brushThickness = 15
display_size_width = 500
display_size_height = 500
########################

color = (0,0,0) #컬러지정

cap = cv2.VideoCapture(1) #웹캠 번호 지정
# print(cap.get(3), cap.get(4))
cap.set(3, display_size_width) #가로 크기 수정
cap.set(4, display_size_height) #세로 크기 수정

detector = hdm.MPHands(detectionCon=0.85,maxHands=1)
xp, yp = 0, 0
# imgCanvas = np.zeros((display_size_height, display_size_width, 3), np.uint8)


#달고나 모양 좌표 추출
imgCanvas = cv2.imread('img/dal.jpg')
imgray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(imgray, 127, 255, 0)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours[1]))


#비교를 위한 결과값
imgCanvas1 = np.ones((500, 500, 3), np.uint8) * 255

start = False
log = []
while True:
    # 웹캠
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # img = cv2.flip(imgCanvas, 1)
    if start == False:
        imgCanvas = cv2.imread('img/dal.jpg')

    # 손인식, 손가락 좌표 검출
    img = detector.DetectHand(img)
    hand_co = detector.DetectCoordi(img, draw=False)

    if len(hand_co) != 0:

        # 8, 12번 x,y값
        x1, y1 = hand_co[8][1:]
        x2, y2 = hand_co[12][1:]

        # 손가락업 판별
        fingers = detector.Up()
        # print(fingers)

        # 손가락 2개 업일 때
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            cv2.circle(imgCanvas, (x1, y1), 8, color, cv2.FILLED)
            # print(x1,y1, sep="     ")
            # print()

        # 손가락 1개 업일 때
        if fingers[1] and fingers[2] == False:
            start = True
            cv2.circle(img, (x1, y1), 15, color, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(imgCanvas, (xp, yp), (x1, y1), color, brushThickness)
            cv2.line(imgCanvas1, (xp, yp), (x1, y1), color, brushThickness)
            xp, yp = x1, y1
            # 좌표 비교(채점)
            correct = False
            for i in range(len(contours[1])):
                if (contours[1][i][0][0] - 10 < x1 < contours[1][i][0][0] + 10) and (contours[1][i][0][1] - 10 < y1 < contours[1][i][0][1] + 10):
                    correct = True
                    log.append(1)
                    break
            if correct == False:
                print("*********************die***********************")
            if correct == True:
                print("ALIVE")
            if correct == True and 230 < x1 < 250 and 132 < y1 < 152 and len(contours[1]) < len(log):
                print("game complete----------------")
            # print(len(log))
            # print(dr.score(contours[1],imgCanvas))

        
    #한 화면에 표현
    # imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    # _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    # imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    # img = cv2.bitwise_and(img,imgInv)
    # img = cv2.bitwise_or(img,imgCanvas)

    #그린 이미지 비교
    # imgCanvas1 = imgCanvas
    # imgray1 = cv2.cvtColor(imgCanvas1, cv2.COLOR_BGR2GRAY)
    # ret1, thr1 = cv2.threshold(imgray1, 1, 255, cv2.THRESH_BINARY_INV)
    # contours1, _ = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(imgCanvas1, contours1, -1, (0,0,255),1)
    cv2.imshow('dd',imgCanvas1)

    # # img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0) #한 화면에 동시에 표현
    cv2.imshow("CAM", img)
    cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow('d',dr.score(contours[1],imgCanvas))
    # cv2.imshow("Inv", imgInv)
    cv2.waitKey(1)