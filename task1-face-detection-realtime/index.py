# coding:utf-8
import cv2
import sys
import numpy as np
import dlib
from PIL import Image

detector = dlib.get_frontal_face_detector()
font = cv2.FONT_HERSHEY_SIMPLEX
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")


def Capture(window_name, camera_idx):
    cv2.namedWindow(window_name)  # 写入打开时视频框的名称
    # 捕捉摄像头
    cap = cv2.VideoCapture(camera_idx)  # camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
    while cap.isOpened():  # 判断摄像头是否打开，打开的话就是返回的是True
        # 读取图像
        ok, frame = cap.read()  # 读取一帧图像，该方法返回两个参数，ok true 成功 false失败，frame一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完ok==flase
        if not ok:  # 如果读取帧数不是正确的则ok就是Flase则该语句就会执行
            break
        gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        faces = detector(frame)
        if len(faces) != 0:
            for i in range(len(faces)):
                landmarks = np.matrix([[p.x, p.y] for p in predictor(gray, faces[i]).parts()])
                for idx, point in enumerate(landmarks):
                    # 68 点的坐标
                    pos = (point[0, 0], point[0, 1])
                    # 利用 cv2.circle 给每个特征点画一个圈，共 68 个
                    cv2.circle(frame, pos, 2, color=(139, 0, 0))
                    # 利用 cv2.putText 写数字 1-68
                    # cv2.putText(frame, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)
            # 人脸数量
            cv2.putText(frame, "faces: " + str(len(faces)), (20, 50), font, 1, (187, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No face", (20, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

        # 显示图像, 显示视频到窗口
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)

        # 键盘按q退出视频
        if c & 0xFF == ord('q'):
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 销毁所有窗口

def videoCapture(video):

    capture = cv2.VideoCapture("./1.mp4")


if __name__ == '__main__':
    Capture("camera", 0)