# 밀버디🍚

- 다양한 사용자들이 음식 주문을 결합하여 배달비를 절감하고, 주문 과정을 더 효율적으로 만드는 웹사이트 개발.
- 사용자는 개인 정보를 등록하고 로그인하여 서비스를 이용.
- 게시글 확인 및 채팅 참여기능을 통해 소통.
- 메뉴 추천기능과 날씨정보를 통한 메뉴 선정에 도움.

## 📖 프로젝트 소개 및 계획이유

- 프로젝트 소개
  > - 다양한 사용자들이 음식 주문을 결합하여 배달비를 절감하고, 주문 과정을 더 효율적으로 만드는 웹사이트 개발.
  > - 사용자는 개인 정보를 등록하고 로그인하여 서비스를 이용.
  > - 게시글 확인 및 채팅 참여기능을 통해 소통.
  > - 메뉴 추천기능과 날씨정보를 통한 메뉴 선정에 도움.
- 프로젝트 계획이유
  > 높아져 가는 배달비로 인해 배달을 시키는데에 부담이 발생하고,  
  > 최소금액이 존재하여 내가 먹을 양보다 많은 양을 시키게 되고 그로 인해 원하지 않은 많은 음식물 쓰레기와 지출이 발생합니다.  
  > 또한, 알뜰 배달이라는 서비스가 존재하지만 긴 배달시간으로 인해 음식이 식거나 형태가 변형되는 경우가 발생하여 이와 같은 문제로 인해 느끼는 불편함을 해소하고자 계획하였습니다.

## 🕰 개발 기간

> 2023.08.17 ~ 2023.09.04

## 🤝 멤버 구성

- 김바름 - django channels를 이용한 채팅기능 구현, open API 연동, 프론트엔드 구현, docker-compose를 통한 배포
- 김범석 - JWT를 이용해 로그인, 회원가입 기능 구현, API 명세서 작성, README 작성
- 류형환 - 게시글 CRUD 구현, 주소와 카테고리 별 필터기능 구현
- 임동성 - USER 관련 정보 수정 기능 구현, 다음 주소 API 연동

## ⚙ 기술 스택

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white"> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white"> <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/Daphne-5b9bd5?style=for-the-badge&logo=Daphne&logoColor=white"> <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=Nginx&logoColor=white">


## 📕 배포 주소

- https://mealbuddy.space/

- 테스트 계정

```
Email : test@test.com
Password : password123
```

## 📤배포환경

### 아키텍처
<img src="./img/배포환경.png">  

### 배포 방식
- Nginx를 웹서버로, gunicorn을 wsgi 서버로, daphne를 asgi 서버로 이용하였습니다.  
- docker를 이용해서 nginx와 빌드된 react 파일을 컨테이너로 만든 후, '/' 경로에서는 nginx가 빌드된 react 파일을 서빙하도록 구성하였습니다.  
- django 도 docker 컨테이너로 만들어준 후, gunicorn은 8080 포트에, daphne는 8000 포트에 매핑한 후, nginx의 리버스 프록시를 이용해서 '/api/' 경로로 요청이 들어올 경우에는 gunicorn을 통해서 django와 wsgi 통신을 하게 하고, '/ws/' 경로로 요청이 들어올 경우에는 daphne를 통해서 asgi 통신을 하도록 구성하였습니다.
- 백엔드의 데이터베이스는 postgreSQL을 이용하였고, websocket연결에서 channels의 Channels Layer를 유지하기 위해서 redis를 이용하였습니다. postgreSql과 redis 또한 도커 컨테이너로 구성했습니다.  
- 각각의 컨테이너는 docker-compose를 이용해서 묶어주었습니다.
- https 인증서는 certbot을 이용해서 발급받았습니다.

### 프론트엔드

