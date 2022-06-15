# coding=gbk
# importing cv2 and matplotlid
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import dlib
import multiprocessing as mp
i = 1
detector = dlib.get_frontal_face_detector() #��ȡ����������
font = cv2.FONT_HERSHEY_SIMPLEX
def detect1(color_img):
    #���ؼ���ͼ��
    prediction = DeepFace.analyze(color_img)
    # ���
    cv2.putText(color_img, "emotion:"+prediction['dominant_emotion'], (25, 50), font, 0.7,(225, 255, 255), 2, cv2.LINE_4)
    # ����
    cv2.putText(color_img, "age:"+str(prediction['age']), (25, 100), font, 0.7,(255, 255, 255), 2, cv2.LINE_4)
    # ����
    cv2.putText(color_img, "race:"+prediction['dominant_race'], (25, 150), font,0.7,(255, 255, 255), 2, cv2.LINE_4)
    # �Ա�
    cv2.putText(color_img, "gender:"+prediction['gender'], (25, 200), font, 0.7,(255, 255, 255), 2, cv2.LINE_4)
    gray = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)
    rects = detector(gray)
    for index, face in enumerate(rects):
        # ��ͼƬ�б�ע����������ʾ
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(color_img, (left, top), (right, bottom), (255,182,193), 3)
    return color_img

def img_detect(path):
    img = cv2.imread(path)  # loading image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = detect1(img)
    plt.imshow(img)
    plt.show()


def video_detect(window_name, camera_idx):
    cv2.namedWindow(window_name)
    global i
    # ʵʱ�����������Ȧ
    cap = cv2.VideoCapture(camera_idx)  # 0���ǵ�������ͷ Ҳ����������Ƶ ������Ƶ��ʽֻ����avi��ʽ mp4����ֱ��ת��
    # ������Ƶ����: propId - ���õ���Ƶ����, value - ���õĲ���ֵ
    cap.set(3, 480)
    while cap.isOpened():  # ����ͼ��
        ok, frame = cap.read()
        if not ok:
            break
        faces = detector(frame)
        if len(faces) != 0 :
            frame = detect1(frame)
        else:
            cv2.putText(frame, "No face", (20, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

        cv2.imshow(window_name, frame)
        k = cv2.waitKey(10)

        if k == ord('s'):
            # ��s�Ļ��浽����
            cv2.imwrite("saved/task2_real_time" + str(i) + '.jpg', frame)
            i += 1
            print(cap.isOpened())

        if k == ord('q'): # ��q�˳�����ͷ
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # img_detect("test_img/emo4.jpg")
    video_detect("camera", 0)
