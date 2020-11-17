import requests

res = requests.get("https://google.com")

# if res.status_code == requests.codes.ok:
#     print(res.status_code)
# else:
#     print("문제가 생겼습니다.", res.status_code)

res.raise_for_status()
print(res.text)

with open("my_google.html", "w", encoding="utf8") as f:
    f.write(res.text)