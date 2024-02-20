# Kream Crawling Mini Project 

### 1. Selenium, Beautifulsoup을 활용하여 원하는 정보 크롤링
- 카테고리, 상품식별자, 브랜드, 상품명, wish수, 리뷰수, 판매량, 상품이미지링크, 상세페이지링크, 리뷰페이지링크 추출 

### 2. 크롤링한 데이터를 MySQL서버에 저장
- pymysql 이용: product table 생성 및 Insert data

### 3. Flask를 이용하여 웹페이지 만들기
- bootstrap을 이용하여 기본적인 html 구성 : 카테고리(dropdown), 키워드 검색창, 체크박스 등의 form 컴포넌트 추가
- 상품명, 리뷰 누르면 해당 상세페이지로 이동
- jinja2 활용: 조건문에 따른 동적 웹페이지 index.html 구성 
- 필터링 기능
  - 카테고리 또는 입력받은 키워드를 바탕으로 데이터를 필터링함
  - 'get' method를 활용하여 form으로부터 인자를 전달받아 sql서버로부터 필터링된 데이터를 웹페이지에 뿌려줌
- 페이지네이션
  - flask의 paginate를 이용하여 페이지네이션 기능 구현
- 그 외 잡다한 추가 기능: 업데이트 날짜 표시(매일 정해진 시간에 crawling 자동 업데이트 - 추가예정), github 아이콘 누르면 내 github주소 연결

### 4. 완성본
<img width="600" height = "400" src="https://github.com/ark0723/assignment/assets/34089914/efd01bff-be2b-4d1d-9713-35b2be585062">
