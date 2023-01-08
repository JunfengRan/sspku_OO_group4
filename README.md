# 面向对象第4组
## 人脸识别
  缺少数据库, 数据处理以及人脸识别代码见face_processing.py.

## 运动检测
  使用光流法进行运动检测以及摄像头移动反馈, 代码见optical_flow.py.

  本仓库给出了一个Demo的结果, 视频来源为http://www.math.cuhk.edu.hk/~rchan/paper/super-resolution/experiments.html. 以视频中间一帧为参考帧, 计算其他帧与参考帧的光流, 尝试使用光流直接还原图像. 部分结果如下.

  ![image](https://github.com/JunfengRan/sspku_OO_group4/blob/main/DEMO.png)

  其对应的latex写法为如下.
```
\begin{figure}[htbp]
	\centering
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatRaw1.jpg}
		\caption{Boat fr=1 图像}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatRaw9.jpg}
		\caption{Boat fr=9 图像}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatRaw17.jpg}
		\caption{Boat fr=17 图像}
	\end{minipage}
	%\qquad
	%让图片换行
	
	\centering
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatPic1.jpg}
		\caption{Boat fr=1 配准后的图像}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatPic9.jpg}
		\caption{Boat fr=9 配准后的图像}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatPic17.jpg}
		\caption{Boat fr=17 配准后的图像}
	\end{minipage}
	%\qquad
	%让图片换行
	
	\centering
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatFlow1.jpg}
		\caption{Boat fr=1 光流可视化图}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatFlow9.jpg}
		\caption{Boat fr=9 光流可视化图}
	\end{minipage}
	\begin{minipage}{0.32\linewidth}
		\centering
		\includegraphics[width=0.9\linewidth]{figures/Nuclear/BoatFlow17.jpg}
		\caption{Boat fr=17 光流可视化图}
	\end{minipage}
\end{figure}
