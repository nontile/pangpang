import json
import requests


with open('d:\\workspaces\\kakao_access.txt', "r") as f:
    kakao_access = json.load(f)
    rest_api_app_key = kakao_access['rest_api_app_key']

token_refresh_data = {
    "grant_type": "refresh_token",
    "client_id": rest_api_app_key,
    "refresh_token": "biDwiAtGHdeBtfuZ199lgkqLa-qszdL-gSFQtgorDKcAAAF2HQsIvg"  # <refresh token을 입력하세요>
}

token_url = "https://kauth.kakao.com/oauth/token"
logout_url = "https://kapi.kakao.com/v1/user/logout"
send_msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


def get_access_token(url, data):
    res= requests.post(url, data=data)
    return res.json().get("access_token")


def send_message(template):
    access_token = get_access_token(token_url, token_refresh_data)
    headers = {
        "Authorization": "Bearer " + access_token
    }

    data = {
        "template_object": json.dumps(template)
    }

    res = requests.post(send_msg_url, data=data, headers=headers)
    print(res.status_code)
    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))


if __name__ == "__main__":
    _template = {
        "object_type": "list",
        "header_title": "마스크 사용",
        "header_link": {
            "web_url": "ncov.mohw.go.kr/",
            "mobile_web_url": "ncov.mohw.go.kr/"
        },
        "contents": [
            {
                "title": "마스트",
                "description": "마스크 써야 합니다.",
                "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": "https://www.youtube.com/watch?v=dnjNhcMsT1c",
                    "mobile_web_url": "https://www.youtube.com/watch?v=dnjNhcMsT1c"
                }
            },
            {
                "title": "2. 그림2",
                "description": "그림2 입니다.",
                "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
                }
            }
        ],
        "buttons": [
            {
                "title": "질병관리본부",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
                }
            }
        ]

    }

    send_message(_template)