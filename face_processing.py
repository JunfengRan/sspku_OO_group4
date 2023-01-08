# face_processing.py
import cv2
import numpy as np
import os


class FaceProcessing(object):
    def __init__(self):
        self.file = os.path.join(os.path.join(os.path.dirname(__file__), "data"),
                                 "haarcascade_frontalface_alt.xml")
        self.face_cascade = cv2.CascadeClassifier(self.file)

    def face_detection(self, image):
        # 将图像转换为 OpenCV 格式
        image_array = np.asarray(bytearray(image), dtype=np.uint8)
        img_opencv = cv2.imdecode(image_array, -1)
        output = []
        # 检测人脸并构建返回值
        gray = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
        for face in faces:
            # 返回检测框坐标
            x, y, w, h = face.tolist()
            face = {"box": [x, y, x + w, y + h]}
            output.append(face)
            print(face)
        # 返回结果
        return output

    def face_detection_without_transfer(self, image):
        # 图像已经是OpenCV格式
        img_opencv = image
        output = []
        # 检测人脸并构建返回值
        gray = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
        for face in faces:
            # 返回检测框坐标
            x, y, w, h = face.tolist()
            face = {"box": [x, y, x + w, y + h]}
            output.append(face)
            print(face)
        # 返回结果
        return output
