## 달고나 게임 Read Me

<p align="center">
    
</p>
<h4 align="center">드라마 '오징어 게임' 속 컨텐츠를 직접 체험할 수 있는 AI 플랫폼</h4>
<p align="center">
  <a href="#tutorial">Tutorial</a></a> • 
  <a href="#features">Features</a> •  
  <a href="#system-structure">System Structures</a> •
  <a href="#Files">Files</a> • 
  <a href="#contributor">Contributors</a> • 
  <a href="#license">License</a>
</p>
<p align="center">
    이 프로젝트는 2021 KT 하반기 인턴교육 과정 중 진행되었습니다. <br/>
    이 프로젝트는 상업적인 목적이 포함되어 있지 않습니다. 
    이 프로젝트는 팀 '우린깐부잖어'에 의해 개발되었습니다.<br/>
    해당 레포는 'AI 오징어 게임' 중 '달고나 게임' 코드를 저장하고 있습니다.      
</p>


## Tutorial

1. 코드 다운
2. pip install opencv-python
3. pip install mediapipe==0.8.8
4. pip install flask
5. pip install numpy
6. 이 외 미설치 라이브러리 설치(상위 폴더 requirements 파일 참고)
7. main.py 코드 실행
8. 서버 IP 접속하여 게임 시작(127.0.0.1:5000) * 로컬환경(테스트 페이지)에서 게임 단독 실행시


## Features

<p align="center">
    <h5>1. 객체 탐지</h5>
    <h5>2. 손가락의 갯수와 좌표 판별</h5>
    <h5>3. 시작 조건</h5>
    <h5>4. 시작 타이머</h5>
    <h5>5. 게임 가이드 표시</h5>    
    <h5>6. 게임 진행 타이머</h5>
    <h5>7. 달고나 이미지에 실시간 경로 표시</h5>
    <h5>8. 정답 달고나 좌표 추출</h5>
    <h5>9. 실시간 좌표 비교</h5>
    <h5>10. 달고나 깨짐 효과</h5>
    <h5>11. 게임 종료 조건 설정</h5>
    <h5>12. 최종평가를 위한 캔버스 추가</h5>
    <h5>13. 최종 그림과 정답 컨투어 비교로 버그 방지</h5>
    <h5>14. 점수 산출</h5>
    <h5>15. 게임 반복 기능</h5>
    <h5>16. 게임 진행상황 API</h5>
    <h5>17. Flask 서버</h5>
</p>


## Files
<p align="center">
    <h5>1. img : 달고나 이미지 저장 폴더</h5>
    <h5>2. templates : 테스트 페이지 저장 폴더</h5>
    <h5>3. HandDetectModel.py : 손 인식 모델</h5>
    <h5>4. dalgona_result : contour 비교 모듈</h5>
    <h5>5. main.py : 달고나 게임 메인 서버</h5>
</p>


## System Structure
<p align="center">
    <img src="https://user-images.githubusercontent.com/78125184/148163269-492f7c99-41c2-43ef-8170-5182d8730ff2.png"/>
</p>


## Contributor

Maintainer : 전민준, 조민호
Contributor : 김서정, 김수연, 김남협, 김주환, 박수정, 유동헌, 윤혜정, 허나연



## License

Apache License 2.0
