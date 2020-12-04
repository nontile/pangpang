import json

with open('d:\\workspaces\\kakao_access.txt', "r") as f:
    kakao_access = json.load(f)
    rest_api_app_key = kakao_access['rest_api_app_key']

url_kakao_oauth = f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_app_key}&response_type=code&redirect_uri=https://localhost.com"

print("아래 링크에 접속해서 access token를 발급받으세요")
print(url_kakao_oauth)