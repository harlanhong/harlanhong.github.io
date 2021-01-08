#!/usr/bin/env python
# coding=utf-8
import numpy as np
import cv2
from interface import YOLO
from Counter import *
from classification.classifier import classifier as CLASSIFIER
import pdb
from settings import cfg
from xml.etree import ElementTree
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

font = cv2.FONT_HERSHEY_SIMPLEX

names =  cfg.get('CLASSIFICATION','NAMES')
names = np.load(names,allow_pickle=True).tolist()
values = list(names.values())

 
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=4):
    # 判断是否为opencv图片类型
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype('simsun.ttc', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def draw_center_rect(img,w,h):
    alphaReserve = 0.8
    BChannel = 255
    GChannel = 0
    RChannel = 0
    yMin = 0
    yMax = h
    xMin = w//2-20
    xMax = w//2+20
    img[yMin:yMax, xMin:xMax, 0] = img[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
    img[yMin:yMax, xMin:xMax, 1] = img[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
    img[yMin:yMax, xMin:xMax, 2] = img[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    return img
def draw_text(img,nameDict):
    string = ''
    for ctg in values:
        if ctg in nameDict:
            string+='{} : {} \n'.format(ctg,nameDict[ctg])
    # RGB
    img = cv2ImgAddText(img, string, 50, 400, (255, 0, 0), 80)
    return img

def process_img(img,yolo3,counter,classifier):
    
    return img
# 向共享缓冲栈中写入数据:
def write(stack, cam, top: int) -> None:
    """
    :param cam: 摄像头参数
    :param stack: Manager.list对象
    :param top: 缓冲栈容量
    :return: None
    """
    print('Process to write: %s' % os.getpid())
    cap = cv2.VideoCapture(cam)
    while True:
        _, img = cap.read()
        if _:
            stack.append(img)
            # 每到一定容量清空一次缓冲栈
            # 利用gc库，手动清理内存垃圾，防止内存溢出
            if len(stack) >= top:
                del stack[:]
                gc.collect()
# 在缓冲栈中读取数据:
def read(stack,path) -> None:
    print('Process to read: %s' % os.getpid())
    SCALE = 3
    cap = cv2.VideoCapture(path)
    fps=cap.get(cv2.CAP_PROP_FPS) #读取帧率FPS
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/SCALE) #读取宽度
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/SCALE) #读取高度
    size=(width,height) #视频大小
    videoWrite=cv2.VideoWriter('outVideo.avi',cv2.VideoWriter_fourcc(*'mp4v'),fps,size) #初始化写出文件路径 编码解码器 帧率 大小
    
    counter = COUNTER(1440,2560)
    classifier = CLASSIFIER()
    yolo3 = YOLO(weights_path="weight/myolov3_16000.weights",model_def="weight/myolov3.cfg",class_path="weight/my.names")

    while True:
        if len(stack) != 0:
            frame = stack.pop()
            #==========
            h,w,c = frame.shape
            xxyy, cls_conf, cls_pred = yolo3.detect(frame)
            scores,names = [],[]
            for (x1,y1,x2,y2) in xxyy:
                x1 = max(0,x1)
                x2 = min(w,x2)
                y1 = max(0,y1)
                y2 = min(h,y2)
                s,n = classifier.classfy_obj(frame[int(y1):int(y2),int(x1):int(x2)])
                names.append(n)
            Number,countingBoxes,countingNames,namedict = counter.count(xxyy,names)
            img = yolo3.draw(xxyy,frame,(0,0,255),names)
            img = yolo3.draw(countingBoxes,img, (0,255,0),countingNames)
            img = draw_text(img,namedict)
            cv2.putText(img, str(Number), (50, 300), font, 4, (0, 0, 255), 4)
            # show a frame
            img = draw_center_rect(img,w,h)
            #==============
            img = cv2.resize(img,(int(w/SCALE),int(h/SCALE)))
            videoWrite.write(img) #写入视频

            cv2.imshow("capture", img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        videoWrite.release()
        cv2.destroyAllWindows() 
if __name__ == '__main__':
    # 父进程创建缓冲栈，并传给各个子进程：
    path = "zj-12(1).mp4"
    # cap = cv2.VideoCapture(path)
    # fps=cap.get(cv2.CAP_PROP_FPS) #读取帧率FPS
    # width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #读取宽度
    # height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #读取高度
    # size=(width,height) #视频大小
    # videoWrite=cv2.VideoWriter('outVideo.avi',cv2.VideoWriter_fourcc(*'mp4v'),fps,size) #初始化写出文件路径 编码解码器 帧率 大小
    
    
    q = Manager().list()
    # model 
    pw = Process(target=write, args=(q, path, 100))
    pr = Process(target=read, args=(q,path=path))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()

    # 等待pr结束:
    pr.join()

    # pw进程里是死循环，无法等待其结束，只能强行终止:
    pw.terminate()

