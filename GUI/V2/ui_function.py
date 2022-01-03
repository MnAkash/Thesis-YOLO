###########################################################################################
###                        CODE:       WRITTEN BY: M.M.Akash December 27 2021           ###
###                        PROJECT:    Yolo Based Polyp Detection                       ###
###                        PURPOSE:    Undergrad Thesis                                 ###
###                                    BASED ON QT DESIGNER, PySide2                    ###
###                        USE CASE:   Used by doctors for polyp detection              ###
###                        LICENCE:    MIT OPENSOURCE LICENCE                           ###
###                                                                                     ###
###                            CODE IS FREE TO USE AND MODIFY                           ###
###########################################################################################

###########################################################################################
#                                     DOCUMENTATION                                       #
#                                                                                         #
#                                                                                         #
#  Each line of the code described below is commented well, such as: the purpose of the   #
#  code, its function, returns e.t.c as in certain caes: the alternatives to that solul-  #
#  ution, other sources like included PDF document has also the working of the code.      #
#  CSS stylesheet of the buttons are given seperatly in the CSS.txt in the parent folder  #
###########################################################################################

###########################################################################################
#                                       CAUTION                                           #
#  SINCE MOST OF THE WORK IS DONE IN THE QT DESIGNER, YOU WAY NOT SEE THE STYLESHEET HERE #
#  FOR THAT PLEASE REFER THE CSS.txt FILE PROVIDED IN THIS SAME FILE.                     #
#  ALSO AMNY OF THE SETTINGS IS PREDEFINED IN THE QT DESIGNER ITSELF, SO HERE IN THIS FUN-#
#  CTION WHAY HAPPENS AFTER THIS I.E. WHEN THE USER CHANGES THE INPUT STATE, ONLY IS DELT #
#  HERE, SO IF YOU WANT TO MODIFY THE FILE, PLEASE OPEN THE CORRESPONDING .ui FILE IN QT  #
#  DESIGNER AND MADE THE MODIFICATION AND THENY COME BACK HERE TO ADD FUNCTIONALITY TO THE#
#  CHANGES.                                                                               #
########################################################################################### 


from main import * #IMPORTING THE MAIN.PY FILE

from about import *


print("Loading weights...")
Polyp_heavy = YOLO('weights/Polyp_heavy.pt')
Polyp_light = YOLO('weights/Polyp_light.pt')
Cancer_heavy = YOLO('weights/Cancer_heavy.pt')
Cancer_light = YOLO('weights/Cancer_light.pt')
Upper_heavy = YOLO('weights/Upper_heavy.pt')
Upper_light = YOLO('weights/Upper_light.pt')
print("\nWeight loaded!\n")


