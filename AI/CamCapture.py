import cv2


# 카메라
cap = cv2.VideoCapture(0)
# 화면크기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()

    if ret:
        # 이미지 뒤집기, 1 = 좌우 뒤집기
        frame_fliped = cv2.flip(frame, 1)

        # 프레임 출력
        cv2.imshow("VideoFrame", frame_fliped)
        # cv2.imshow("VideoFrame", frame)

    # 1ms 동안 사용자가 키를 누르기를 기다림
    if cv2.waitKey(1) > 0:
        break

        # 카메라 객체 반환
cap.release()

# 화면에 나타난 윈도우들을 종료
cv2.destroyAllWindows()
