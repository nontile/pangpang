import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return BeautifulSoup(res.text, "lxml")


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
    news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li")
    for i, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{} {} ".format(i+1, title))
        print(" (링크 : {})".format(link))
    print()


if __name__ == "__main__":
    # scrape_weather()
    scrape_headline_new()