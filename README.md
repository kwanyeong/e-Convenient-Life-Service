# 🥛 e-Convenient-Life-Service
친환경 Eco 다회용컵 자동관리 공정시스템

---
### 프로젝트 배경
- 친환경적 저탄소 운동 중심의 탄소중립 추진
- 빈번한 탄소플라스틱 제품사용으로 인한 지구온난화, 이상기후으로 인한 자연재해 급증
- 다회용컵(텀블러 등) 활성화를 통한 일회용품 사용 최소화

---
### 프로젝트 목적
- 다회용컵 사용 활성화를 통한 플랫폼 기능을 수행하고 시스템사용 활성화를 위한 ECO 포인트 적립을 유도함으로써 탄소중립목표를 실현
  
---
### 프로젝트 설명
- 다회용컵 제품에 RFID 센서를 부착하여 제품등록
- RFID 센서 제품인식을 통해 대여/반납 시스템 작동시작
- 사용후 제품반납시 카메라센서를 통해 사용 전/후 제품상태 식별
- 식별된 제품상태에 관한 학습된 이미지 모델링을 통해 제품 상태등급을 분류하여 기록 
- 분류된 상태등급에 따른 ECO 포인트 차등지급
- (A등급 -> A등급 : 1500포인트 / A등급 -> B 등급: 500포인트 / A등급 -> C등급 : 폐기대상)

---
#### 기술 스택
![stack](https://github.com/kwanyeong/e-convient-Life-Service/assets/124857002/cb92c3a0-6dde-4fdc-b8b1-2421b5f2b745)

---
##### 메뉴 구성
- Service
- Point
- Rental
- Contact
- MyPage

##### 시스템 기획
![image](https://github.com/kwanyeong/e-Convenient-Life-Service/assets/124857002/9fcd3299-d3f4-491c-b153-494a1eb21424)

---
##### ERD (ER-다이어그램) [DB 개념적 설계]
![image](https://github.com/kwanyeong/e-Convenient-Life-Service/assets/124857002/85e03c14-1b26-429f-abd4-b6e9b520f5d6)

##### DB 설계도 (논리적 설계)
![image](https://github.com/kwanyeong/e-Convenient-Life-Service/assets/124857002/e4aa0e2a-1052-432b-b7e6-4b20aae89616)

---
##### 회로구성도
![image](https://github.com/kwanyeong/e-Convenient-Life-Service/assets/124857002/250b6136-8409-4f82-b2b6-8bc7555e27f9)

---
##### 시연영상
[![image](https://github.com/kwanyeong/e-convient-Life-Service/assets/124857002/aa97e6ec-8ffd-4399-99f4-dfe53f35585d)](https://www.youtube.com/watch?v=y84rJoFc4vo)

[시연영상](https://www.youtube.com/watch?v=y84rJoFc4vo)

---
##### 최종발표 PPT자료
[![image](https://github.com/kwanyeong/e-convient-Life-Service/assets/124857002/e2080355-d78b-4bd3-9b17-21cfd5a2adad)](https://github.com/kwanyeong/e-convient-Life-Service/assets/124857002/e2080355-d78b-4bd3-9b17-21cfd5a2adad)
[최종발표 PPT](https://github.com/kwanyeong/e-convient-Life-Service/files/13269935/ECO._.pptx)


---
#### 역할 구성

### My Stack
(1) Web 개발 (HTML/CSS, JavaScript, AJAX, Django, Flask)

    - Main 페이지 : 네비게이션 바, 스크롤바, 캐로셀(Carousel), 이벤트정보 기능 구현 등
    - User/Admin 페이지 : 로그인, 회원가입, 회원가입 완료, Mypage, 회원정보 수정
    - Product 페이지 : 제품정보 등록/수정, 제품정보 조회
    - Rental 페이지 : 대여정보 조회
    - Point 페이지 : 고객 포인트정보 조회

(2) SMTP(Simple Mailing Transfer Protocol) 메일링 서비스 개발

    - Contact 페이지 : 회사로 직접 연락할 수 있는 메일링 기능 구현
    - SMTP/SSL(Secure Sockets Layer) 메일통신간 정보보안 무결성 제공

(3) DB – Server 통신

    - MySQL : 웹서버 – DB정보간 실시간 통신 (MQTT Socket 통신)

(4) AI 모델링

    - Roboflow 웹사이트에서 Crack and Dent 데이터 수집
    - OpenCV 기반 이미지 딥러닝 모델구축 및 학습

(5) 프로젝트 PM 총괄

    - 프로젝트 기획(WireFrame 화면설계), DB설계, Web 개발 및 AIoT 프로젝트 관리

### Team Stack

    - (1) 제품 인식 : RFID기술을 활용한 제품간 고유 식별 ID 생성
    - (2) DB데이터 통신 : MQTT socket 통신
    - (3) AIoT 하드웨어 제작
    - (4) AIoT 소프트웨어 모델링 (Arduino / RasberryPi)
---
