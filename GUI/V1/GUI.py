# -*- coding=utf-8 -*-

__author__ = "Moniruzzaman Akash"
__version__ = "1.00"
__license__ = "GNU GPLv3"


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys, os
import cv2
import keyboard


from detect import YOLO


print("Loading weights...")
normal_heavy = YOLO('weights/normal_heavy.pt')
normal_light = YOLO('weights/normal_light.pt')
biopsy_heavy = YOLO('weights/biopsy_heavy.pt')
biopsy_light = YOLO('weights/biopsy_light.pt')
print("\nWeight loaded!\n")

class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowTitle("Polyp Detector")
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DesktopIcon))
        self.sizeObject = QDesktopWidget().screenGeometry(-1)
        
        #self.setStyleSheet("background-color:rgb(51,51,51);")
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)



        #=====UI components
        
        # creating a push button
        button1 = QPushButton("Detect with image/video", self)
        button1.setMinimumSize(QSize(350, 70))
        button1.setMaximumSize(QSize(350, 70))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(16)
        button1.setFont(font6)
        button1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        button1.setCheckable(False)
        button1.setFlat(True)        
        button1.setGeometry(int(self.sizeObject.width()/2)-150, int(self.sizeObject.height()/2)-100, 200, 70)# setting geometry of button
        button1.clicked.connect(self.gotoImageDetect)# adding action to a button
        


        # creating a push button
        button2 = QPushButton("Detect Live", self)
        button2.setMinimumSize(QSize(350, 70))
        button2.setMaximumSize(QSize(350, 70))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(16)
        button2.setFont(font6)
        button2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        button2.setCheckable(False)
        button2.setFlat(True)   
        button2.setGeometry(int(self.sizeObject.width()/2)-150, int(self.sizeObject.height()/2)+100, 200, 70)# setting geometry of button
        button2.clicked.connect(self.gotoLiveDetect)# adding action to a button

        



        # closeBtn = QPushButton(self)
        # closeBtn.setGeometry(1280, 30, 50, 48)
        # closeBtn.setStyleSheet("border-image : url(images/close50.png);")
        # closeBtn.clicked.connect(QCoreApplication.instance().quit)

        self.setStyleSheet(u"background:rgb(91,90,90);")


        #self.resize(940,680)
        #self.showFullScreen()
        self.showMaximized()
        
    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     painter = QPainter(self)
    #     pixmap = QPixmap("images/polyp.png")
    #     painter.drawPixmap(self.rect(), pixmap)


        

    def gotoImageDetect(self):
        # self.cams = Window1(self.lineEdit1.text())
        self.cams = Window1('Hi')
        self.cams.show()
        self.close()
    # action method
    def gotoLiveDetect(self):
        self.cams = Window2("self.lineEdit1.text()")
        self.cams.show()
        self.close()





