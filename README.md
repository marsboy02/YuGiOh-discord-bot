# YuGiOh-discord-bot
유희왕 마스터 듀얼 헬퍼 봇입니다.
> 주요 기능
> 1. 우라라 타이밍 조회 (구현)
> 2. 와라시 타이밍 조회 (구현)
> 3. 유희왕 카드 크롤링 기능 (미구현)


## 개발환경
``` 
$ pip install -r requirements.txt // 개발환경 복사
$ python3 main.py // 실행
```

## 파일 설명

- requirement.txt : 봇이 돌아가는 환경 패키지 설정
- runtime.txt : 파이썬 버전 설정 (Heroku 22 version 기준)
- Selenium.py & chromedriver : 카드 서치용 크롤링 파일
- Procfile : Heroku 가동 환경 설정
- Handtrap.py : 우라라 및 와라시 리스트 기능
- functions.py : 코드 모듈화 함수 파일
- 