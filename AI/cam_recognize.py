import cv2


# 카메라 캡쳐 객체, 0=내장 카메라
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

# 카메라 객체 반환
cap.release()

# 화면에 나타난 윈도우들을 종료
cv2.destroyWindow("video")
