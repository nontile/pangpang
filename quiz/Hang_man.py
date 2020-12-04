from random import *

questions = ["apple", "banana", "orange", "grape", "strawberry"]
target = choice(questions)
target_cnt = len(target)

sheet = []
for i in range(target_cnt):
    sheet.insert(i, "_")

print(" ".join(sheet))
right_cnt = 0
while True:
    answer = input("알파벳 > ")

    is_right = False
    for i, t in enumerate(target):
        if answer == t:
            sheet[i] = t
            right_cnt += 1
            is_right = True

    if is_right:
        is_right = False
    else:
        print("wrong")

    print(" ".join(sheet))

    if target_cnt == right_cnt:
        print("Success")
        break
