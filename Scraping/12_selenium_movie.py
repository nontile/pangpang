# import requests
# from bs4 import BeautifulSoup
#
# url = "https://play.google.com/store/movies/top"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
#            "Accept-Language": "ko-KR,ko"
#            }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})

# print(len(movies))
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())

# for m in movies:
#     title = m.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
#     print(title)

from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)


# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")  # 1920 * 1080
# browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


def get_scroll_height():
    return browser.execute_script("return document.body.scrollHeight")


def scroll_bottom():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


import time

prev_height = get_scroll_height()
interval = 2  # 2 초에 한번씩 스크롤 내리기
while True:
    # 스크롤 맨 밑으로 내림
    scroll_bottom()
    time.sleep(interval)
    curr_height = get_scroll_height()
    print(f"previou: {prev_height}, current: {curr_height}")
    if curr_height == prev_height:
        break

    prev_height = curr_height

time.sleep(3)
browser.quit()
