
names = ["홍길동", "이순신", "전봉준", "뉴턴"]

for name in names:
    with open(f"{name}.txt", "w", encoding="utf8") as f:
        f.write(f"""
안녕하세요? {name}님.

우리회사는 영상 관련 회사입니다.
그래서 {name}님의 영상을 보고 연락합니다.

(주) 나도출판
""")