- [프론트엔드 레포지토리](https://github.com/Group-buying-service/mealbuddy-front)
- React를 활용해서 SPA 형식의 프론트엔드를 구성하였습니다.

## 📌 주요 기능

- 지역기반 배달 공동구매 중개 커뮤니티
- 메뉴 추천
- 주민간의 채팅 서비스
- 지역 날씨 정보 확인

## 🚩 API 경로

**백엔드**  
- prefix: `https://mealbuddy.space/api`

|URL|기능|
|---|---|
|`/user/login/`|로그인|
|`/user/register/`|회원가입|
|`/user/delete/`|회원탈퇴|
|`/user/changepassword/`|비밀번호 변경|
|`/user/update/`|유저정보 수정|
|`/user/current/`|유저정보 확인|
|`/post/`|글 목록 조회|
|`/post/detail/<post_id>/`|글 상세 조회|
|`/post/write/`|글 작성|
|`/post/detail/<post_id>/edit/`|글 수정|
|`/post/detail/<post_id>/delete/`|글 삭제|
|`/chat/<room_id>/`|채팅방 상태 조회, 채팅방 접근권한 얻기, 채팅방 삭제|
|`/chat/<room_id>/user/`|채팅방 유저 조회, 채팅방 나가기|
|`/chat/<room_id>/user/ban/`|채팅방 유저 강퇴|
|`/openAPI/weather/`|날씨 정보 조회|
|`/openAPI/foodchoicer/`|음식 추천|

## 🚩 [API 명세서](https://github.com/Group-buying-service/mealbuddy-backend/blob/main/API%20%EB%AA%85%EC%84%B8%EC%84%9C.md)

<details>
<summary style="font-size: 1.3rem;">API 명세서 접기/펼치기</summary>

## API 명세서 설명
- 모든 엔드포인트는 `https://mealbuddy.space/api` 를 기준으로 작성되어 있습니다.
- 응답이 따로 표기되지 않은 경우에는 status code와 에러시의 에러메세지만 반환됩니다.

##  User
### 회원가입
- URL : `/user/register/`
- Method : `POST`
- Description : 유저를 새로 생성하고 토큰값을 생성하여 반환합니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |email|string|필수|이메일|
    |username|string|필수|유저명|
    |password|string|필수|비밀번호|
    |password2|string|필수|비밀번호 확인|
    |address|string|필수|주소|


- Request 예시
    ```
    {
        "username": "testuser",
        "email": "test@email.com",
        "password": "test1234",
        "password2": "test1234",
        "address": "제주특별자치도 제주시 용담이동"
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 로그인
- URL : `/user/login/`
- Method : `POST`
- Description : 로그인에 필요한 정보를 가지고 로그인합니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |email|string|필수|이메일|
    |password|string|필수|비밀번호|

- Request 예시
    ```
    {
        "email": "test@email.com",
        "password": "test1234"
    }
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 유저 삭제
- URL : `/user/delete/`
- Method : `POST`
- Description : 유저의 정보를 삭제합니다.
 - Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|

- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |password|string|필수|비밀번호|

- Request 예시  
    ```
    {
        "password": "test1234"
    }
    ```


### 비밀번호 변경
- URL : `/user/changepassword/`
- Method : `POST`
- Description : 현재 비밀번호를 새로운 비밀번호로 변경합니다.
 - Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |current_password|string|필수|현재 비밀번호|
    |new_password1|string|필수|신규 비밀번호|
    |new_password2|string|필수|신규 비밀번호 확인|
- Request 예시  
    ```
    {
        "current_password": "test1234",
        "new_password1": "testtest",
        "new_password2": "testtest"
    }
    ```

### 유저 정보 확인
- URL : `/user/current/`
- Method : `GET`
- Description : 사용자의 정보를 확인합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 프로필 업데이트
- URL : `/user/update/`
- Method : `POST`
- Description : 사용자의 username과 address를 변경합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |username|string||유저명|
    |address|string||주소|

- Request 예시  
    ```
    {
        "username": "test",
        "address": "경상남도 밀양시 내이동"
    }
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```
---

### - Post

### 파라미터 정의

- category
    - 족발,보쌈
    - 찜,탕,찌개
    - 돈까스,회,일식
    - 피자
    - 고기구이
    - 양식
    - 치킨
    - 중식
    - 아시안
    - 백반,죽,국수
    - 도시락
    - 분식
    - 카페,디저트
    - 페스트푸드

### 글 목록 조회
- URL : `/post/?category={category}&page={page}`
- Method : `GET`
- Description : 유저의 address와 일치하는 게시글 목록을 쿼리에 맞춰서 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |cateogory|string||검색할 카테고리|
    |page|string||이동할 페이지|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/?category=치킨&page=1
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |posts|array|게시글 목록|
    |paginator|objects|페이지 정보|

    - posts  
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|게시글 pk|
        |title|string|제목|
        |created_at|datetime|작성시간|
        |category|string|카테고리|
        |address|int|작성된 지역 주소|
        |content|string|내용|
        |is_compelete|boolean|모집완료 여부|
        |target_number|int|목표 인원수|
        |join_number|int|참여 인원수|
        |chat_id|int|게시글의 채팅방 pk|
        |writer|int|작성자 정보|

        - writer
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|int|작성자 유저명|
            |email|int|작성자 이메일|
    
    - paginator
        |파라미터|타입|설명|
        |---|---|---|
        |page_range|array|페이지 범위, 현재페이지 기준으로 10개만 반환|
        |current_page|int|현재 페이지 번호|
        |prev_button|int, null|현재페이지-10, 1 미만일 경우 1, 1 페이지일 경우 null|
        |next_button|int, null|현재페이지+10, 마지막페이지보다 클경우 마지막페이지, 마지막페이지일 경우 null|
    
- Response 예시  
    ```
    {
        "posts" : [
            {
                "id": "1",
                "title": "치킨먹으실분 찾아요",
                "created_at": "2023-09-01 01:34:49.237071+00:00"
                "category": "치킨",
                "address": "제주특별자치도 제주시 용담이동",
                "content": "치킨이 너무 먹고싶네요",
                "is_compelete": "true",
                "target_number": "3",
                "join_number": "3",
                "chat_id": "1",
                "writer": {
                    "id": "3",
                    "username": "test",
                    "email": "test@test.com"
                }
            }
        ]
        "paginator": {
            "page_range": "[1,2,3,4,5,6,7,8,9,10]",
            "current_page": "1",
            "prev_button": "null",
            "next_button": "11",
        }
    }
    ```

### 글 작성
- URL : `/post/write/`
- Method : `POST`
- Description : 새로운 글을 작성합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |title|string|필수|제목|
    |category|string|필수|카테고리|
    |target_number|int|필수|목표 인원, 최소 2, 최대 10|
    |content|string|필수|내용|
- Request 예시  
    ```
    {
        "title": "치킨이 먹고싶어요",
        "category": "치킨",
        "모집인원": "8",
        "content": "치킨이 먹고싶어요",
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 상세 조회
- URL : `/post/detail/{id}/`
- Method : `GET`
- Description : 작성된 글의 상세 내용을 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/detail/1/
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |is_joined|bool|요청을 보낸사람의 채팅 참여 여부|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "is_joined": "true",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 수정
- URL : `/post/detail/{id}/edit/`
- Method : `POST`
- Description : 작성되어 있는 글을 수정합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|
    |title|string|필수|제목|
    |category|string|필수|카테고리|
    |target_number|int|필수|목표 인원, 최소 2, 최대 10|
    |content|string|필수|내용|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/detail/1/

    {
        "title": "치킨이 먹고싶어요",
        "category": "치킨",
        "모집인원": "8",
        "content": "치킨이 먹고싶어요",
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |is_joined|bool|요청을 보낸사람의 채팅 참여 여부|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "is_joined": "true",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 삭제
- URL : `/post/detail/{id}/delete/`
- Method : `POST`
- Description : 작성되어 있는 글을 삭제합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
    |X-CSRFToken|string|필수|csrftoken|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|
- Request 예시  
    ```
    https://mealbuddy.space/post/detail/1/delete/
    ```

---

### - Chat

- 소켓 통신의 경우 엔드포인트를 따로 기재합니다.

### 채팅방 정보 조회
- URL : `/chat/{id}/`
- Method : `GET`
- Description : 채팅방의 정보 및 메세지를 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |messages|array|메세지 목록|
    |title|string|채팅방 제목|
    |target_number|int|채팅방 최대 인원|
    |join_number|int|채팅방 참여 인원|
    |writer|objects|채팅방 생성자 정보|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
    
    - writer  
        |파라미터|타입|설명|
        |---|---|---|
        |id|array|채팅방 생성자 pk|
        |username|array|채팅방 생성자 유저명|
        |email|array|채팅방 생성자 이메일|

- Response 예시  

    ```
    {
        "messages": [
            {
                "message": "안녕하세요",
                "created_at": "2023-09-01 01:34:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "1",
                    "username": "test",
                    "email": "test@test.com"
                }
            },
            {
                "message": "안녕하세요!!",
                "created_at": "2023-09-01 01:55:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "2",
                    "username": "test2",
                    "email": "test2@test.com"
                }
            }
        ],
        "writer": {
            "id": "1",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 채팅방 접근 권한 얻기
- URL : `/chat/{id}/`
- Method : `POST`
- Description : 채팅방의 접근 권한을 얻습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |messages|array|메세지 목록|
    |title|string|채팅방 제목|
    |target_number|int|채팅방 최대 인원|
    |join_number|int|채팅방 참여 인원|
    |writer|objects|채팅방 생성자 정보|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
    
    - writer  
        |파라미터|타입|설명|
        |---|---|---|
        |id|array|채팅방 생성자 pk|
        |username|array|채팅방 생성자 유저명|
        |email|array|채팅방 생성자 이메일|

- Response 예시  

    ```
    {
        "messages": [
            {
                "message": "안녕하세요",
                "created_at": "2023-09-01 01:34:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "1",
                    "username": "test",
                    "email": "test@test.com"
                }
            },
            {
                "message": "안녕하세요!!",
                "created_at": "2023-09-01 01:55:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "2",
                    "username": "test2",
                    "email": "test2@test.com"
                }
            }
        ],
        "writer": {
            "id": "1",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 채팅방 유저 리스트 조회
- URL : `/chat/{id}/user/`
- Method : `GET`
- Description : 채팅방의 접근 권한을 얻습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |response|array|유저리스트|
    |id|int|작성자 pk|
    |username|string|작성자 유저명|
    |email|string|작성자 이메일|

- Response 예시  

    ```
    {
        0: [
            {
                "id": "1",
                "username": "test",
                "email": "test@test.com"
            },
            {
                "id": "2",
                "username": "test2",
                "email": "test2@test.com"
            }
        ]
    }
    ```

### 채팅방 나가기
- URL : `/chat/{id}/user/`
- Method : `DELETE`
- Description : 채팅방의 접근권한을 삭제합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```

### 채팅방 유저 강퇴
- URL : `/chat/{id}/user/ban/`
- Method : `POST`
- Description : 채팅방에 있는 유저를 강퇴합니다. blacklist에 등록되어서 같은 채팅방에 다시 참여할 수 없습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
    |target_user_id|int|필수|강퇴할 유저 pk|

- Request 예시
    ```
    https://mealbuddy.space/api/post/detail/1/

    {
        "target_user_id": "1"
    }
    ```

## 채팅방 웹소켓 통신

- URL: `wss://mealbuddy.com/ws/chat/{id}/?token={token}`
- Method: `WEB SOCKET`
- Description: 웹 소켓 방식으로 신규 메세지를 주고받습니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
    |token|string|필수|엑세스 토큰|

- Request 예시

    ```
    wss://mealbuddy.com/ws/chat/1/?token=eYDfefd...EDfke
    ```

- Response  
    WebSocket Event 형태로 응답.


### 웹소켓 메세지 송수신
- Event: `onMessage`
- type: `chat.message`, `chat.user.join`, `chat.user.leave`
- Request Elements
    |파라미터|타입|설명|
    |---|---|---|
    |message|string|내용|

- Request 예시
    ```
        {
            "message": "안녕하세요!"
        }
    ```

- Event Elements

    |파라미터|타입|설명|
    |---|---|---|
    |type|string|이벤트 타입|
    |message|objects|신규 메세지|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects, null|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
- Event 예시

    ```
    {
        "type": "chat.message"
        "message": "안녕하세요!!",
        "created_at": "2023-09-01 01:55:49.237071+00:00",
        "chatroom": "1",
        "user": {
            "id": "2",
            "username": "test2",
            "email": "test2@test.com"
        }
    }
    ```


### 웹 소켓 종료
- Event: `onClose`
- Event Elements

    |파라미터|타입|설명|
    |---|---|---|
    |code|int|종료코드. 4040 일 경우 채팅방이 삭제되었음을 의미|

</details>

## 🛢데이터베이스 설계

<img src="db설계도.png">

## 🖥 화면 구성 및 상세 구현

|   **회원가입**  |
|:---------------:|
|<img src="./gif/회원가입_정보입력_.gif">|
|회원가입에는 이메일과 유저명, 그리고 이용자의 행정동 정보를 입력받습니다.<br>다음 우편번호 API를 이용해서 주소를 검색할 수 있고, GeoLocation API와 KAKAO REST API를 이용해서 현재위치를 입력할 수 있습니다.|
|   **회원가입(오류처리)**  |
|<img src="./gif/회원가입_오류처리_.gif">|
|오류발생시 각 필드에 대한 오류가 표기됩니다.|
|   **로그인**   |
|<img src="./gif/로그인.gif">|
|로그인은 PyJWT 라이브러리를 이용한 JWT 방식으로 구현되어 있습니다.|
|   **음식추천 및 날씨정비**   |
|<img src="./gif/음식추천및날씨정보.gif">|
|현재 접속한 지역의 날씨를 공공데이터 포털의 기상청 단기예보 API를 이용해서 표기합니다.<br>chatGPT를 이용해서 현재 날씨를 바탕으로 적당한 메뉴를 5개 추천해 줍니다.|
|   **회원정보 수정**   |
|<img src="./gif/회원정보_수정.gif">|
|유저명과 주소에 대한 수정이 가능합니다.|
|   **비밀번호 변경**   |
|<img src="./gif/비밀번호 변경.gif">|
|현재 비밀번호와 새 비밀번호, 새 비밀번호 확인을 입력해서 비밀번호의 수정이 가능합니다.<br>오류 발생시 각 필드에 대한 오류가 표기됩니다.|
|   **회원탈퇴**   |
|<img src="./gif/회원탈퇴.gif">|
|현재 비밀번호를 입력해서 회원탈퇴가 가능합니다.<br>회원의 탈퇴는 회원테이블의 is_active를 False로 변경해서 논리적으로 삭제합니다.|
|   **글 작성**   |
|<img src="./gif/글-작성.gif">|
|제목과 카테고리, 모집인원 및 내용을 가진 게시글을 작성할 수 있습니다.<br>게시글 작성시 django siginal을 통해서 게시글을 위한 채팅방이 생성됩니다.|
|   **글 수정**   |
|<img src="./gif/글-수정.gif">|
|게시글의 삭제기능입니다.|
|   **모집상태 변경 및 삭제**   |
|<img src="./gif/모집상태-변경-및-삭제.gif">|
|모집상태는 인원이 가득차거나, 글의 작성자가 완료 버튼을 선택하면 모집 완료로 변경됩니다.<br>모집완료 상태일때는 새로운 참자가가 채팅방에 참여할 수 없습니다.|
|   **게시판**   |
|<img src="./gif/게시판.gif">|
|게시판에서는 음식카테고리별로 필터링이 가능합니다.<br>또한 django의 paginator 객체를 활용해서 페이지기능을 구현하였고, page 쿼리를 이용해서 페이지의 전환이 가능합니다.<br>표기되는 페이지 버튼에 대한 정보도 백엔드 서버에서 전달됩니다.|
|   **채팅**   |
|<img src="./gif/채팅.gif">|
|django-channels를 이용해서 실시간 채팅이 가능합니다.<br>채팅방에 참여하거나 퇴장할때 메세지가 전달됩니다.<br>각각의 유저는 유저 리스트 옆의 버튼을 이용해서 채팅방에서 나갈 수 있으며, 채팅방의 생성자는 다른 유저를 강퇴할 수 있습니다.<br> 강퇴당한 유저는 해당 채팅방에 다시 참여할 수 없습니다.<br>채팅방이 삭제될 시 websocket을 통해서 4040 code가 전송됩니다.|
|   **에러페이지**   |
|<img src="./img/에러페이지.png">|
|올바르지 않은 요청이 발생할 경우에 에러페이지로 이동됩니다.|

## 🗜 아키텍쳐

### 디렉토리 구조

```
📦mealbuddy-backend
│  .env
│  manage.py
│  README.md
│  requirements.txt
├─chat
│  │  admin.py
│  │  apps.py
│  │  consumers.py
│  │  models.py
│  │  routing.py
│  │  serializer.py
│  │  signal.py
│  │  urls.py
│  │  views.py
│  └─migrations
│     │  0001_initial.py
│     └  0002_initial.py    
├─core
│  │  exceptions.py
│  └─models.py        
├─group_buying_service
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  views.py
│  │  wsgi.py
│  ├─API
│  │  │  openAI.py
│  │  └─ weather.py
│  └─utils
│     │  coordinate_convert.py
│     └─ paginator.py
├─openAPI
│  │  apps.py
│  │  urls.py
│  └─views.py
├─post
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  serializers.py
│  │  signal.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  └─migrations
│     │  0001_initial.py
│     └─0002_initial.py
└─user
   │  admin.py
   │  apps.py
   │  backends.py
   │  managers.py
   │  models.py
   │  permissions.py
   ├─api
   │  │  renderers.py
   │  │  serializers.py
   │  │  urls.py
   │  └─ views.py      
   └─migrations
      └─0001_initial.py
```

## 💡 개발 중 장애 및 극복 방법

### WebSocket 과 JWT

웹 소켓 방식으로 통신을 할 시, 기본적으로 지원하는 미들웨어에서는 세션방식의 인증을 지원하고 있어서, 중간에 JWT를 인증하는 미들웨어를 새로 만들어서 인증을 하도록 로직을 구현했습니다. 하지만 자바스크립트의 WebSocket API 에서는 header를 따로 구성할 수가 없어서 웹소켓 연결 쿼리에 담아서 토큰을 보낸 후 이를 이용하도록 하였는데, 이 부분에서 더 안전한 방법이 없는지 조금 더 공부해가는 과정이 필요할 것 같습니다.

### ASGI 배포과정에서의 문제

채팅기능을 이용하기 위해서 django-channels와 daphne를 이용한 ASGI 프로토콜으로 통신을 하게 되었습니다. runserver 환경에서는 정상적으로 작동하였지만, 실제 배포 환경에서는 daphne를 따로 실행하는 방식으로 구현을 하였는데, daphne가 정상적으로 실행되지 않는 현상이 발생하였습니다.
이를 해결하기 위해서 로그를 확인해보고, 두가지 문제점을 발견했습니다. 
첫번째는 개발을 진행했던 window 환경과는 다르게 EC2의 ubuntu 환경에서는 os.environ.setdefault 명령어가 정상적으로 작동하지 않는 것이었습니다. 이를 해결하기 위해서 docker-compose.yml 파일에서 environ을 설정해주는 방식을 이용하였습니다.
두번째로는 모듈을 import 하는 순서에 문제가 있었습니다. runserver로 개발 서버를 실행할때는 django가 로딩 된 후 asgi application과 daphne가 연결되지만 daphne를 따로 실행 할 경우에는 asgi apllication의 위치에 따라서 모듈을 import 하는데 문제가 생기는 것을 확인했습니다. 이를 해결하기 위해 asgi.py 파일내의 다른 모듈들을 get_asgi_application 메서드가 실행 된 후에 import 되도록 변경하였습니다.

### React 프로젝트의 빌드

docker compose를 이용하면서, nginx가 빌드될 때, mealbuddy-frontend 의 파일들을 이용해서 빌드를 진행한 후에, 생성된 build 폴더를 nginx의 /usr/share/nginx/html 경로에 복사해서 nginx 가 빌드된 리액트 파일을 서빙하도록 구현하려고 하였으나, 이렇게 진행할 경우 빌드에 너무나도 긴 시간이 걸리고, 중간에 EC2 인스턴스가 멈춰버리는 문제가 발생하였습니다. 
문제의 원인을 찾기 위해서 ubuntu에서 top 명령어를 이용해보니, nginx의 빌드 명령이 실행되면 docker-compose가 메모리를 전부 차지하는것을 알게 되었습니다.
이를 해결하기 위해서 로컬환경에서 빌드한 이후에, nginx의 빌드 명령이 실행될때는 빌드된 정적 파일을 복사만 하는 구조로 변경하였습니다. 추후에는 EC2 인스턴스의 사양을 업그레이드하거나, 다른 더 효율적인 빌드 방법을 확인해보고 적용해보는 과정이 필요할 것 같습니다.

## 💡추가 및 리서치 하고 싶은 기능

1. 결제금액을 충전 및 포인트 적립 시스템 추가.  
    중개 역할을 넘어서, 배달에 필요한 금액을 미리 지불해서 배달 공동 구매 서비스가 원할하게 진행될 수 있도록 하고 싶습니다.  
    
2. 배달음식을 넘어서 동네 주민들간의 여가생활 커뮤니티를 연결.  
    같은 지역 주민들 끼리 이용할 수 있는 서비스인 만큼, 커뮤니티 기능을 더 추가해서 동네간의 정보도 공유할 수 있는 서비스로 만들고 싶습니다.  

3. 모바일 서비스 지원  
    현재 페이지는 반응형을 지원하지 않는데, 서비스의 특성 상 모바일환경에 더 적합하므로, 모바일도 지원하도록 서비스를 변경하고 싶습니다.  

4. 프로필 테이블을 분리하고 기능 추가.  
    프로필 테이블을 분리해서 사용자의 성별등의 추가적인 정보를 받아서 메뉴추천등의 기능에 사용할 수 있도록 하고, 프로필 이미지를 추가해서 S3등의 외부 저장소를 이용하는 기능도 추가하고 싶습니다.  

5. 웹소켓을 이용한 참여한 채팅리스트 기능 및 업데이트 알림기능 추가.  
    채팅 서비스인 만큼, 현재 참여한 채팅리스트 기능과, 채팅이 업데이트 되면 알림이 되는 기능을 추가할 예정입니다.  
    ChatRoomJoin 테이블을 이용해서 채팅방이 업데이트 되었다는 상태를 저장하고, 채팅리스트를 관리하는 웹소켓과 django siginal기능을 이용해서 관리하는 로직으로 고려하고 있습니다.  

6. 소셜 로그인 추가 및 JWT 로그인방식 고도화.  
    현재 로그인기능은 PyJWT를 이용해서 access token 만 발급하는 형태인데, simple_jwt를 이용해서 access, refresh token을 모두 관리하는 방식으로 바꾸고, oAuth등의 추가적인 패키지를 이용한 소셜로그인 기능의 추가도 고려하고 있습니다.

 ## 💡 후기

- 김바름
  > Channels를 이용한 web socket 통신이나, docker를 이용한 배포과정 등을 처음 경험해봤는데, 작업과정에서 발생하는 관련 오류를 수정해가면서 channels나 docker에 대해서도 이해할 수 있는 좋은 기회였습니다. 또한 팀프로젝트에서 각자의 코드작성 예상시간과 실제시간의 차이가 많이 나서, 전체적인 일정이 복잡해졌는데, 이러한 관리의 중요성에 대해서도 알 수 있었습니다. 그리고 협업에서 branch 전략을 제대로 이용해본것은 처음인데, 머지과정에서 발생하는 충돌을 해결해보고, 풀 리퀘스트의 코드를 보고 서로 의견을 주고받는것도 정말 좋은 경험이었습니다.
- 김범석
  > JWT를 이용해 토큰을 관리하는 것을 이해하는 것이 조금 어려웠었고, 팀프로젝트로 협업하는 것이 처음이라 서투르다보니 문제점이 많았었습니다.  
  > 다른 팀원들에게 정말 많이 배웠고 제대로 팀프로젝트를 진행한 것이 처음이라서 새로운 경험을 할 수 있었습니다. 이를 통해 django drf와 git을 다루는 데에 익숙해져서 스스로가 조금 더 성장한 시간이었습니다.
- 류형환
  > 프론트가 없는 상태에서 기능만 개발하다 보니 기능이 완성되어도 데이터가 정상적으로 주고받고 데이터 처리를 확인하는 작업이 어색하여 어려웠습니다.  
  > drf가 무엇인지 조금이나마 아는 시간이 되었고 깃허브를 이용하여 팀과 협업을 한 경우가 이번이 처음이었는데 깃허브를 다루는 게 조금이나마 익숙해지는 시간이었던 거 같습니다.
- 임동성
  > 로그인과정에서의 token개념에 대해서 이해가 어려웠었고 django에 대해서 익숙해 지기가 어려웠습니다.  
  > 협업의 중요성에 대해서 깨닫게 되고 drf에서 사용되는 Serializer의 구조에 대해서 좀 더 직관적으로 알게되었습니다.
