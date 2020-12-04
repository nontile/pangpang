import requests
import json

# https://kauth.kakao.com/oauth/authorize?client_id=30d11cd1cadd7ad3b817a70c15379720&response_type=code&redirect_uri=https://localhost.com
url = "https://kauth.kakao.com/oauth/token"

# data = {
#     "grant_type": "authorization_code",
#     "client_id": "30d11cd1cadd7ad3b817a70c15379720", # rest_api_app_key
#     "redirect_uri": "https://localhost.com",
#     "code": "Vsb8yzonAjd9D5um4ydXbmaUARItNUqtCKgdbKIh6oEIkJohiZuaLGUykC1sJZYzZ4V1iAorDNIAAAF2G9sBRQ"
# }
#
#
# res = requests.post(url, data=data)
# tokens = res.json()
#
# print(tokens)
#
# # 해당 token들은 계속 사용할 것이므로, 파일에 저장해 둡니다.
# with open("kakao_token.json", "w") as f:
#     json.dump(tokens, f)

# refresh
# re_data = {
#     "grant_type" : "refresh_token",
#     "client_id"  : "30d11cd1cadd7ad3b817a70c15379720",
#     "refresh_token" : "0nA-wIyCi-53yhx-5S7HqXKhvUHrDW8dI6sqdAopyV8AAAF2G9uWGA" #<refresh token을 입력하세요>
# }
# response = requests.post(url, data=re_data)
# print(response.json())
# access_token = response.json().get("access_token")
#
# # logout
# logout_url = "https://kapi.kakao.com/v1/user/logout"
# logout_headers = {
#     "Authorization": "Bearer X2iemz_Pul4AhfzHcomZ2Wnv0vSOxLc_YjVI4QopdSkAAAF2HDQ4SA"
# }
# response = requests.post(logout_url, headers=logout_headers)
# print(response.text)

# url_access_token_info ="https://kapi.kakao.com/v1/user/access_token_info"
# logout_headers = {
#     "Authorization": "Bearer X2iemz_Pul4AhfzHcomZ2Wnv0vSOxLc_YjVI4QopdSkAAAF2HDQ4SA"
# }
# response = requests.get(url_access_token_info, headers=logout_headers)
# print(response.text)
