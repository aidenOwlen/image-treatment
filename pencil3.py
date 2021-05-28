# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\pencil.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt4 import QtCore, QtGui
import numpy as np
import cv2
import shutil
import time
from PIL import Image,ImageFilter,ImageDraw,ImageFont,ImageOps, ImageEnhance
from PyQt4.QtGui import QImage
from PIL.ImageQt import ImageQt
import numpy.core._methods
import numpy.lib.format
# import image module

from PIL import Image

from PIL import ImageFilter

highThresh  = 0.4
lowThresh       = 0.1


def sobel (img):
    '''
    Detects edges using sobel kernel
    '''
    opImgx      = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)  #detects horizontal edges
    opImgy      = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)  #detects vertical edges
    #combine both edges
    return cv2.bitwise_or(opImgx,opImgy)    #does a bitwise OR of pixel values at each pixel

def sketch(frame):  
    #Blur it to remove noise
    frame       = cv2.GaussianBlur(frame,(3,3),0)
    
    #make a negative image
    invImg  = 255-frame
    
    #Detect edges from the input image and its negative
    edgImg0     = sobel(frame)
    edgImg1     = sobel(invImg)
    edgImg      = cv2.addWeighted(edgImg0,1,edgImg1,1,0)    #different weights can be tried too
    
    #Invert the image back
    opImg               = 255-edgImg
    return opImg

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1335, 875)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 821, 781))
        self.frame.setStyleSheet(_fromUtf8("background:rgba(32, 221, 225, 179);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.theimg = QtGui.QLabel(self.frame)
        self.theimg.setScaledContents(True)
        self.theimg.setGeometry(QtCore.QRect(0, 0, 821, 781))
        self.theimg.setText(_fromUtf8(""))
        self.theimg.setObjectName(_fromUtf8("theimg"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(860, 200, 441, 241))
        self.groupBox.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"color:white;font:bold;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 311, 71))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.ceruza = QtGui.QSlider(self.groupBox_3)
        self.ceruza.setMinimum(0)
        self.ceruza.setMaximum(2)
        self.ceruza.valueChanged.connect(self.Ceruza)
        self.ceruza.setGeometry(QtCore.QRect(20, 30, 271, 22))
        self.ceruza.setOrientation(QtCore.Qt.Horizontal)
        self.ceruza.setObjectName(_fromUtf8("ceruza"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 110, 311, 71))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.kite = QtGui.QSlider(self.groupBox_4)
        self.kite.setGeometry(QtCore.QRect(20, 30, 271, 22))
        self.kite.setOrientation(QtCore.Qt.Horizontal)
        self.kite.setObjectName(_fromUtf8("kite"))
        self.kite.setMinimum(0)
        self.kite.setMaximum(10)
        self.kite.setValue(0)
        self.kite.valueChanged.connect(self.Kite)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(860, 50, 361, 131))
        self.balala = False
        self.groupBox_2.setStyleSheet(_fromUtf8("background:transparent;\n"
"font:bold;\n"
"color:white;font:bold;"))
        self.baloch = False
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.upload = QtGui.QPushButton(self.groupBox_2)
        self.upload.setGeometry(QtCore.QRect(20, 30, 321, 28))
        self.upload.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.upload.setObjectName(_fromUtf8("upload"))
        self.save = QtGui.QPushButton(self.groupBox_2)
        self.save.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.save.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.save.setObjectName(_fromUtf8("save"))

        self.save1 = QtGui.QPushButton(self.groupBox)
        self.save1.setGeometry(QtCore.QRect(340, 50, 93, 28))
        self.save1.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.save1.setObjectName(_fromUtf8("save"))
        self.save1.setText("Save")


        self.reset = QtGui.QPushButton(self.groupBox)
        self.reset.setGeometry(QtCore.QRect(30, 200, 401, 28))
        self.reset.setStyleSheet(_fromUtf8("background-color:rgb(75, 226, 226);\n"
"alternate-background-color: rgb(75, 226, 226);\n"
"color:black;\n"
"font:bold;"))
        self.reset.setObjectName(_fromUtf8("save"))
        self.reset.setText("Reset filters")
        self.reset.clicked.connect(self.Reset)

        self.save1.clicked.connect(self.Save1)

        self.name = QtGui.QLineEdit(self.groupBox_2)
        self.name.setGeometry(QtCore.QRect(120, 73, 221, 22))
        self.name.setStyleSheet(_fromUtf8("background:white;\n"
"color:black;\n"
"font:bold;"))
        self.name.setObjectName(_fromUtf8("name"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1335, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.upload.clicked.connect(self.Upload)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.save.clicked.connect(self.Save)
        self.EN = 0

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pencil sketch", None))
        self.groupBox.setTitle(_translate("MainWindow", "Filters", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Scale Range", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Line Thickness", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image", None))
        self.upload.setText(_translate("MainWindow", "Upload image", None))
        self.save.setText(_translate("MainWindow", "Save image", None))
        self.name.setText(_translate("MainWindow", "name.jpg", None))

    def Reset(self):
        self.balala = False 
        self.THEIMG = Image.open("testmg.png")
        self.image = cv2.imread("testmg.png")
        #self.blurred = cv2.pyrMeanShiftFiltering(self.image,61,91)
        self.gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        self.th,_ = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
        self.theimg.setPixmap(QtGui.QPixmap("testmg.png"))
        self.kite.setValue(0)
        self.ceruza.setValue(0)

    def Save1(self):
        self.SavedMg.save("cere.png")
        self.image = cv2.imread("cere.png")
        #self.blurred = cv2.pyrMeanShiftFiltering(self.image,61,91)
        self.gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        self.th,_ = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    

    def Upload(self):

        file = QtGui.QFileDialog.getOpenFileName()
        imgFileLst  = (file,file)
        
        for imgFile in imgFileLst:
            print (imgFile)
            self.img     = cv2.imread (imgFile,0)
            opImg   = sketch(self.img)   
            
            cv2.waitKey()
            cv2.destroyAllWindows()
            cv2.imwrite("testmg.png", opImg)
        self.theimg.setPixmap(QtGui.QPixmap("testmg.png"))
        self.THEIMG = Image.open("testmg.png")
        self.SavedMg = self.THEIMG
        self.image = cv2.imread("testmg.png")
        #self.blurred = cv2.pyrMeanShiftFiltering(self.image,61,91)
        self.gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        self.th,_ = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
  

    def Ceruza(self):
        self.kite.setValue(0)

        value = self.ceruza.value()

        imageObject = self.THEIMG

        
            

        
        if value == 0:
            
            self.EN = 0
        if value ==1:
           
            imageObject = imageObject.filter(ImageFilter.EDGE_ENHANCE)
      
           
            self.EN = 1
        if value ==2:
           
            imageObject = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)
            
            self.EN = 2

        QtImage1 = ImageQt(imageObject)
        QtImage2 = QtGui.QImage(QtImage1)
        self.pixmap = QtGui.QPixmap(QtImage2)
        self.theimg.setPixmap(self.pixmap)
        self.SavedMg = imageObject

    def Kite(self):
        self.ceruza.setValue(0)
        if self.kite.value() == 0:
            height, width, byteValue = self.image.shape
            byteValue = byteValue * width
            QtImage2 = QtGui.QImage(self.image,width, height, byteValue, QImage.Format_RGB888)
            self.pixmap = QtGui.QPixmap(QtImage2)
            self.theimg.setPixmap(self.pixmap)
            self.tempf = self.image.copy()
        
        
            
        else:
            self.tempf = self.image.copy()
            cv2.drawContours(self.tempf,self.th,-1,(0,0,0),self.kite.value()-1)

          
            #QtImage1 = ImageQt(image)
           
            height, width, byteValue = self.tempf.shape
            byteValue = byteValue * width
            QtImage2 = QtGui.QImage(self.tempf,width, height, byteValue, QImage.Format_RGB888)
            self.pixmap = QtGui.QPixmap(QtImage2)
            self.theimg.setPixmap(self.pixmap)
        self.SavedMg = self.tempf
            


    def Save(self):
        try:
            self.SavedMg.save("tempmg.png")
        except:
            cv2.imwrite("tempmg.png",self.SavedMg)
        
        shutil.copyfile("tempmg.png", "images/"+self.name.text())
        try:
            os.system("images/" + self.name.text())
        except:
            pass

        
   









 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

