# YuGiOh-discord-bot
유희왕 마스터 듀얼이라는 게임을 도와주는 디스코드 봇 입니다.

> 주요 기능
> 1. 우라라 타이밍 조회
> 2. 와라시 타이밍 조회
> 3. 유희왕 카드 크롤링 기능 (개발중)


## 개발환경
``` 
$ python3 -r venv .venv
가상환경 세팅
$ source venv/bin/activate
가상환경 실행
$ python3 main.py 
실행
```

## 파일 설명

- requirement.txt : 봇이 돌아가는 환경 패키지 설정
- runtime.txt : 파이썬 버전 설정 (Heroku 22 version 기준)
- Selenium.py & chromedriver : 카드 서치용 크롤링 파일
- Procfile : Heroku 가동 환경 설정
- Handtrap.py : 우라라 및 와라시 리스트 기능
- functions.py : 코드 모듈화 함수 파일

## 패키지 버전
- Selenium 명령어 호환성 문제로 버전 3.141 설정
- Heroku 22 환경으로 python 버전 3.10.5 설정
