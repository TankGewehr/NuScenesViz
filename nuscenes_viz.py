from ui.ui_form import Ui_form
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from utils.nuscenes import *

import os 
import numpy as np
import random
import time


class Form(QWidget,Ui_form):

    def __init__(self):
        super(Form,self).__init__()
        self.setupUi(self)
        self.sample={}
        self.data_path=''
        self.img_cache_path=''
        self.load_button.clicked.connect(self._Load)
        self.prev_button.clicked.connect(self._Prev)
        self.lidar_button.clicked.connect(self._Lidar)
        self.rand_button.clicked.connect(self._Rand)
        self.next_button.clicked.connect(self._Next)
        self.exit_button.clicked.connect(self._Clear_and_Exit)

    def _remove_img_cache(self,filepath):
        del_list=os.listdir(filepath)
        for f in del_list:
            file_path=os.path.join(filepath,f)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def show_img(self):
        self.sample=self.nusc.sample[self.num-1]
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_FRONT_LEFT'],out_path=out_path,verbose=False)
        img_width,img_height=self.left_front_label.width(),self.left_front_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.left_front_label.setPixmap(pixmap)
        
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_FRONT'],out_path=out_path,verbose=False)
        img_width,img_height=self.front_center_label.width(),self.front_center_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.front_center_label.setPixmap(pixmap)
        
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_FRONT_RIGHT'],out_path=out_path,verbose=False)
        img_width,img_height=self.right_front_label.width(),self.right_front_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.right_front_label.setPixmap(pixmap)
        
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_BACK_LEFT'],out_path=out_path,verbose=False)
        img_width,img_height=self.left_back_label.width(),self.left_back_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.left_back_label.setPixmap(pixmap)
        
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_BACK'],out_path=out_path,verbose=False)
        img_width,img_height=self.back_label.width(),self.back_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.back_label.setPixmap(pixmap)
        
        
        img_name=time.strftime('%H%M%S')+'.jpg'
        out_path=self.img_cache_path+'/'+img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_BACK_RIGHT'],out_path=out_path,verbose=False)
        img_width,img_height=self.right_back_label.width(),self.right_back_label.height()
        pixmap=QPixmap(out_path).scaled(img_width,img_height)
        self.right_back_label.setPixmap(pixmap)

    def _Load(self):
        self.data_path=QFileDialog.getExistingDirectory(self,"选取数据集文件夹","./")
        if self.data_path!='':
            self.img_cache_path=os.path.join(self.data_path,'img_cache')        
            if not os.path.exists(self.img_cache_path):
                os.makedirs(self.img_cache_path)
            self._remove_img_cache(self.img_cache_path)

            for version in os.listdir(self.data_path):
                if len(version.split('-'))==2 and version[0]=='v':
                    self.version=version
                    break
            self.nusc=NuScenes(version=self.version,dataroot=str(self.data_path))
            self.num=1
            self.show_img()

    def _Prev(self):
        if self.data_path!='':
            self.num-=1
            if(self.num<1):
                self.num=len(self.nusc.sample)
            self.show_img()

    def _Lidar(self):
        if self.data_path!='':
            img_name=time.strftime('%H%M%S')+'.jpg'
            out_path=self.img_cache_path+'/'+img_name
            self.nusc.render_sample_data(
                self.sample['data']['LIDAR_TOP'],
                nsweeps=1,
                underlay_map=True,
                out_path=out_path,
                verbose=False
            )
        
            img_width,img_height=self.back_label.width(),self.back_label.height()
            pixmap=QPixmap(out_path).scaled(img_width,img_height)
            self.back_label.setPixmap(pixmap)

    def _Rand(self):
        if self.data_path!='':
            self.num=random.randint(1,len(self.nusc.sample))
            self.show_img()
    
    def _Next(self):
        if self.data_path!='':
            self.num+=1
            if(self.num>len(self.nusc.sample)):
                self.num=1
            self.show_img()

    def _Clear_and_Exit(self):
        if self.data_path!='':
            self._remove_img_cache(self.img_cache_path)
            os.removedirs(self.img_cache_path)
        self.close()

if __name__ == '__main__': 
    app=QApplication(sys.argv)
    ui=Form()
    ui.show()
    sys.exit(app.exec_())

