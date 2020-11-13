import time
from PIL import ImageGrab

# time.sleep(5)
#
# for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
#     img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
#     img.save("image{}.png".format(i)) # 파일로 저장(image1.png ~ image10.png)
#     time.sleep(2)

kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)