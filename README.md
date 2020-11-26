# Python Project
## How to run
- pip install -r requirements.txt
- python <*.py>

## 1. Game using pygame

## 2. GUI using tkinter
1. my_capture.py 실행 -> 캡처화면 10장이 만들어 진다.
2. 포토 합치기 실행 -> 3_option.py

## 3. WEB Scrapping 
### developer guide
pip freeze > requirements.txt

## exe 만들기
1. pip install pyinstaller

2. pyinstaller test.py
- build, dist 폴더 생성
- test.spec 파일 생성

resource_path 를 소스에 추가

pyinstaller -w --add-data 'D:\workspaces\gam\GUI\project\*.png;project' D:\workspaces\gam\GUI\project\3_option.py
pyinstaller -w D:\workspaces\gam\GUI\project\3_option.py
pyinstaller -w -F D:\workspaces\gam\Scraping\18_day_msingleone.py
