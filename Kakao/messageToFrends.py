import json
import requests

# get_access_code에서 링크에 접속해서 로그인후 code를 발급받아 


authorization_code = "8ORu8gWzP2L5Ah72QV0iacrrncUtILqSeNHAe42JhOQdlbiSH7LiAsTY9oLgnsd2v2-niAo9dRoAAAF2HQp31Q"

with open('d:\\workspaces\\kakao_access.txt', "r") as f:
    kakao_access = json.load(f)
    rest_api_app_key = kakao_access['rest_api_app_key']


token_url = "https://kauth.kakao.com/oauth/token"
logout_url = "https://kapi.kakao.com/v1/user/logout"
send_msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
get_frends_url = "https://kapi.kakao.com//v1/api/talk/friends/message/default/send"

token_request_data = {
    "grant_type": "authorization_code",
    "client_id": rest_api_app_key,
    "redirect_uri": "https://localhost.com",
    "code": authorization_code
}


# 권한코드는 한번만 사용 가능함, 한번 호출이후 refresh 사용
def get_token(url, data):
    res = requests.post(url, data=data)
    return res.json()


def get_access_token(url, data):
    res= requests.post(url, data=data)
    return res.json().get("access_token")


def send_message(url, access_token):
    headers = {
        "Authorization": "Bearer " + access_token
    }
    data = {
        "template_object": json.dumps({"object_type": "text",
                                       "text": "Hello, world!",
                                       "link": {
                                           "web_url": "www.naver.com"
                                       }
                                       })
    }

    res = requests.post(url, headers=headers, data=data)
    print(res.status_code)
    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))


def send_list_message(url, access_token):
    headers = {
        "Authorization": "Bearer " + access_token
    }

    template = {
        "object_type": "list",
        "header_title": "초밥 사진",
        "header_link": {
            "web_url": "www.naver.com",
            "mobile_web_url": "www.naver.com"
        },
        "contents": [
            {
                "title": "1. 그림1",
                "description": "그림1 입니다.",
                "image_url": "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
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
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
                }
            }
        ]

    }

    data = {
        "template_object": json.dumps(template)
    }

    res = requests.post(url, data=data, headers=headers)
    print(res.status_code)
    if res.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))


def get_frends(url, access_token):
    headers = {
        "Authorization": "Bearer " + access_token
    }

    template = {
        "object_type": "list",
        "header_title": "초밥 사진",
        "header_link": {
            "web_url": "www.naver.com",
            "mobile_web_url": "www.naver.com"
        },
        "contents": [
            {
                "title": "1. 그림1",
                "description": "그림1 입니다.",
                "image_url": "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
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
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://www.daum.net"
                }
            }
        ]

    }

    data = {
        "template_object": json.dumps(template)
    }

    res = requests.post(url, data=data, headers=headers)
    print(res.text)


if __name__ == "__main__":
    # tokens = get_token(token_url, token_request_data)
    # print(tokens)

    token_refresh_data = {
        "grant_type": "refresh_token",
        "client_id": rest_api_app_key,
        "refresh_token": "biDwiAtGHdeBtfuZ199lgkqLa-qszdL-gSFQtgorDKcAAAF2HQsIvg"  # <refresh token을 입력하세요>
    }

    access_token = get_access_token(token_url, token_refresh_data)
    get_frends(get_frends_url, access_token=access_token)
    # send_message(send_msg_url, access_token=access_token)
    # send_list_message(send_msg_url, access_token=access_token)
