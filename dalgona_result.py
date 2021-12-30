import cv2


def score(target, submit, shape_num):
    # 매칭을 위한 이미지 읽기
    # target = cv2.imread(target) # 매칭 대상
    # shapes = cv2.imread(submit) # 그린 도형
    shapes = submit

    # 그레이 스케일 변환
    # targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
    
    # 바이너리 스케일 변환
    # ret, targetTh = cv2.threshold(targetGray, 128, 255, cv2.THRESH_BINARY_INV)
    ret, shapesTh = cv2.threshold(shapesGray, 20, 255, cv2.THRESH_BINARY_INV)

    # 컨투어 찾기
    # cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntrs_shapes, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 대상 도형의 사이즈 측정
    target_size = cv2.contourArea(target)

    # 매칭 점수와 사이즈 비율을 저장할 리스트
    matching = []
    
    # 각 도형과 매칭을 위한 반복문
    for contr in cntrs_shapes:
        cv2.drawContours(shapes, contr, -1, (0, 255, 0), 3)
        # 대상 도형과 그린 도형 중 하나와 매칭 실행
        match = cv2.matchShapes(target, contr, cv2.CONTOURS_MATCH_I2, 0.0)
        # 그린 도형의 사이즈 측정
        shape_size = cv2.contourArea(contr)
        # 매칭 점수와 크기 비율을 쌍으로 저장
        matching.append([match, shape_size/target_size])

    # 사이즈로 정렬(제일 큰게 진짜 그리고 싶었던거라는 판단)
    matching.sort(key=lambda x : -x[1])

    if shape_num == 4:
        for cand in matching:
            print(cand)
            # 20% 이상 크면 pass
            if cand[1] > 1.5:
                continue
            # 매칭 점수가 0.3 이하이고, 사이즈가 20% 이하로 차이나면 성공
            elif 1.0 <= cand[1] <= 1.5:
                if cand[0] <= 3:
                    return 'success'
            # 사이즈로 정렬했기 때문에 이 뒤로는 볼 필요도 없이 실패
            else:
                break

    else:
        for cand in matching:
            print(cand)
            # 20% 이상 크면 pass
            if cand[1] > 1.5:
                continue
            # 매칭 점수가 0.3 이하이고, 사이즈가 20% 이하로 차이나면 성공
            elif 1.0 <= cand[1] <= 1.5:
                if cand[0] <= 1:
                    return 'success'
            # 사이즈로 정렬했기 때문에 이 뒤로는 볼 필요도 없이 실패
            else:
                break
    
    # 실패


    # cv2.imshow('target', target)
    # cv2.imshow('Match Shape', shapes)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return 'fail'

# 이미지 주소
# target_image = './images/circle.png'
# submitted_image = './images/test2.png'

# 실행 결과
# print(score(target_image, submitted_image))