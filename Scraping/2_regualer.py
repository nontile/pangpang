import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave

# . : 하나의 문자
# ^ : 문자열 시작
# $ : 문자열 끝
p = re.compile("ca.e")


def print_match(m):
    if m:
        print("m.group()",m.group())
        print("m.string", m.string)
        print("m.start()", m.start())
        print("m.end()", m.end())
        print("m.span()", m.span())
    else:
        print("매치않됨")


# m = p.match("good care")
# m = p.search("good care")
# print_match(m)

list = p.findall("careless cafe")
print(list)

# 1. p = re.compile("ca.e")
# 2. p.match("good care")
# 2. p.search("good care")
# 2. p.findall("careless cafe") # list로 반환