GLOBAL_STATE = 0 #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
init = False # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_setting', 'bn_cloud'] #BUTTONS IN MAIN TAB  
# setting_buttons = ['bn_setting_contact', 'bn_setting_game', 'bn_setting_clean', 'bn_setting_world'] #BUTTONS IN setting STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    #INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True
    ################################################################################################


    #------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)
    ################################################################################################


    #----> MAXIMISE/RESTORE FUNCTION
    #THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    #THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png")) #CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()
    ################################################################################################


    #----> RETURN STATUS MAX OR RESTROE
    #NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE


    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    #------> TOODLE MENU FUNCTION
    #THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    #ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    #IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE 
    #HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        for each in self.ui.frame_bottom_west.findChildren(QFrame): 
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
            minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth==80:
                extend = maxWidth
                #----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                #-----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            #THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################


    #-----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        #-----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        #----> REMOVE NORMAL TITLE BAR 
        if True:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        #-----> RESIZE USING DRAG                                       THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        self.sizegrip = QSizeGrip(self.ui.frame_drag)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON FUNCTION 
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################


    #----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName=='bn_home':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST 

            elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_bug':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_setting':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
                self.ui.lab_tab.setText("Setting")
                self.ui.frame_setting.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                UIFunction.androidStackPages(self, "page_contact")

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_setting)
                self.ui.lab_tab.setText("About > setting")
                self.ui.frame_setting.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_cloud':
            if self.ui.frame_bottom_west.width()==80 and index!=6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.lab_tab.setText("Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        #ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.
    ########################################################################################################################





    #----> BUTTON IN HOME TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def homeButtonPressed(self, buttonName):
        if buttonName=='pushButton_select':
            # print("pushButton_select")
            weightType = self.ui.comboBox.currentText()
            source = response = QFileDialog.getOpenFileName(
                            parent=self,
                            caption='Select image or video',
                            directory=os.getcwd(),
                            #filter='Images (*.png, *.jpg, *.mp4)'
                        )[0]
            
            #If nothing selected, return empty
            if source == '':
                return 0
            
            isBiopsy = self.ui.checkBox_suggestBiopsy.isChecked()
            isColonoscopy = self.ui.radioButton_colonoscopy.isChecked()

            print(isBiopsy)
            print(source)
            print(weightType)
            print(isColonoscopy)

            if isColonoscopy == True:                   #Doing Colonoscopy

                if isBiopsy == True:                    #Biopsy checked
                    if weightType == 'Heavy':               #heavy
                        Cancer_heavy.Detect(source)         
                    else:                                   #light
                        Cancer_light.Detect(source)
                else:                                   #Biopsy not checked
                    if weightType == 'Heavy':               #heavy
                        Polyp_heavy.Detect(source)
                    else:                                   #light
                        Polyp_light.Detect(source)

            else:                                       #Doing Endoscopy
                if weightType == 'Heavy':               #heavy
                    Upper_heavy.Detect(source)
                else:                                   #light
                    Upper_light.Detect(source)

            outDirectory = 'inference/output/'
            output_Link = outDirectory + source.split("/")[-1]
            
            #if image
            if output_Link[-3:] == 'jpg' or output_Link[-3:] == 'png':
                pixmap = QPixmap(output_Link)
                self.ui.lab_home_main_disc.setPixmap(pixmap)
                _translate = QCoreApplication.translate
                self.ui.lab_home_main_hed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff5500;\">Detected from Image</span></p></body></html>"))
                
            #else if video
            else:
                _translate = QCoreApplication.translate
                self.ui.lab_home_main_hed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff5500;\">Detection from Video</span></p></body></html>"))
                cap = cv2.VideoCapture(output_Link)

                if (cap.isOpened()== False):
                    print("Error opening video stream or file")

                while(cap.isOpened()):
                    # Capture frame-by-frame
                    ret, frame = cap.read()
                    if ret == True:

                        # Display the resulting frame
                        #cv2.imshow('Frame',frame)

                        image = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)

                        qformat = QImage.Format_Indexed8
                        if len(image.shape) == 3:
                            if image.shape[2] == 4:
                                qformat = QImage.Format_RGBA8888
                            else:
                                qformat = QImage.Format_RGB888
                        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
                        outImage = outImage.rgbSwapped()
                        #outImage = image
                        self.ui.lab_home_main_disc.setPixmap(QPixmap.fromImage(outImage))
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break

                    else:
                        break
                cap.release()
                #end video play

        elif buttonName=='pushButton_start':
            self.ui.lab_home_main_disc.clear()
            _translate = QCoreApplication.translate
            self.ui.lab_home_main_hed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ff5500;\">Live Detection</span></p></body></html>"))
            weightType = self.ui.comboBox.currentText()
            isBiopsy = self.ui.checkBox_suggestBiopsy.isChecked()
            isColonoscopy = self.ui.radioButton_colonoscopy.isChecked()
            source = '0'


            if isColonoscopy == True:                   #Doing Colonoscopy

                if isBiopsy == True:                    #Biopsy checked
                    if weightType == 'Heavy':               #heavy
                        Cancer_heavy.Detect(source)         
                    else:                                   #light
                        Cancer_light.Detect(source)
                else:                                   #Biopsy not checked
                    if weightType == 'Heavy':               #heavy
                        Polyp_heavy.Detect(source)
                    else:                                   #light
                        Polyp_light.Detect(source)

            else:                                       #Doing Endoscopy
                if weightType == 'Heavy':               #heavy
                    Upper_heavy.Detect(source)
                else:                                   #light
                    Upper_light.Detect(source)

        elif buttonName=='pushButton_stop':
            print("pushButton_stop")


    #----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE 
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):

        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        #self.ui.lab_home_main_hed.setText("Live Detection")
        #self.ui.lab_home_stat_hed.setText("Selection")

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug
        self.ui.bn_bug_start.clicked.connect(lambda: APFunction.addNumbers(self, self.ui.comboBox_bug.currentText(), True))  

        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        #ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        #########PAGE CLOUD #############
        self.ui.bn_cloud_connect.clicked.connect(lambda: APFunction.cloudConnect(self))
        #self.ui.bn_cloud_clear.clicked.connect(lambda: self.dialogexec("Warning", "Do you want to save the file", "icons/1x/errorAsset 55.png", "Cancel", "Save"))
        self.ui.bn_cloud_clear.clicked.connect(lambda: APFunction.cloudClear(self))

        #########PAGE ANDROID WIDGET AND ITS STACKANDROID WIDGET PAGES
        self.ui.bn_setting_contact.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_contact"))
        self.ui.bn_setting_game.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_game"))
        self.ui.bn_setting_clean.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_clean"))
        self.ui.bn_setting_world.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_world"))
        
        ######Setting > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        self.ui.bn_setting_contact_delete.clicked.connect(lambda: self.dialogexec("Warning", "The Contact Infromtion will be Deleted, Do you want to continue.", "icons/1x/errorAsset 55.png", "Cancel", "Yes"))

        self.ui.bn_setting_contact_edit.clicked.connect(lambda: APFunction.editable(self))

        self.ui.bn_setting_contact_save.clicked.connect(lambda: APFunction.saveContact(self))

        #######Setting > PAGE GAMEPAD >>>>>>>>>>>>>>>>>>>
        self.ui.textEdit_gamepad.setVerticalScrollBar(self.ui.vsb_gamepad)   # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText("Type Here Something, or paste something here")

        ######Setting > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        #NOTHING HERE
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: print("Slider: Horizondal: ", self.ui.horizontalSlider_2.value())) #CHECK WEATHER THE SLIDER IS MOVED OR NOT
        self.ui.checkBox.stateChanged.connect(lambda: self.errorexec("Happy to Know you liked the UI", "icons/1x/smile2Asset 1.png", "Ok")) #WHEN THE CHECK BOX IS CHECKED IT ECECUTES THE ERROR BOX WITH MESSAGE.
        self.ui.checkBox_2.stateChanged.connect(lambda: self.errorexec("Even More Happy to hear this", "icons/1x/smileAsset 1.png", "Ok"))

        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        self.ui.text_about_home.setText(aboutHome)
    ################################################################################################################################


    #-----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE Setting BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE Setting PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE. 
    def androidStackPages(self, page):
        #------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_setting_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_contact)
            self.ui.lab_tab.setText("setting > Contact")
            self.ui.frame_setting_contact.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_game":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_game)
            self.ui.lab_tab.setText("setting > GamePad")
            self.ui.frame_setting_game.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_clean)
            self.ui.lab_tab.setText("setting > Clean")
            self.ui.frame_setting_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_setting.setCurrentWidget(self.ui.page_setting_world)
            self.ui.lab_tab.setText("setting > World")
            self.ui.frame_setting_world.setStyleSheet("background:rgb(91,90,90)")

        #ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE setting STACK PAGE.
    ##############################################################################################################

    
