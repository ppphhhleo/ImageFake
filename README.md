# Image Forgery 
**内容安全-图像伪造 Lab**   
[Report - MyBlog](https://ppphhhleo.github.io/)  
***
Task1 人脸实时检测，Dlib人脸关键点检测，标注68点  
Task2 人脸表情检测，标注信息  
Task3 人脸识别demo   
Task4 图像伪造，换脸    
Task5 换脸检测 Face-X-Ray  
[Face-X-Ray](git@github.com:neverUseThisName/Face-X-Ray.git)

---
## Task1 人脸关键点实时
Dlib 68关键点检测器
[shape_predictor_68_face_landmarks.dat](https://drive.google.com/file/d/1q1voY8JpRnDMebJzwDdVEl2g1j2ByCun/view?usp=sharing)  

## Task2 人脸表情
需要下载weights，一般保存在C盘user目录./.deepface/weights/，可自行网页下载 保存在自定义文件夹内。    
![emotions](https://raw.githubusercontent.com/ppphhhleo/pictures/main/img_ContentSecurity/emo.jpg)

To Do:
提高实时流畅性，加载模型时检测过程易卡帧

## Task3 人脸识别 
### files
* **./data/data_dlib/** 
[dlib_face_recognition_resnet_model_v1.dat](https://drive.google.com/file/d/1PkgywtSY-_Ji0rS489ouxflQyT8V-rdn/view?usp=sharing)  
[shape_predictor_68_face_landmarks.dat](https://drive.google.com/file/d/1q1voY8JpRnDMebJzwDdVEl2g1j2ByCun/view?usp=sharing)
* **./data/data_faces_from_camera/**  
人脸采集照片库，每个人脸身份对应一个单独的文件夹
* **./data/features_all.csv**
人脸特征，提取128D特征值，构成特征库

### **人脸采集**

```
python 1-get_faces_from_camera.py
```
开启摄像头，采集人脸图像，图片保存至 **./data/data_faces_from_camera/**
### **特征提取**
```
python 2-features_extraction_to_csv.py
```
所有人脸特征保存至 **./data/features_all.csv**
### **识别**
```
python 3-face_reco_from_camera.py
```
实时识别，对比特征库中所有人脸，当匹配到的**最小欧式距离<0.4**，才会显示匹配的姓名，否则识别为“Unknown”

## Task4 change face  
首先基于人脸检测器获取目标人脸的特征点，其次使用普氏分析调整脸部至被操控的人脸角度，再获取目标人脸的遮罩，将遮罩与被操纵的人脸图像叠加，并校正颜色  
* face1 face2 
将图片放置在文件夹内  
* [Drive Download](https://drive.google.com/file/d/1q1voY8JpRnDMebJzwDdVEl2g1j2ByCun/view?usp=sharing)  
放置在文件目录下
PREDICTOR_PATH = "./shape_predictor_68_face_landmarks.dat"


## Task5 Face-X-Ray
### **Source Codes**：
``` 
git clone https://github.com/neverUseThisName/Face-X-Ray
```
### **Dependencies**：
```
pip install numpy, opencv-python, scikit-image, dlib, tqdm, color_transfer.
```
### **“shape_predictor_68_face_landmarks.dat”**
[Drive Download](https://drive.google.com/file/d/1q1voY8JpRnDMebJzwDdVEl2g1j2ByCun/view?usp=sharing)  
将dat文件，放置在文件目录内

### **files**
* database：正常人脸图片全集文件夹
* source：待检测的人脸伪造图片文件夹
* dump：检测结果
* faceBlending.py：main文件

### execute  
```cmd
python .\faceBlending.py -sfp=source -fd=database
```


## References
[1] ["Face X-ray for More General Face Forgery Detection"](https://arxiv.org/pdf/1912.13458.pdf)  
[2] ["DeepFace: Closing the Gap to Human-Level Performance in Face Verification"](https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf?spm=5176.100239.blogcont55892.18.pm8zm1&file=Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf)  
[3] ["普氏分析"](https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem)  
[4] ["face recognition"](git@github.com:coneypo/Dlib_face_recognition_from_camera.git)