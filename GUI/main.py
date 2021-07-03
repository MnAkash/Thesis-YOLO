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


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setWindowTitle("Polyp Detector")
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DesktopIcon))
        self.sizeObject = QDesktopWidget().screenGeometry(-1)
        
        #self.setStyleSheet("background-color:rgb(51,51,51);")
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        self.UiComponents()
        #self.resize(840,580)
        self.showFullScreen()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("images/polyp.png")
        painter.drawPixmap(self.rect(), pixmap)


    # method for widgets
    def UiComponents(self):


        # creating a push button
        button1 = QPushButton("Detect with image/video", self)
        button1.setGeometry(int(self.sizeObject.width()/2)-100, int(self.sizeObject.height()/2)-100, 200, 70)# setting geometry of button
        #button1.setStyleSheet("border-radius : 2;border : 2px solid black;");
        button1.clicked.connect(self.gotoImageDetect)# adding action to a button
        #button1.setStyleSheet("background-image : url(images/polyp.png);")# setting image to the button
        
        #button.setIcon(QIcon('logo.png'))
        #self.button.setIconSize(QSize(200, 200))

        # creating a push button
        button2 = QPushButton("Detect Live", self)
        button2.setGeometry(int(self.sizeObject.width()/2)-100, int(self.sizeObject.height()/2)+100, 200, 70)# setting geometry of button
        #button2.setStyleSheet("border-radius : 2; border : 2px solid black;");
        button2.clicked.connect(self.gotoLiveDetect)# adding action to a button
        
        #button1.setStyleSheet("background-image : url(images/polyp.png);")# setting image to the button

        closeBtn = QPushButton(self)
        closeBtn.setGeometry(1280, 30, 50, 48)
        closeBtn.setStyleSheet("border-image : url(images/close50.png);")
        closeBtn.clicked.connect(QCoreApplication.instance().quit)

        

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
        self.setWindowTitle('Window1')
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

        
        suggestBiopsy = QCheckBox("&Suggest Biopsy")
        suggestBiopsy.toggled.connect(self.topGroupBox.setDisabled)

        leftLayout  = QVBoxLayout()
        leftLayout.addSpacing(150)
        leftLayout.addWidget(self.topGroupBox)
        leftLayout.addSpacing(30)
        leftLayout.addWidget(suggestBiopsy)
        leftLayout.addStretch(1)

        widget2 = QLabel("")

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addWidget(widget2)
        layout.addWidget(widget2)
        layout.addWidget(widget2)
        layout.addWidget(widget2)
        self.setLayout(layout)




        selectBtn = QPushButton("Select File", self)
        selectBtn.setGeometry(50, 320, 200, 50)# setting geometry of button
        selectBtn.setFont(QFont('Times', 15))
        #selectBtn.setStyleSheet("border-radius : 2;");
        selectBtn.clicked.connect(self.treatSelectedFile)# adding action to a button

        homeBtn = QPushButton("Home", self)
        homeBtn.setGeometry(50, 390, 200, 50)# setting geometry of button
        selectBtn.setFont(QFont('Times', 15))
        homeBtn.clicked.connect(self.goMainWindow)# adding action to a button


        # pixmap = QPixmap(self.res_location)
        # self.imgLabel.setPixmap(pixmap)



        

        closeBtn = QPushButton(self)
        closeBtn.setGeometry(1280, 30, 50, 48)
        closeBtn.setStyleSheet("border-image : url(images/close50.png);")
        closeBtn.clicked.connect(QCoreApplication.instance().quit)
        self.showFullScreen()
        #self.showMaximized()

    def treatSelectedFile(self):
        # option = self.options.index(self.combo.currentText())
        option = self.combo.currentText()
        response = self.getFilename()
        print(response)
        print(option)

    def getFilename(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select image or video',
            directory=os.getcwd(),
            filter='Images (*.png, *.jpg)'
        )
        return response[0]


    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("images/select_page.png")
        painter.drawPixmap(self.rect(), pixmap)
    def goMainWindow(self):
        self.cams = mainWindow()
        self.cams.show()
        self.close() 
        
    
class Window2(QDialog):
    def __init__(self, value=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
        

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

        closeBtn = QPushButton(self)
        closeBtn.setGeometry(1280, 30, 50, 48)
        closeBtn.setStyleSheet("border-image : url(images/close50.png);")
        closeBtn.clicked.connect(QCoreApplication.instance().quit)
        

        self.imgLabel = QLabel(self)
        self.imgLabel.setGeometry(550, 105, 640, 480)

        self.showMaximized()

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
            print("Done")
        
        
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("images/select_page.png")
        painter.drawPixmap(self.rect(), pixmap)
    
    def startLive(self):
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)  # Create Timer
        self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        self.timer.start(40)  # emit the timeout() signal at x=40ms

    def stopLive(self):
        print("Stop!")
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
        

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

