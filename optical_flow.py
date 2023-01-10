# optical_flow.py
import math
import cv2
import numpy as np
import os
import copy

class OpticalFlow(object):
    # 初始化, len_cap为教师活动区域的长度, cam_dis为摄像头到教师的距离, human_speed为教师移动速度的阈值, 假设此时摄像头已经合理放缩居中, 使得教师检测框占据整个图像高度和宽度的1/2, 假设输出为1920*1080像素, 假设视频帧率为30fps
    def __init(self, len_cap=10, cam_dis=5, human_speed=0.5):
        self.len_cap = len_cap
        self.cam_dis = cam_dis
        self.human_speed = human_speed_threshold
        self.optical_flow_threshold = 64 # 大于此(像素间距)值则认为对应像素点产生了移动, 此处根据上述假设暂时设为64
        self.cam_vertical_pos = 0
        self.cam_horizontal_pos = 0
        self.cam_vertical_limit = np.pi / 4
        self.cam_horizontal_limit = math.atan(len_cap / 2 / cam_dis)

    # 保存图片
    def save_image(self, image, addr, name, num):
        address = addr + name + str(num) + '.jpg'
        cv2.imwrite(address, image)

    # 读取图片
    def read_image(self, addr, name, num):
        address = addr + name + str(num) + '.jpg'
        return cv2.imread(address)

    # 光流可视化
    def show_flow_hsv(self, flow, show_style=1):
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])  # 将直角坐标系光流场转成极坐标系

        hsv = np.zeros((flow.shape[0], flow.shape[1], 3), np.uint8)

        # 光流可视化的颜色模式
        if show_style == 1:
            hsv[..., 0] = ang * 180 / np.pi / 2  # angle弧度转角度
            hsv[..., 1] = 255
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)  # magnitude归到0～255之间
        elif show_style == 2:
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 1] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            hsv[..., 2] = 255

        # hsv转bgr
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return bgr

    # 读取视频并保存图片
    def video_processing(self):
        cap = cv2.VideoCapture(os.path.join(os.path.dirname(__file__), "boat512-r-2.avi"))

        # 摄像头实现方式为
        # cap = cv2.VideoCapture(0)

        video_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        video_fps = cap.get(cv2.CAP_PROP_FPS)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.video_frame = int(round(video_frame))
        self.video_fps = int(round(video_fps))
        self.height = int(round(height))
        self.width = int(round(width))
        print("Video FPS:", video_fps)
        print("Video Frame", video_frame)

        f_index = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            f_index = f_index + 1
            save_image(frame, 'Boat/', 'BoatRaw', f_index)
            print('save image:', f_index)

    # 移动摄像头
    def move_cam(self):
        pass

    # 连续超过某段时间跟丢教师时重置摄像头
    def reset_cam(self):
        pass


# Demo, 以视频中间一帧为参考帧, 计算其他帧与参考帧的光流, 尝试使用光流直接还原图像
# 计算光流也可以封装入类中, 此处为了演示过程将其独立出来
OPT = OpticalFlow()
OPT.video_processing()
img0 = OPT.read_image('Boat/', 'BoatRaw', floor(OPT.video_frame / 2) + 1)
img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# 计算参考帧和每一帧之间的光流
for fr in range(1, 1+OPT.video_frame):
    img = read_image('Boat/', 'BoatRaw', fr)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inst = cv2.optflow.createOptFlow_DeepFlow()
    imgFlow = inst.calc(img0, img, None)

    # 将每一帧移回参考帧的坐标系中并可视化光流
    imgNew = copy.deepcopy(img)
    for i in range(OPT.height):
        for j in range(OPT.width):
            imgNew[np.mod(i-int(np.floor(imgFlow[i, j, 0])), OPT.height), np.mod(j-int(np.floor(imgFlow[i, j, 1])), OPT.width)]\
                = img[i, j]

    save_image(show_flow_hsv(imgFlow, show_style=1), 'Boat/', 'BoatFlow', fr)
    save_image(imgNew, 'Boat/', 'BoatPic', fr)
