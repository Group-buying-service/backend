# 밀버디🍚

## 📖 프로젝트 소개 및 계획이유
---
>높아져 가는 배달비로 인해 배달을 시키는데에 부담이 발생하고,    
최소금액이 존재하여 내가 먹을 양보다 많은 양을 시키게 되고 그로 인해 원하지 않은 많은 음식물 쓰레기와 지출이 발생합니다.   
또한, 알뜰 배달이라는 서비스가 존재하지만 긴 배달시간으로 인해 음식이 식거나 형태가 변형되는 경우가 발생하여 이와 같은 문제로 인해 느끼는 불편함을 해소하고자 계획하였습니다.


## 🕰 개발 기간
---
> 2023.08.17 ~ 2023.09.04

## 🤝 멤버 구성
---
- 김바름 - 
- 김범석 - 
- 류형환 - 
- 임동성 - 

## 📕 시작 가이드
---
Requirements
 - 1
 - 2
 - 3

Installation
```
code
```

## ⚙ 기술 스택
---
뱃지

## 📌 주요 기능
--- 
기능 1    
기능 2    
기능 3

## 🚩 API 명세서
---

## 🚩 API 경로
---
**백엔드**  
|URL|기능|
|---|---|
|`/user/login/`|로그인|
|`/user/logout/`|로그아웃|
|`/user/signup/`|회원가입|
|`/user/delete/`|회원탈퇴|
|`/user/password/change/`|비밀번호 변경|
|`/user/profile/`|프로필 확인 및 수정|
|`/token/refresh/`|JWT 토큰 갱신|
|`/chat/list/`|게시글 목록 및 검색|
|`/chat/list/self/`|자신의 게시글 목록|
|`/chat/detail/<chat_id>/`|채팅페이지|
|`/chat/<chat_id>/update/`|채팅 제목 수정 및 추가질문|
|`/chat/write/`|채팅 페이지 작성|
|`/chat/delete/<chat_id>`|채팅 삭제|
|`/chat/<chat_id>/comment/write/`|댓글 작성|
|`/chat/comment/delete/<comment_id>`|댓글 삭제|
|`/chat/comment/delete/child/<childcomment_id>`|대댓글 삭제(댓글과 같은 뷰)|
|`/chat/comment/update/<comment_id>`|댓글 수정|
|`/chat/comment/update/child/<childcomment_id>`|대댓글 수정(댓글과 같은 뷰)|



## 🖥 화면 구성
---
|   **1**  |   **2**  |
|:----:|:----:|
|이미지|이미지|

## 🗜 아키텍쳐
---
### 디렉토리 구조
```
📦backend
├─ .gitignore
├─ README.md
├─ channels-redis.txt
├─ chat
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ consumers.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ routing.py
│  ├─ serializer.py
│  ├─ signal.py
│  ├─ templates
│  │  └─ chat
│  │     ├─ APIindex.html
│  │     ├─ APIroom.html
│  │     ├─ index.html
│  │     └─ room.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ core
│  ├─ exceptions.py
│  └─ models.py
├─ group_buying_service
│  ├─ API
│  │  ├─ openAI.py
│  │  └─ weather.py
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ utils
│  │  ├─ coordinate_convert.py
│  │  └─ paginator.py
│  ├─ views.py
│  └─ wsgi.py
├─ manage.py
├─ openAPI
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ templates
│  │  └─ openAPI
│  │     └─ index.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ post
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ signal.py
│  ├─ static
│  │  ├─ chat.css
│  │  ├─ common.css
│  │  ├─ list.css
│  │  ├─ login-join.css
│  │  ├─ next.png
│  │  ├─ prev.png
│  │  ├─ table.css
│  │  ├─ view.css
│  │  └─ write.css
│  ├─ templates
│  │  └─ post
│  │     ├─ form_error.html
│  │     ├─ post_detail.html
│  │     ├─ post_edit.html
│  │     ├─ post_form.html
│  │     └─ post_list.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirement.txt
├─ static
│  ├─ chat.css
│  ├─ common.css
│  ├─ list.css
│  ├─ login-join.css
│  ├─ next.png
│  ├─ prev.png
│  ├─ table.css
│  ├─ view.css
│  └─ write.css
├─ templates
│  ├─ base.html
│  └─ index.html
└─ user
   ├─ __init__.py
   ├─ admin.py
   ├─ api
   │  ├─ renderers.py
   │  ├─ serializers.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ apps.py
   ├─ backends.py
   ├─ managers.py
   ├─ migrations
   │  ├─ 0001_initial.py
   │  └─ __init__.py
   ├─ models.py
   ├─ permissions.py
   ├─ templates
   │  ├─ profile.html
   │  ├─ register.html
   │  ├─ updatepassword.html
   │  └─ user_login.html
   └─ tests.py
```

## 💡 후기
---