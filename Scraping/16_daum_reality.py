import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EA%B4%91%EB%AA%85%ED%95%B4%EB%AA%A8%EB%A1%9C&o=1&q=%EA%B4%91%EB%AA%85+%ED%95%B4%EB%AA%A8%EB%A1%9C%EC%9D%B4%EC%97%B0%EC%95%84%ED%8C%8C%ED%8A%B8"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

titles = ["거래 : ", "면적 : ", "가격 : ", "동 : ", "층 : "]
rows = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")
for i, row in enumerate(rows):
    columns = row.find_all("div", attrs={"class": "txt_ac"})

    print("=" * 10, f"매물 {i + 1}", "=" * 10)
    print("거래 :", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip())
    print("가격 :", columns[2].get_text().strip())
    print("동 : ", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())