#------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS 
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
#REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE    
class APFunction():
    #-----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    def addNumbers(self, number, enable):
        if enable:
            lastProgress = 0
            for x in range(0, int(number), 1):
                progress = int((x/int(number))*100)
                if progress!=lastProgress:
                    self.ui.progressBar_bug.setValue(progress)
                    lastProgress = progress
            self.ui.progressBar_bug.setValue(100)
    ###########################

    #---> FUNCTION TO CONNECT THE CLOUD USING ADRESS AND RETURN A ERROR STATEMENT
    def cloudConnect(self):
        self.ui.bn_cloud_clear.setEnabled(False)
        textID = self.ui.line_cloud_id.text()
        textADRESS = self.ui.line_cloud_adress.text()
        if textID=='asd' and textADRESS=='1234':
            self.ui.line_cloud_adress.setText("")
            self.ui.line_cloud_id.setText("")
            self.ui.line_cloud_proxy.setText("Connection established")
        else:
            self.errorexec("Incorrect Credentials", "icons/1x/errorAsset 55.png", "Retry")

    def cloudClear(self):
        self.ui.line_cloud_proxy.setText("")
        self.ui.line_cloud_adress.setText("")
        self.ui.line_cloud_id.setText("")

    #-----> FUNCTION IN ACCOUNT OF CONTACT PAGE IN setting MENU
    def editable(self):
        self.ui.line_setting_name.setEnabled(True)
        self.ui.line_setting_adress.setEnabled(True)
        self.ui.line_setting_org.setEnabled(True)
        self.ui.line_setting_email.setEnabled(True)
        self.ui.line_setting_ph.setEnabled(True)

        self.ui.bn_setting_contact_save.setEnabled(True)
        self.ui.bn_setting_contact_edit.setEnabled(False)
        self.ui.bn_setting_contact_share.setEnabled(False)
        self.ui.bn_setting_contact_delete.setEnabled(False)

#-----> FUNCTION TO SAVE THE MODOFOED TEXT FIELD
    def saveContact(self):
        self.ui.line_setting_name.setEnabled(False)
        self.ui.line_setting_adress.setEnabled(False)
        self.ui.line_setting_org.setEnabled(False)
        self.ui.line_setting_email.setEnabled(False)
        self.ui.line_setting_ph.setEnabled(False)

        self.ui.bn_setting_contact_save.setEnabled(False)
        self.ui.bn_setting_contact_edit.setEnabled(True)
        self.ui.bn_setting_contact_share.setEnabled(True)
        self.ui.bn_setting_contact_delete.setEnabled(True)
###############################################################################################################################################################