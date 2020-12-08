import cv2
import tensorflow.keras
import numpy as np
import winsound as ws
import AI.get_mask_sub as kakao


# 이미지 전처리
def pre_processing(_frame):
    # resize
    size = (224, 224)
    frame_resized = cv2.resize(_frame, size, interpolation=cv2.INTER_AREA)

    # 이미지정규화
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 - 예측을 위해 reshape 해줍니다.
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

    return frame_reshaped


# Load the model
model = tensorflow.keras.models.load_model("resources/keras_model.h5")

# 카메라 캡쳐 객체, 0=내장 카메라
capture = cv2.VideoCapture(0)

# 캡쳐 프레임 사이즈 조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
no_mask = 0
while True:
    ret, frame = capture.read()
    if ret:
        # 이미지 뒤집기
        frame_fliped = cv2.flip(frame, 1)

        # 이미지 출력
        cv2.imshow("VideoFrame", frame_fliped)

    # 1초마다 검사하며, video frame 창으로 아무 키나 누르게 되면 종료
    if cv2.waitKey(200) > 0:
        break

    # 데이터 전처리
    preprocessed = pre_processing(frame_fliped)

    # 예측
    # [[0.00533728 0.99466264]]
    # 마스크 안씀     마스크 씀
    prediction = model.predict(preprocessed)
    # print(prediction)

    if prediction[0, 0] < prediction[0, 1]:
        no_mask += 1
        # 10초간 지속되면
        if no_mask % 10 == 0:
            print('##### 미착용 #####')
            no_mask = 0
            ws.PlaySound("*", ws.SND_NOSTOP)
            kakao.send_music_link()
            # send_message()
        # if sleep_cnt % 30 == 0:
        #     sleep_cnt = 1
        #     print('30초간 졸고 있네요!!!')
        #     # beepsound()
        #     # send_music_link()
        #     break  ## 1번만 알람이 오면 프로그램을 정지 시킴 (반복을 원한다면, 주석으로 막기!)
    else:
        print('마스크 착용중')

# 카메라 객체 반환
capture.release()
# 화면에 나타난 윈도우들을 종료
cv2.destroyAllWindows()
