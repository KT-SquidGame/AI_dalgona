import numpy as np
import cv2
def contour():
    img = cv2.imread('img/um.jpg')
    imgCanvas = np.zeros((500, 500, 3), np.uint8)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(contours)
    # for i in contours[0]:
    # cv2.circle(imgCanvas, (20,20), 3, (255,128,0), cv2.FILLED)
    cv2.drawContours(imgCanvas, contours[1], -1, (0,0,255),1)
    # cv2.drawContours(imgCanvas, contours[2], -1, (0,0,255),1)

    for i in range(len(contours[1])):
        print("in x,y : {}, {}".format(contours[1][i][0][0], contours[1][i][0][1]))

    # for i in range(len(contours[2])):
    #     print("out x,y : {}, {}".format(contours[2][i][0][0], contours[2][i][0][1]))


    cv2.imshow('thresh',thr)
    cv2.imshow('contour', img)
    cv2.imshow('d',imgCanvas)

    cv2.waitKey(0)
    cv2. destroyAllWindows()

contour()