import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return BeautifulSoup(res.text, "lxml")


def print_news(index, title, link):
    print("{} {} ".format(index + 1, title))
    print(" (링크 : {})".format(link))


def scrape_weather():
    print(" <오늘의 날씨>")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    info_data = soup.find("div", attrs={"class": "info_data"})
    today_temp = info_data.find("span", attrs={"class": "todaytemp"}).get_text()
    cast_txt = info_data.find("p", attrs={"class": "cast_txt"}).get_text()
    min_temp = info_data.find("span", attrs={"class": "min"}).get_text()
    max_temp = info_data.find("span", attrs={"class": "max"}).get_text()

    morning_rain_rate = soup.find("span", attrs={"class": "point_time morning"}).find("span", attrs={"class": "rain_rate"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).find("span", attrs={"class": "rain_rate"}).get_text().strip()

    sub_info = soup.find("div", attrs={"class": "sub_info"}).find_all("dd")
    fine_dust_info = sub_info[0].get_text()
    ultra_dust_info = sub_info[0].get_text()

    print(cast_txt)
    print(f"현재 {today_temp}도 (최저 {min_temp} 최고 {max_temp})")
    print(f"오전 {morning_rain_rate} / 오후 {afternoon_rain_rate}")
    print(f"미세먼지 {fine_dust_info} / 초미세먼지 {ultra_dust_info}")


def scrape_headline_new():
    print(" <헤드라인 뉴스>")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3)
    for i, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(i, title, link)
    print()


def scrape_it_news():
    print(" <IT 뉴스>")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    a_idx = 0
    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)
    for i, news in enumerate(news_list):
        img = news.find("img")
        if img:
            a_idx = 1  # img 태그가 있으면 1번째 a tag 사용하고 img 가 없으면 첫번째 a tag 사용
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find_all("a")[a_idx]["href"]
        print_news(i, title, link)
    print()


def scrape_english():
    print(" <오늘의 영어회화>")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
    print("영어지문")
    for sentence in sentences[len(sentences)//2:]:  # 영어먼저 가저와 //는 나누기때 몫 만 가저옴
        print(sentence.get_text().strip())

    print()
    print("한글지문")
    for sentence in sentences[:len(sentences)//2]:  # 0 ~ 반까지 가저와 //는 나누기때 몫 만 가저옴
        print(sentence.get_text().strip())
        

if __name__ == "__main__":
    scrape_weather()
    scrape_headline_new()
    scrape_it_news()
    scrape_english()