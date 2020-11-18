import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["onclick"])

# <a href="/mypage/myActivity.nhn" class="Nbtn_upload" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# print(soup.find(attrs={"class": "Nbtn_upload"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 형제
# print(rank2.a.get_text())
# print(rank1.parent) # 부모

# rank2 = rank1.find_next_sibling("li")
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="참교육-3화")
print(webtoon)