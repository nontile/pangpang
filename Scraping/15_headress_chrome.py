import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# User-Agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36")

browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)


def get_scroll_height():
    return browser.execute_script("return document.body.scrollHeight")


def scroll_bottom():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


interval = 2  # 2 초에 한번씩 스크롤 내리기
prev_height = get_scroll_height()
while True:
    scroll_bottom()
    time.sleep(interval)
    curr_height = get_scroll_height()
    # print(f"previou: {prev_height}, current: {curr_height}")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print(" <스크롤 완료>")

browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
for i, m in enumerate(movies):
    title = m.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    link = "https://play.google.com" + m.find("a", attrs={"class": "JC71ub"})["href"]
    print(i + 1, title, link)

time.sleep(2)
browser.quit()