class Window1(QDialog):
    def __init__(self, value= None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Detect from ')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))

        self.originalPalette = QApplication.palette()
        
        
        self.options = ('Light', 'Heavy')
        self.combo = QComboBox()
        self.combo.setFixedSize(250,40)
        #self.combo.setFont(QFont('calibri', 12))
        self.combo.addItems(self.options)

        label = QLabel("&Detection Mode:")
        label.setBuddy(self.combo)


        topLayout  = QVBoxLayout()
        topLayout .addWidget(label)
        topLayout .addWidget(self.combo)

        self.topGroupBox = QGroupBox("")
        self.topGroupBox.setLayout(topLayout)

        
        self.suggestBiopsy = QCheckBox("&Suggest Biopsy")
        self.suggestBiopsy.setStyleSheet("""
                                    QCheckBox::indicator {
                                        width:30px;
                                        height:30px;
                                    }
                                QCheckBox {
                                    font-size: 18px;
                                }
                                """)
        #self.suggestBiopsy.setGeometry
        # self.suggestBiopsy.toggled.connect(self.topGroupBox.setDisabled)
        #self.suggestBiopsy.toggled.connect(self.is_biopsy)

       


        selectBtn = QPushButton("Select File", self)
        selectBtn.setObjectName(u"selectBtn")
        selectBtn.setMinimumSize(QSize(200, 40))
        selectBtn.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        selectBtn.setFont(font6)
        selectBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        selectBtn.setCheckable(False)
        selectBtn.setFlat(True)


        #selectBtn.setGeometry(50, 320, 200, 50)# setting geometry of button
        #selectBtn.setFont(QFont('Times', 15))
        #selectBtn.setStyleSheet("border-radius : 2;");
        selectBtn.clicked.connect(self.treatSelectedFile)# adding action to a button


        


        homeBtn = QPushButton("Home", self)
        homeBtn.setObjectName(u"homeBtn")
        homeBtn.setMinimumSize(QSize(200, 40))
        homeBtn.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        homeBtn.setFont(font6)
        homeBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        homeBtn.setCheckable(False)
        homeBtn.setFlat(True)
        
        
        
        #homeBtn.setGeometry(50, 390, 200, 50)# setting geometry of button
        #homeBtn.setFont(QFont('Times', 15))
        homeBtn.clicked.connect(self.goMainWindow)# adding action to a button
        
        
        
        self.outputImageLabel = QLabel(self)
        self.outputImageLabel.setGeometry(700, 105, 640, 480)
        
        

        #=============Layout management=================
        leftLayout  = QVBoxLayout()
        leftLayout.addSpacing(150)
        leftLayout.addWidget(self.topGroupBox)
        leftLayout.addSpacing(30)
        leftLayout.addWidget(self.suggestBiopsy)
        leftLayout.addSpacing(30)
        
        leftLayout.addWidget(selectBtn)
        leftLayout.addWidget(homeBtn)
        leftLayout.addStretch(1)


        vert_divide = QFrame(self)
        vert_divide.setObjectName(u"vert_divide")
        vert_divide.setFrameShape(QFrame.VLine)
        vert_divide.setFrameShadow(QFrame.Sunken)
        
        
        widget2 = QLabel("")

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addSpacing(10)
        layout.addWidget(vert_divide)
        layout.addWidget(widget2)
        layout.addWidget(self.outputImageLabel)
        layout.addWidget(widget2)
        self.setLayout(layout)
        
        
        
        
        
        # pixmap = QPixmap(self.res_location)
        # self.imgLabel.setPixmap(pixmap)


        # closeBtn = QPushButton(self)
        # closeBtn.setGeometry(1280, 30, 50, 48)
        # closeBtn.setStyleSheet("border-image : url(images/close50.png);")
        # closeBtn.clicked.connect(QCoreApplication.instance().quit)
        
        self.setStyleSheet(u"background:rgb(91,90,90);") 
        
        #self.showFullScreen()
        self.showMaximized()
        #self.resize(940,680)
        
        
    def treatSelectedFile(self):
        # option = self.options.index(self.combo.currentText())
        weightType = self.combo.currentText()
        source = self.getFilename()
        
        isBiopsy = self.suggestBiopsy.isChecked()
        
        print(isBiopsy)
        print(source)
        print(weightType)
        
        
        if isBiopsy == True:                    #Biopsy checked
            if weightType == 'heavy':               #heavy
                biopsy_heavy.Detect(source)         
            else:                                   #light
                biopsy_light.Detect(source)
        else:                                   #Biopsy not checked
            if weightType == 'heavy':               #heavy
                normal_heavy.Detect(source)
            else:                                   #light
                normal_light.Detect(source)
        
        outDirectory = 'G:\\University materials\\Thesis-YOLO\\GUI\\V1\\inference\\output\\'
        outImage = outDirectory + source.split("/")[-1]
        print(outImage)
        
        pixmap = QPixmap(outImage)
        self.outputImageLabel.setPixmap(pixmap)
        
        #self.label.resize(800,600)
        
        
        print("Done!")

    def getFilename(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select image or video',
            directory=os.getcwd(),
            filter='Images (*.png, *.jpg)'
        )
        return response[0]


    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     painter = QPainter(self)
    #     pixmap = QPixmap("images/select_page.png")
    #     painter.drawPixmap(self.rect(), pixmap)
    def goMainWindow(self):
        self.cams = mainWindow()
        self.cams.show()
        self.close() 
        
    
class Window2(QDialog):
    def __init__(self, value=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
        
        '''
        self.res_location = 'images/stop.png'
        startBtn = QPushButton("Start", self)
        startBtn.setGeometry(50, 260, 200, 50)# setting geometry of button
        startBtn.setIcon(QIcon('images/start.png'))
        startBtn.setIconSize(QSize(40, 40))
        startBtn.setFont(QFont('Times', 15))
        startBtn.clicked.connect(self.startLive)# adding action to a button

        stopBtn = QPushButton("Stop", self)
        stopBtn.setGeometry(50, 330, 200, 50)
        stopBtn.setIcon(QIcon('images/stop.png'))
        stopBtn.setIconSize(QSize(40, 40))
        stopBtn.setFont(QFont('Times', 15))
        stopBtn.clicked.connect(self.stopLive)

        homeBtn = QPushButton("Home", self)
        homeBtn.setGeometry(50, 400, 200, 50)
        homeBtn.setFont(QFont('Times', 15))
        homeBtn.clicked.connect(self.goMainWindow)
        
        
        vert_divide = QFrame(self)
        vert_divide.setObjectName(u"vert_divide")
        vert_divide.setFrameShape(QFrame.VLine)
        vert_divide.setFrameShadow(QFrame.Sunken)
        

        

        self.imgLabel = QLabel(self)
        self.imgLabel.setGeometry(550, 105, 640, 480)
        '''
        self.options = ('Light', 'Heavy')
        self.combo = QComboBox()
        self.combo.setFixedSize(250,40)
        #self.combo.setFont(QFont('calibri', 12))
        self.combo.addItems(self.options)

        label = QLabel("&Detection Mode:")
        label.setBuddy(self.combo)


        topLayout  = QVBoxLayout()
        topLayout .addWidget(label)
        topLayout .addWidget(self.combo)

        self.topGroupBox = QGroupBox("")
        self.topGroupBox.setLayout(topLayout)

        
        self.suggestBiopsy = QCheckBox("&Suggest Biopsy")
        self.suggestBiopsy.setStyleSheet("""
                                    QCheckBox::indicator {
                                        width:30px;
                                        height:30px;
                                    }
                                QCheckBox {
                                    font-size: 18px;
                                }
                                """)
        #self.suggestBiopsy.setGeometry
        # self.suggestBiopsy.toggled.connect(self.topGroupBox.setDisabled)
        #self.suggestBiopsy.toggled.connect(self.is_biopsy)

       


        startBtn = QPushButton("Start", self)
        startBtn.setObjectName(u"startBtn")
        startBtn.setMinimumSize(QSize(200, 40))
        startBtn.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        startBtn.setFont(font6)
        startBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        startBtn.setCheckable(False)
        startBtn.setFlat(True)
        startBtn.clicked.connect(self.startLive)# adding action to a button




        
        stopBtn = QPushButton("Stop", self)
        stopBtn.setObjectName(u"stopBtn")
        stopBtn.setMinimumSize(QSize(200, 40))
        stopBtn.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        stopBtn.setFont(font6)
        stopBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        stopBtn.setCheckable(False)
        stopBtn.setFlat(True)
        stopBtn.clicked.connect(self.stopLive)# adding action to a button




        homeBtn = QPushButton("Home", self)
        homeBtn.setObjectName(u"homeBtn")
        homeBtn.setMinimumSize(QSize(200, 40))
        homeBtn.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        homeBtn.setFont(font6)
        homeBtn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        homeBtn.setCheckable(False)
        homeBtn.setFlat(True)
        homeBtn.clicked.connect(self.goMainWindow)# adding action to a button
        
        
    
        
        

        #=============Layout management=================
        leftLayout  = QVBoxLayout()
        leftLayout.addSpacing(150)
        leftLayout.addWidget(self.topGroupBox)
        leftLayout.addSpacing(30)
        leftLayout.addWidget(self.suggestBiopsy)
        leftLayout.addSpacing(30)
        
        leftLayout.addWidget(startBtn)
        leftLayout.addWidget(stopBtn)
        leftLayout.addWidget(homeBtn)
        leftLayout.addStretch(1)


        vert_divide = QFrame(self)
        vert_divide.setObjectName(u"vert_divide")
        vert_divide.setFrameShape(QFrame.VLine)
        vert_divide.setFrameShadow(QFrame.Sunken)
        
        
        widget2 = QLabel("")

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addSpacing(10)
        layout.addWidget(vert_divide)
        layout.addWidget(widget2)
        layout.addWidget(widget2)
        layout.addWidget(widget2)
        self.setLayout(layout)
        
        
        self.setStyleSheet(u"background:rgb(91,90,90);")
        
        self.showMaximized()
        #self.resize(940,680)

    def update_frame(self):
        ret, self.image = self.capture.read()
        #print(type(self.image))

        self.displayImage(self.image)

    def displayImage(self, image, window=1):
        """
        :param image: frame from camera
        :param window: number of window
        :return:
        """

        try:
            image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_AREA)
        except:
            print("No cam feed!")
            return

        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        #outImage = image
        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            #self.imgLabel.setScaledContents(True)
            #print("Done")
        
        
    # def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #     painter = QPainter(self)
    #     pixmap = QPixmap("images/select_page.png")
    #     painter.drawPixmap(self.rect(), pixmap)
    
    def startLive(self):
        # self.capture = cv2.VideoCapture(0)
        # self.timer = QTimer(self)  # Create Timer
        # self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        # self.timer.start(40)  # emit the timeout() signal at x=40ms
        
        
        weightType = self.combo.currentText()
        source = '0'
        isBiopsy = self.suggestBiopsy.isChecked()
        
        # print(isBiopsy)
        # print(source)
        # print(weightType)
        
        
        if isBiopsy == True:                    #Biopsy checked
            if weightType == 'heavy':               #heavy
                biopsy_heavy.Detect(source)         
            else:                                   #light
                biopsy_light.Detect(source)
        else:                                   #Biopsy not checked
            if weightType == 'heavy':               #heavy
                normal_heavy.Detect(source)
            else:                                   #light
                normal_light.Detect(source)
        
        

    def stopLive(self):
        #print("Stop!")
        #self.timer.stop()
        #self.capture.release()
        #cv2.destroyAllWindows()
        keyboard.press_and_release('q')

    def goMainWindow(self):
        try:
            self.timer.stop()
        except:
            pass
        self.cams = mainWindow()
        self.cams.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())