import AI.kakao_utils as ka


def send_music_link():
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
                    "web_url": "ncov.mohw.go.kr/",
                    "mobile_web_url": "ncov.mohw.go.kr/"
                }
            }
        ]
    }

    ka.send_message(_template)
