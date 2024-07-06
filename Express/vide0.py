from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from baidu_Interface.text_find import text_get
from baidu_Interface.text_find import num_get
class Video(QThread):
    send = pyqtSignal(int, int, int, bytes,int,str)
    def __init__(self,video_id):
        super().__init__()
        self.th_id = 0
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        if video_id == 'data/vd2.mp4':
            self.th_id = 2
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)

    def run(self):
        while True:
            ret, frame = self.dev.read()
            if self.th_id == 1:
                frame, num = text_get(frame)
            if self.th_id == 2:
                frame, num = num_get(frame)    
            if not ret:
                print('no')
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes,self.th_id,num)
            QThread.usleep(10000)



