from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os,toml
from PyQt5.QtGui import QKeyEvent
import sys
import time
import subprocess

class KeyboardLineEdit(QLineEdit):
        clicked= pyqtSignal()
        def __init__(self,widget):
            super().__init__(widget)
        def mousePressEvent(self,QMouseEvent):
            self.clicked.emit()



class Ui_Dialog(QMainWindow):
    

    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1036, 696)
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(90, 640, 211, 41))
        self.save_btn.setObjectName("save_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(700, 640, 191, 41))
        self.exit_btn.setObjectName("exit_btn")
        self.settings_tab = QtWidgets.QTabWidget(Dialog)
        self.settings_tab.setGeometry(QtCore.QRect(0, 0, 1031, 621))
        self.settings_tab.setObjectName("settings_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_texturefilltering = QtWidgets.QLabel(self.tab)
        self.label_texturefilltering.setGeometry(QtCore.QRect(40, 490, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_texturefilltering.setFont(font)
        self.label_texturefilltering.setObjectName("label_texturefilltering")
        self.combobox_aspectratio = QtWidgets.QComboBox(self.tab)
        self.combobox_aspectratio.setGeometry(QtCore.QRect(650, 40, 301, 31))
        self.combobox_aspectratio.setObjectName("combobox_aspectratio")
        self.combobox_aspectratio.addItem("")
        self.combobox_aspectratio.addItem("")
        self.combobox_aspectratio.addItem("")
        self.combobox_aspectratio.addItem("")
        self.combobox_texturefiltering = QtWidgets.QComboBox(self.tab)
        self.combobox_texturefiltering.setGeometry(QtCore.QRect(200, 500, 301, 31))
        self.combobox_texturefiltering.setObjectName("combobox_texturefiltering")
        self.combobox_texturefiltering.addItem("")
        self.combobox_texturefiltering.addItem("")
        self.label_graphicsdevice = QtWidgets.QLabel(self.tab)
        self.label_graphicsdevice.setGeometry(QtCore.QRect(40, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_graphicsdevice.setFont(font)
        self.label_graphicsdevice.setObjectName("label_graphicsdevice")
        self.combobox_graphicsdevice = QtWidgets.QComboBox(self.tab)
        self.combobox_graphicsdevice.setGeometry(QtCore.QRect(200, 40, 301, 31))
        self.combobox_graphicsdevice.setObjectName("combobox_graphicsdevice")
        self.combobox_graphicsdevice.addItem("")
        self.combobox_windowresolution = QtWidgets.QComboBox(self.tab)
        self.combobox_windowresolution.setGeometry(QtCore.QRect(200, 160, 301, 31))
        self.combobox_windowresolution.setObjectName("combobox_windowresolution")
        self.combobox_windowresolution.addItem("")
        self.combobox_windowresolution.addItem("")
        self.combobox_windowresolution.addItem("")
        self.combobox_windowresolution.addItem("")
        self.combobox_windowresolution.addItem("")
        self.combobox_windowresolution.addItem("2560x1440")
        self.combobox_windowresolution.addItem("3840x2160")
        self.combobox_graphicsapi = QtWidgets.QComboBox(self.tab)
        self.combobox_graphicsapi.setGeometry(QtCore.QRect(200, 100, 301, 31))
        self.combobox_graphicsapi.setObjectName("combobox_graphicsapi")
        self.combobox_graphicsapi.addItem("")
        self.combobox_graphicsapi.addItem("")
        self.combobox_graphicsapi.addItem("")
        self.label_shadowresolution = QtWidgets.QLabel(self.tab)
        self.label_shadowresolution.setGeometry(QtCore.QRect(40, 430, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_shadowresolution.setFont(font)
        self.label_shadowresolution.setObjectName("label_shadowresolution")
        self.label_anisotropic = QtWidgets.QLabel(self.tab)
        self.label_anisotropic.setGeometry(QtCore.QRect(40, 360, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_anisotropic.setFont(font)
        self.label_anisotropic.setObjectName("label_anisotropic")
        self.label_aspectratio = QtWidgets.QLabel(self.tab)
        self.label_aspectratio.setGeometry(QtCore.QRect(530, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_aspectratio.setFont(font)
        self.label_aspectratio.setObjectName("label_aspectratio")
        self.combobox_maxfps = QtWidgets.QComboBox(self.tab)
        self.combobox_maxfps.setGeometry(QtCore.QRect(200, 230, 301, 31))
        self.combobox_maxfps.setObjectName("combobox_maxfps")
        self.combobox_maxfps.addItem("")
        self.combobox_maxfps.addItem("")
        self.combobox_maxfps.addItem("")
        self.combobox_maxfps.addItem("")
        self.label_windowsresolution = QtWidgets.QLabel(self.tab)
        self.label_windowsresolution.setGeometry(QtCore.QRect(40, 150, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_windowsresolution.setFont(font)
        self.label_windowsresolution.setObjectName("label_windowsresolution")
        self.label_antialiasing = QtWidgets.QLabel(self.tab)
        self.label_antialiasing.setGeometry(QtCore.QRect(40, 290, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_antialiasing.setFont(font)
        self.label_antialiasing.setObjectName("label_antialiasing")
        self.checkbox_enablemotionblur = QtWidgets.QCheckBox(self.tab)
        self.checkbox_enablemotionblur.setGeometry(QtCore.QRect(650, 240, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkbox_enablemotionblur.setFont(font)
        self.checkbox_enablemotionblur.setObjectName("checkbox_enablemotionblur")
        self.label_maxfps = QtWidgets.QLabel(self.tab)
        self.label_maxfps.setGeometry(QtCore.QRect(40, 220, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_maxfps.setFont(font)
        self.label_maxfps.setObjectName("label_maxfps")
        self.combobox_dof = QtWidgets.QComboBox(self.tab)
        self.combobox_dof.setGeometry(QtCore.QRect(650, 100, 301, 31))
        self.combobox_dof.setObjectName("combobox_dof")
        self.combobox_dof.addItem("Auto")
        self.combobox_dof.addItem("Low")
        self.combobox_dof.addItem("Medium")
        self.combobox_dof.addItem("High")
        self.combobox_dof.addItem("Ultra")
        self.combobox_anisotropic = QtWidgets.QComboBox(self.tab)
        self.combobox_anisotropic.setGeometry(QtCore.QRect(200, 370, 301, 31))
        self.combobox_anisotropic.setObjectName("combobox_anisotropic")
        self.combobox_anisotropic.addItem("")
        self.combobox_anisotropic.addItem("")
        self.combobox_anisotropic.addItem("")
        self.combobox_anisotropic.addItem("")
        self.combobox_anisotropic.addItem("")

        self.combobox_shadowresolution = QtWidgets.QComboBox(self.tab)
        self.combobox_shadowresolution.setGeometry(QtCore.QRect(200, 440, 301, 31))
        self.combobox_shadowresolution.setObjectName("combobox_shadowresolution")
        self.combobox_shadowresolution.addItem("")
        self.combobox_shadowresolution.addItem("")
        self.combobox_shadowresolution.addItem("")
        self.combobox_shadowresolution.addItem("")
        self.combobox_shadowresolution.addItem("")
        self.combobox_shadowresolution.addItem("")
        self.checkbox_enabletransparencyantialiasing = QtWidgets.QCheckBox(self.tab)
        self.checkbox_enabletransparencyantialiasing.setGeometry(QtCore.QRect(530, 300, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkbox_enabletransparencyantialiasing.setFont(font)
        self.checkbox_enabletransparencyantialiasing.setObjectName("checkbox_enabletransparencyantialiasing")
        self.combobox_antialiasing = QtWidgets.QComboBox(self.tab)
        self.combobox_antialiasing.setGeometry(QtCore.QRect(200, 300, 301, 31))
        self.combobox_antialiasing.setObjectName("combobox_antialiasing")
        self.combobox_antialiasing.addItem("")
        self.combobox_antialiasing.addItem("")
        self.combobox_antialiasing.addItem("")
        self.combobox_antialiasing.addItem("")
        self.label_dof = QtWidgets.QLabel(self.tab)
        self.label_dof.setGeometry(QtCore.QRect(530, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_dof.setFont(font)
        self.label_dof.setObjectName("label_dof")
        self.label_graphicsapi = QtWidgets.QLabel(self.tab)
        self.label_graphicsapi.setGeometry(QtCore.QRect(40, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_graphicsapi.setFont(font)
        self.label_graphicsapi.setObjectName("label_graphicsapi")
        self.checkbox_showfps = QtWidgets.QCheckBox(self.tab)
        self.checkbox_showfps.setGeometry(QtCore.QRect(530, 240, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkbox_showfps.setFont(font)
        self.checkbox_showfps.setObjectName("checkbox_showfps")
        self.checkbox_enablevsync = QtWidgets.QCheckBox(self.tab)
        self.checkbox_enablevsync.setGeometry(QtCore.QRect(820, 240, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkbox_enablevsync.setFont(font)
        self.checkbox_enablevsync.setObjectName("checkbox_enablevsync")
        self.checkbox_enablefullscreen = QtWidgets.QCheckBox(self.tab)
        self.checkbox_enablefullscreen.setGeometry(QtCore.QRect(530, 170, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkbox_enablefullscreen.setFont(font)
        self.checkbox_enablefullscreen.setObjectName("checkbox_enablefullscreen")
        self.settings_tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_leftstickup = QtWidgets.QLabel(self.tab_2)
        self.label_leftstickup.setGeometry(QtCore.QRect(50, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_leftstickup.setFont(font)
        self.label_leftstickup.setObjectName("label_leftstickup")
        self.label_leftstickdown = QtWidgets.QLabel(self.tab_2)
        self.label_leftstickdown.setGeometry(QtCore.QRect(50, 90, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_leftstickdown.setFont(font)
        self.label_leftstickdown.setObjectName("label_leftstickdown")
        self.label_leftstickleft = QtWidgets.QLabel(self.tab_2)
        self.label_leftstickleft.setGeometry(QtCore.QRect(50, 150, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_leftstickleft.setFont(font)
        self.label_leftstickleft.setObjectName("label_leftstickleft")
        self.label_leftstickright = QtWidgets.QLabel(self.tab_2)
        self.label_leftstickright.setGeometry(QtCore.QRect(50, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_leftstickright.setFont(font)
        self.label_leftstickright.setObjectName("label_leftstickright")
        self.label_rightstickdown = QtWidgets.QLabel(self.tab_2)
        self.label_rightstickdown.setGeometry(QtCore.QRect(50, 350, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_rightstickdown.setFont(font)
        self.label_rightstickdown.setObjectName("label_rightstickdown")
        self.label_rightstickright = QtWidgets.QLabel(self.tab_2)
        self.label_rightstickright.setGeometry(QtCore.QRect(50, 470, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_rightstickright.setFont(font)
        self.label_rightstickright.setObjectName("label_rightstickright")
        self.label_rightstickleft = QtWidgets.QLabel(self.tab_2)
        self.label_rightstickleft.setGeometry(QtCore.QRect(50, 410, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_rightstickleft.setFont(font)
        self.label_rightstickleft.setObjectName("label_rightstickleft")
        self.label_rightstickup = QtWidgets.QLabel(self.tab_2)
        self.label_rightstickup.setGeometry(QtCore.QRect(50, 290, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_rightstickup.setFont(font)
        self.label_rightstickup.setObjectName("label_rightstickup")
        self.label_xbutton = QtWidgets.QLabel(self.tab_2)
        self.label_xbutton.setGeometry(QtCore.QRect(560, 410, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_xbutton.setFont(font)
        self.label_xbutton.setObjectName("label_xbutton")
        self.label_abutton = QtWidgets.QLabel(self.tab_2)
        self.label_abutton.setGeometry(QtCore.QRect(560, 290, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_abutton.setFont(font)
        self.label_abutton.setObjectName("label_abutton")
        self.label_bbutton = QtWidgets.QLabel(self.tab_2)
        self.label_bbutton.setGeometry(QtCore.QRect(560, 350, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_bbutton.setFont(font)
        self.label_bbutton.setObjectName("label_bbutton")
        self.label_ybutton = QtWidgets.QLabel(self.tab_2)
        self.label_ybutton.setGeometry(QtCore.QRect(560, 470, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_ybutton.setFont(font)
        self.label_ybutton.setObjectName("label_ybutton")
        self.label_lefttrigger = QtWidgets.QLabel(self.tab_2)
        self.label_lefttrigger.setGeometry(QtCore.QRect(560, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_lefttrigger.setFont(font)
        self.label_lefttrigger.setObjectName("label_lefttrigger")
        self.label_righttrigger = QtWidgets.QLabel(self.tab_2)
        self.label_righttrigger.setGeometry(QtCore.QRect(560, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_righttrigger.setFont(font)
        self.label_righttrigger.setObjectName("label_righttrigger")
        self.label_leftbummer = QtWidgets.QLabel(self.tab_2)
        self.label_leftbummer.setGeometry(QtCore.QRect(560, 150, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_leftbummer.setFont(font)
        self.label_leftbummer.setObjectName("label_leftbummer")
        self.label_rightbummer = QtWidgets.QLabel(self.tab_2)
        self.label_rightbummer.setGeometry(QtCore.QRect(560, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_rightbummer.setFont(font)
        self.label_rightbummer.setObjectName("label_rightbummer")
        self.label_startbutton = QtWidgets.QLabel(self.tab_2)
        self.label_startbutton.setGeometry(QtCore.QRect(290, 530, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_startbutton.setFont(font)
        self.label_startbutton.setObjectName("label_startbutton")
        self.lineEdit_leftstickup = KeyboardLineEdit(self.tab_2)
        self.lineEdit_leftstickup.setGeometry(QtCore.QRect(190, 40, 291, 31))
        self.lineEdit_leftstickup.setObjectName("lineEdit_leftstickup")
        self.lineEdit_leftstickdown = KeyboardLineEdit(self.tab_2)
        self.lineEdit_leftstickdown.setGeometry(QtCore.QRect(190, 100, 291, 31))
        self.lineEdit_leftstickdown.setObjectName("lineEdit_leftstickdown")
        self.lineEdit_leftstickright = KeyboardLineEdit(self.tab_2)
        self.lineEdit_leftstickright.setGeometry(QtCore.QRect(190, 220, 291, 31))
        self.lineEdit_leftstickright.setObjectName("lineEdit_leftstickright")
        self.lineEdit_leftstickleft = KeyboardLineEdit(self.tab_2)
        self.lineEdit_leftstickleft.setGeometry(QtCore.QRect(190, 160, 291, 31))
        self.lineEdit_leftstickleft.setObjectName("lineEdit_leftstickleft")
        self.lineEdit_rightstickdown = KeyboardLineEdit(self.tab_2)
        self.lineEdit_rightstickdown.setGeometry(QtCore.QRect(190, 360, 291, 31))
        self.lineEdit_rightstickdown.setObjectName("lineEdit_rightstickdown")
        self.lineEdit_rightstickup = KeyboardLineEdit(self.tab_2)
        self.lineEdit_rightstickup.setGeometry(QtCore.QRect(190, 300, 291, 31))
        self.lineEdit_rightstickup.setObjectName("lineEdit_rightstickup")
        self.lineEdit_rightstickright = KeyboardLineEdit(self.tab_2)
        self.lineEdit_rightstickright.setGeometry(QtCore.QRect(190, 480, 291, 31))
        self.lineEdit_rightstickright.setObjectName("lineEdit_rightstickright")
        self.lineEdit_rightstickleft = KeyboardLineEdit(self.tab_2)
        self.lineEdit_rightstickleft.setGeometry(QtCore.QRect(190, 420, 291, 31))
        self.lineEdit_rightstickleft.setObjectName("lineEdit_rightstickleft")
        self.lineEdit_rightbummer = KeyboardLineEdit(self.tab_2)
        self.lineEdit_rightbummer.setGeometry(QtCore.QRect(680, 220, 291, 31))
        self.lineEdit_rightbummer.setObjectName("lineEdit_rightbummer")
        self.lineEdit_leftbummer = KeyboardLineEdit(self.tab_2)
        self.lineEdit_leftbummer.setGeometry(QtCore.QRect(680, 160, 291, 31))
        self.lineEdit_leftbummer.setObjectName("lineEdit_leftbummer")
        self.lineEdit_righttrigger = KeyboardLineEdit(self.tab_2)
        self.lineEdit_righttrigger.setGeometry(QtCore.QRect(680, 100, 291, 31))
        self.lineEdit_righttrigger.setObjectName("lineEdit_righttrigger")
        self.lineEdit_lefttrigger = KeyboardLineEdit(self.tab_2)
        self.lineEdit_lefttrigger.setGeometry(QtCore.QRect(680, 40, 291, 31))
        self.lineEdit_lefttrigger.setObjectName("lineEdit_lefttrigger")
        self.lineEdit_ybutton = KeyboardLineEdit(self.tab_2)
        self.lineEdit_ybutton.setGeometry(QtCore.QRect(680, 480, 291, 31))
        self.lineEdit_ybutton.setObjectName("lineEdit_ybutton")
        self.lineEdit_xbutton = KeyboardLineEdit(self.tab_2)
        self.lineEdit_xbutton.setGeometry(QtCore.QRect(680, 420, 291, 31))
        self.lineEdit_xbutton.setObjectName("lineEdit_xbutton")
        self.lineEdit_bbutton = KeyboardLineEdit(self.tab_2)
        self.lineEdit_bbutton.setGeometry(QtCore.QRect(680, 360, 291, 31))
        self.lineEdit_bbutton.setObjectName("lineEdit_bbutton")
        self.lineEdit_abutton = KeyboardLineEdit(self.tab_2)
        self.lineEdit_abutton.setGeometry(QtCore.QRect(680, 300, 291, 31))
        self.lineEdit_abutton.setObjectName("lineEdit_abutton")
        self.lineEdit_startbutton = KeyboardLineEdit(self.tab_2)
        self.lineEdit_startbutton.setGeometry(QtCore.QRect(390, 540, 291, 31))
        self.lineEdit_startbutton.setObjectName("lineEdit_startbutton")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(20, 270, 991, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.settings_tab.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.settings_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
       
        Dialog.setWindowTitle(_translate("Dialog", "Unleashed Launcher"))
        self.save_btn.setText(_translate("Dialog", "Save Changes"))
        self.exit_btn.setText(_translate("Dialog", "Exit"))
        self.combobox_graphicsdevice.setItemText(0, _translate("Dialog", "Auto"))
        self.label_texturefilltering.setText(_translate("Dialog", "GI Texture Filtering :"))
        self.combobox_graphicsapi.setItemText(0, _translate("Dialog", "Auto"))
        self.combobox_graphicsapi.setItemText(1, _translate("Dialog", "D3D12"))
        self.combobox_graphicsapi.setItemText(2, _translate("Dialog", "Vulkan"))
        self.combobox_aspectratio.setItemText(0, _translate("Dialog", "Auto"))
        self.combobox_aspectratio.setItemText(1, _translate("Dialog", "Original 4:3"))
        self.combobox_aspectratio.setItemText(2, _translate("Dialog", "4:3"))
        self.combobox_aspectratio.setItemText(3, _translate("Dialog", "16:9"))
        self.combobox_texturefiltering.setItemText(0, _translate("Dialog", "Bilinear"))
        self.combobox_texturefiltering.setItemText(1, _translate("Dialog", "Bicubic"))
        self.label_graphicsdevice.setText(_translate("Dialog", "Graphics Device:"))
        self.combobox_windowresolution.setItemText(0, _translate("Dialog", "640x480"))
        self.combobox_windowresolution.setItemText(1, _translate("Dialog", "800x600"))
        self.combobox_windowresolution.setItemText(2, _translate("Dialog", "1024x768"))
        self.combobox_windowresolution.setItemText(3, _translate("Dialog", "1280x720"))
        self.combobox_windowresolution.setItemText(4, _translate("Dialog", "1920x1080"))
        self.label_shadowresolution.setText(_translate("Dialog", "Shadow Resolution :"))
        self.label_anisotropic.setText(_translate("Dialog", "Anisotropic Filtering :"))
        self.label_aspectratio.setText(_translate("Dialog", "Aspect Ratio :"))
        self.combobox_maxfps.setItemText(0, _translate("Dialog", "30"))
        self.combobox_maxfps.setItemText(1, _translate("Dialog", "60"))
        self.combobox_maxfps.setItemText(2, _translate("Dialog", "120"))
        self.combobox_maxfps.setItemText(3, _translate("Dialog", "144"))
        self.label_windowsresolution.setText(_translate("Dialog", "Window Resolution :"))
        self.label_antialiasing.setText(_translate("Dialog", "Anti-Aliasing"))
        self.checkbox_enablemotionblur.setText(_translate("Dialog", "Enable Motion Blur"))
        self.label_maxfps.setText(_translate("Dialog", "Maximum FPS :"))
        
        self.combobox_anisotropic.setItemText(0, _translate("Dialog", "0"))
        self.combobox_anisotropic.setItemText(1, _translate("Dialog", "2"))
        self.combobox_anisotropic.setItemText(2, _translate("Dialog", "4"))
        self.combobox_anisotropic.setItemText(3, _translate("Dialog", "8"))
        self.combobox_anisotropic.setItemText(4, _translate("Dialog", "16"))

        self.combobox_shadowresolution.setItemText(0, _translate("Dialog", "Original"))
        self.combobox_shadowresolution.setItemText(1, _translate("Dialog", "512"))
        self.combobox_shadowresolution.setItemText(2, _translate("Dialog", "1024"))
        self.combobox_shadowresolution.setItemText(3, _translate("Dialog", "2048"))
        self.combobox_shadowresolution.setItemText(4, _translate("Dialog", "4096"))
        self.combobox_shadowresolution.setItemText(5, _translate("Dialog", "8192"))
        self.checkbox_enabletransparencyantialiasing.setText(_translate("Dialog", "Enable Transparency Anti-Aliasing"))
        self.combobox_antialiasing.setItemText(0, _translate("Dialog", "None"))
        self.combobox_antialiasing.setItemText(1, _translate("Dialog", "2x MSAA"))
        self.combobox_antialiasing.setItemText(2, _translate("Dialog", "4x MSAA"))
        self.combobox_antialiasing.setItemText(3, _translate("Dialog", "8x MSAA"))
        self.label_dof.setText(_translate("Dialog", "Depth Of Field :"))
        
        self.label_graphicsapi.setText(_translate("Dialog", "Graphics API :"))
      
        self.checkbox_showfps.setText(_translate("Dialog", "Show FPS"))
        self.checkbox_enablevsync.setText(_translate("Dialog", "Enable V-Sync"))
        self.checkbox_enablefullscreen.setText(_translate("Dialog", "Enable Full-Screen"))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.tab), _translate("Dialog", "Video Settings"))
        self.label_leftstickup.setText(_translate("Dialog", "Left Stick Up :"))
        self.label_leftstickdown.setText(_translate("Dialog", "Left Stick Down :"))
        self.label_leftstickleft.setText(_translate("Dialog", "Left Stick Left :"))
        self.label_leftstickright.setText(_translate("Dialog", "Left Stick Right :"))
        self.label_rightstickdown.setText(_translate("Dialog", "Right Stick Down :"))
        self.label_rightstickright.setText(_translate("Dialog", "Right Stick Right :"))
        self.label_rightstickleft.setText(_translate("Dialog", "Right Stick Left :"))
        self.label_rightstickup.setText(_translate("Dialog", "Right Stick Up :"))
        self.label_xbutton.setText(_translate("Dialog", "X Button :"))
        self.label_abutton.setText(_translate("Dialog", "A Button :"))
        self.label_bbutton.setText(_translate("Dialog", "B Button :"))
        self.label_ybutton.setText(_translate("Dialog", "Y Button :"))
        self.label_lefttrigger.setText(_translate("Dialog", "Left Trigger :"))
        self.label_righttrigger.setText(_translate("Dialog", "Right Trigger :"))
        self.label_leftbummer.setText(_translate("Dialog", "Left Bummer :"))
        self.label_rightbummer.setText(_translate("Dialog", "Right Bummer :"))
        self.label_startbutton.setText(_translate("Dialog", "Start Button :"))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.tab_2), _translate("Dialog", "Keyboard Remapping"))
        self.save_btn.clicked.connect(self.save_changes)
        self.exit_btn.clicked.connect(self.exit_program)
        self.combobox_antialiasing.currentTextChanged.connect(self.func_antialiasing)

        self.lineEdit_leftstickup.setReadOnly(True)
        self.lineEdit_leftstickdown.setReadOnly(True)
        self.lineEdit_leftstickleft.setReadOnly(True)
        self.lineEdit_leftstickright.setReadOnly(True)
        self.lineEdit_rightstickup.setReadOnly(True)
        self.lineEdit_rightstickdown.setReadOnly(True)
        self.lineEdit_rightstickleft.setReadOnly(True)
        self.lineEdit_rightstickright.setReadOnly(True)
        self.lineEdit_lefttrigger.setReadOnly(True)
        self.lineEdit_leftbummer.setReadOnly(True)
        self.lineEdit_rightbummer.setReadOnly(True)
        self.lineEdit_righttrigger.setReadOnly(True)
        self.lineEdit_abutton.setReadOnly(True)
        self.lineEdit_bbutton.setReadOnly(True)
        self.lineEdit_startbutton.setReadOnly(True)
        self.lineEdit_xbutton.setReadOnly(True)
        self.lineEdit_ybutton.setReadOnly(True)

        self.lineEdit_leftstickup.clicked.connect(partial(self.prompt_values,"leftstickup"))
        self.lineEdit_leftstickdown.clicked.connect(partial(self.prompt_values,"leftstickdown"))
        self.lineEdit_leftstickleft.clicked.connect(partial(self.prompt_values,"leftstickleft"))
        self.lineEdit_leftstickright.clicked.connect(partial(self.prompt_values,"leftstickright"))
        self.lineEdit_rightstickup.clicked.connect(partial(self.prompt_values,"rightstickup"))
        self.lineEdit_rightstickdown.clicked.connect(partial(self.prompt_values,"rightstickdown"))
        self.lineEdit_rightstickleft.clicked.connect(partial(self.prompt_values,"rightstickleft"))
        self.lineEdit_rightstickright.clicked.connect(partial(self.prompt_values,"rightstickright"))
        self.lineEdit_startbutton.clicked.connect(partial(self.prompt_values,"startbutton"))
        self.lineEdit_abutton.clicked.connect(partial(self.prompt_values,"abutton"))
        self.lineEdit_bbutton.clicked.connect(partial(self.prompt_values,"bbutton"))
        self.lineEdit_xbutton.clicked.connect(partial(self.prompt_values,"xbutton"))
        self.lineEdit_ybutton.clicked.connect(partial(self.prompt_values,"ybutton"))
        self.lineEdit_lefttrigger.clicked.connect(partial(self.prompt_values,"lefttrigger"))
        self.lineEdit_leftbummer.clicked.connect(partial(self.prompt_values,"leftbummer"))
        self.lineEdit_righttrigger.clicked.connect(partial(self.prompt_values,"righttrigger"))
        self.lineEdit_rightbummer.clicked.connect(partial(self.prompt_values,"rightbummer"))
        

    def func_antialiasing(self):
        if self.combobox_antialiasing.currentText() == "None":
            self.checkbox_enabletransparencyantialiasing.setChecked(False)
            self.checkbox_enabletransparencyantialiasing.setDisabled(True)
        else:
            self.checkbox_enabletransparencyantialiasing.setDisabled(False)

    def prompt_values(self,value):
        window2.current_key = value
        ui.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        window2.show()

    
        
        
    def init_values(self):
        
        with open(file_path, 'r') as f:
          config_unleashed = toml.load(f)

        import xml.etree.ElementTree as ET

        # Parse the XML file

        dxdiag_xml = ET.parse('gpuspecs.xml')
  
        avaliable_devices = []
        lst = dxdiag_xml.findall('DisplayDevices/DisplayDevice/CardName')
        for gpu in lst:
            avaliable_devices.append(gpu.text)
    
        #Video Settings Variables
        graphics_device = config_unleashed["Video"]["GraphicsDevice"]
        maxfps = config_unleashed['Video']['FPS']
        cur_resolution = f"{config_unleashed['Video']['WindowWidth']}x{config_unleashed['Video']['WindowHeight']}"
        graphics_api = config_unleashed["Video"]["GraphicsAPI"]
        vsync = config_unleashed['Video']['VSync']
        antialiasing = config_unleashed['Video']['AntiAliasing']
        anisotropic = config_unleashed['Video']['AnisotropicFiltering']
        shadow_resolution = config_unleashed['Video']['ShadowResolution']
        gl_texture =  config_unleashed['Video']['GITextureFiltering']
        aspect_ratio = config_unleashed['Video']['AspectRatio']
        depthoffield = config_unleashed['Video']['DepthOfFieldQuality']
        full_screen = config_unleashed['Video']['Fullscreen']
        showfps = config_unleashed['Video']['ShowFPS']
        motion_blur = config_unleashed['Video']['MotionBlur']
        transparency_antialising = config_unleashed['Video']['TransparencyAntiAliasing']

        #Keyboard Input Settings Variables

        left_stick_up = config_unleashed['Bindings']['Key_LeftStickUp']
        left_stick_down = config_unleashed['Bindings']['Key_LeftStickDown']
        left_stick_left = config_unleashed['Bindings']['Key_LeftStickLeft']
        left_stick_right = config_unleashed['Bindings']['Key_LeftStickRight']
        right_stick_up = config_unleashed['Bindings']['Key_RightStickUp']
        right_stick_down = config_unleashed['Bindings']['Key_RightStickDown']
        right_stick_left = config_unleashed['Bindings']['Key_RightStickLeft']
        right_stick_right = config_unleashed['Bindings']['Key_RightStickRight']
        a_button = config_unleashed['Bindings']['Key_A']
        b_button = config_unleashed['Bindings']['Key_B']
        x_button = config_unleashed['Bindings']['Key_X']
        y_button = config_unleashed['Bindings']['Key_Y']
        left_trigger = config_unleashed['Bindings']['Key_LeftTrigger']
        right_trigger = config_unleashed['Bindings']['Key_RightTrigger']
        left_bummer = config_unleashed['Bindings']['Key_LeftBumper']
        right_bummer = config_unleashed['Bindings']['Key_RightBumper']
        start_button = config_unleashed['Bindings']['Key_Start']


        #Set Variables to Init Current Video Settings
        for item_gpu in avaliable_devices:
                self.combobox_graphicsdevice.addItem(item_gpu)
        self.combobox_graphicsdevice.setCurrentText(graphics_device)
      

        self.combobox_maxfps.setCurrentText(str(maxfps))
        self.combobox_graphicsapi.setCurrentText(str(graphics_api))
        self.combobox_shadowresolution.setCurrentText(str(shadow_resolution)) 
        self.combobox_texturefiltering.setCurrentText(str(gl_texture)) 
        self.combobox_antialiasing.setCurrentText(str(antialiasing)) 
        self.combobox_anisotropic.setCurrentText(str(anisotropic)) 
        self.combobox_aspectratio.setCurrentText(str(aspect_ratio)) 
        self.combobox_dof.setCurrentText(str(depthoffield)) 
        self.combobox_windowresolution.setCurrentText(cur_resolution) 

        if antialiasing == "None":
            self.checkbox_enabletransparencyantialiasing.setDisabled(True)
        else:
            self.checkbox_enabletransparencyantialiasing.setDisabled(False)

        if motion_blur == "Off":
            self.checkbox_enablemotionblur.setChecked(False)
        else:
            self.checkbox_enablemotionblur.setChecked(True)

        self.checkbox_showfps.setChecked(showfps)
        self.checkbox_enablefullscreen.setChecked(full_screen)
        self.checkbox_enablevsync.setChecked(vsync)
        self.checkbox_enabletransparencyantialiasing.setChecked(transparency_antialising)

        #Set text to Init Current Keyboard Mappings

        self.lineEdit_leftstickup.setText(left_stick_up)
        self.lineEdit_leftstickdown.setText(left_stick_down)
        self.lineEdit_leftstickleft.setText(left_stick_left)
        self.lineEdit_leftstickright.setText(left_stick_right)

        self.lineEdit_rightstickup.setText(right_stick_up)
        self.lineEdit_rightstickdown.setText(right_stick_down)
        self.lineEdit_rightstickleft.setText(right_stick_left)
        self.lineEdit_rightstickright.setText(right_stick_right)

        self.lineEdit_abutton.setText(a_button)
        self.lineEdit_bbutton.setText(b_button)
        self.lineEdit_xbutton.setText(x_button)
        self.lineEdit_ybutton.setText(y_button)

        self.lineEdit_startbutton.setText(start_button)
        self.lineEdit_lefttrigger.setText(left_trigger)
        self.lineEdit_righttrigger.setText(right_trigger)
        self.lineEdit_leftbummer.setText(left_bummer)
        self.lineEdit_rightbummer.setText(right_bummer)

    def show_info_messagebox(self): 
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
  
    # setting message for Message Box 
        msg.setText("Saved Config") 
      
    # setting Message box window title 
        msg.setWindowTitle("Unleashed Launcher") 
      
    # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok) 
      
    # start the app 
        retval = msg.exec_() 
    
    def show_error_messagebox(self): 
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Critical) 
  
    # setting message for Message Box 
        msg.setText("Error:config.toml is missing or corrupted") 
      
    # setting Message box window title 
        msg.setWindowTitle("Unleashed Launcher") 
      
    # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok) 
      
    # start the app 
        retval = msg.exec_() 

    def exit_program(self):
        app.quit()
    
    def save_changes(self):

        #Variables Text:

        u_graphicsdevice = self.combobox_graphicsdevice.currentText()
        u_graphicsapi = self.combobox_graphicsapi.currentText()
        u_resolution = self.combobox_windowresolution.currentText()
        u_fps = self.combobox_maxfps.currentText()
        u_antialiasing = self.combobox_antialiasing.currentText()
        u_anisotropic = self.combobox_anisotropic.currentText()
        u_shadowresolution = self.combobox_shadowresolution.currentText()
        u_gitexturefiltering = self.combobox_texturefiltering.currentText()
        u_aspectratio = self.combobox_aspectratio.currentText()
        u_dof = self.combobox_dof.currentText()

        u_fullscreen = self.checkbox_enablefullscreen.isChecked()
        u_vsync = self.checkbox_enablevsync.isChecked()
        u_showfps = self.checkbox_showfps.isChecked()
        u_transparencyaa = self.checkbox_enabletransparencyantialiasing.isChecked()


        k_leftstickup = self.lineEdit_leftstickup.text()
        k_leftstickdown = self.lineEdit_leftstickdown.text()
        k_leftstickleft = self.lineEdit_leftstickleft.text()
        k_leftstickright = self.lineEdit_leftstickright.text()
        k_rightstickup = self.lineEdit_rightstickup.text()
        k_rightstickdown = self.lineEdit_rightstickdown.text()
        k_rightstickleft = self.lineEdit_rightstickleft.text()
        k_rightstickright = self.lineEdit_rightstickright.text()
        k_abutton = self.lineEdit_abutton.text()
        k_bbutton = self.lineEdit_bbutton.text()
        k_xbutton = self.lineEdit_xbutton.text()
        k_ybutton = self.lineEdit_ybutton.text()
        k_startbutton = self.lineEdit_startbutton.text()
        k_leftbummer = self.lineEdit_leftbummer.text()
        k_lefttrigger = self.lineEdit_lefttrigger.text()
        k_righttrigger = self.lineEdit_righttrigger.text()
        k_rightbummer = self.lineEdit_rightbummer.text()

        # Save Video Settings on config.toml
        try:
            with open(file_path, 'r') as f:
             config_unleashed = toml.load(f)

            config_unleashed['Video']['GraphicsDevice'] = u_graphicsdevice
            config_unleashed['Video']['GraphicsAPI'] = u_graphicsapi
            config_unleashed['Video']['WindowWidth'] = int(u_resolution.split("x")[0])
            config_unleashed['Video']['WindowHeight'] = int(u_resolution.split("x")[1])
            config_unleashed['Video']['FPS'] = int(u_fps)
            config_unleashed['Video']['AntiAliasing'] = u_antialiasing
            config_unleashed['Video']['AnisotropicFiltering'] = int(u_anisotropic)
            config_unleashed['Video']['ShadowResolution'] = u_shadowresolution
            config_unleashed['Video']['GITextureFiltering'] = u_gitexturefiltering 
            config_unleashed['Video']['AspectRatio'] = u_aspectratio
            config_unleashed['Video']['DepthOfFieldQuality'] = u_dof

            config_unleashed['Video']['Fullscreen'] = u_fullscreen
            config_unleashed['Video']['VSync'] = u_vsync
            config_unleashed['Video']['ShowFPS'] = u_showfps
            config_unleashed['Video']['TransparencyAntiAliasing'] = u_transparencyaa

            if self.checkbox_enablemotionblur.isChecked():
                config_unleashed['Video']['MotionBlur'] = "On"
            else:
                config_unleashed['Video']['MotionBlur'] = "Off"

     # Save Keyboard Mappings on config.toml
     
            config_unleashed['Bindings']['Key_LeftStickUp'] = k_leftstickup
            config_unleashed['Bindings']['Key_LeftStickDown'] = k_leftstickdown
            config_unleashed['Bindings']['Key_LeftStickLeft'] = k_leftstickleft
            config_unleashed['Bindings']['Key_LeftStickRight'] = k_leftstickright
            config_unleashed['Bindings']['Key_RightStickUp'] = k_rightstickup
            config_unleashed['Bindings']['Key_RightStickDown'] = k_rightstickdown
            config_unleashed['Bindings']['Key_RightStickLeft'] = k_rightstickleft
            config_unleashed['Bindings']['Key_RightStickRight'] = k_rightstickright

            config_unleashed['Bindings']['Key_A'] = k_abutton
            config_unleashed['Bindings']['Key_B'] = k_bbutton
            config_unleashed['Bindings']['Key_X'] = k_xbutton
            config_unleashed['Bindings']['Key_Y'] = k_ybutton

            config_unleashed['Bindings']['Key_LeftTrigger'] = k_lefttrigger
            config_unleashed['Bindings']['Key_LeftBumper'] = k_leftbummer

            config_unleashed['Bindings']['Key_Start'] = k_startbutton

            config_unleashed['Bindings']['Key_RightTrigger'] = k_righttrigger
            config_unleashed['Bindings']['Key_RightBumper'] = k_rightbummer
 
        # Write the modified config back to the file
            with open(file_path, 'w') as f:
                toml.dump(config_unleashed, f)
            self.show_info_messagebox()
        
        except:
            self.show_error_messagebox()

    
class MainWindow(Ui_Dialog,QMainWindow):
    
    def closeEvent(self,event):
        print(event)

     
class KeyInputWindow(QMainWindow):
    def __init__(self):
        current_key = None
        super().__init__()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
       
        self.setWindowTitle("Unleashed Launcher")
        self.resize(320,240)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        button = QLabel("  Enter key to change keyboard mappings")
        button.setFont(font)
        self.setCentralWidget(button)

   
   
    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key = event.key()
            ascil_to_key = {
                48 : "0",
                49 : "1",
                50 : "2",
                51 : "3",
                52 : "4",
                53 : "5",
                54 : "6",
                55 : "7",
                56 : "8",
                57 : "9",
                65 : "A",
                66 : "B",
                67 : "C",
                68 : "D",
                69 : "E",
                70 : "F",
                71 : "G",
                72 : "H",
                73 : "I",
                74 : "J",
                75 : "K",
                76 : "L",
                77 : "M",
                78 : "N",
                79 : "O",
                80 : "P",
                81 : "Q",
                82 : "R",
                83 : "S",
                84 : "T",
                85 : "U",
                86 : "V",
                87 : "W",
                88 : "X",
                89 : "Y",
                90 : "Z",
                32 : "SPACE",
                45 : "MINUS",
                61 : "EQUALS",
                16777252 : "CAPS LOCK",
                16777248 : "LEFT SHIFT",
                16777249 : "LEFT CTRL",
                16777251 : "LEFT ALT",
                16777220 : "RETURN",
                16777216 : "ESCAPE",
                16777217 : "TAB",
                16777222 : "INSERT",
                16777232 : "HOME",
                16777238 : "PAGE UP",
                16777223 : "DELETE",
                16777233 : "END",
                16777264 : "F1",
                16777265 : "F2",
                16777266 : "F3",
                16777267 : "F4",
                16777268 : "F5",
                16777269 : "F6",
                16777270 : "F7",
                16777271 : "F8",
                16777272 : "F9",
                16777273 : "F10",
                16777274 : "F11",
                16777275 : "F12",
                16777254 : "SCROLL LOCK",
                16777224 : "PAUSE",
                96 : "GRAVE",
                44 : "COMMA",
                46 : "PERIOD",
                47 : "SLASH",
                59 : "SEMICOLON",
                39 : "APOSTROPHE",
                92 : "BACKSLASH",
                91 : "LEFT BRACKET",
                93 : "RIGHT BRACKET",
                16777239 : "PAGE DOWN",
                16777219 : "BACKSPACE",
                16777301 : "MENU",
                16777250 : "LEFT SUPER",
                16777235 : "UP",
                16777234 : "LEFT",
                16777236 : "RIGHT",
                16777237 : "DOWN",
                16777221 : "KP ENTER",
                43 : "KP PLUS",
                42 : "KP MULTIPLY",
                16777253 : "NUM LOCK"

                

            }
            key_maps = {
                "leftstickup":ui.lineEdit_leftstickup,
                "leftstickdown":ui.lineEdit_leftstickdown,
                "leftstickleft":ui.lineEdit_leftstickleft,
                "leftstickright":ui.lineEdit_leftstickright,
                "lefttrigger":ui.lineEdit_lefttrigger,
                "leftbummer":ui.lineEdit_leftbummer,
                "rightstickup":ui.lineEdit_rightstickup,
                "rightstickdown":ui.lineEdit_rightstickdown,
                "rightstickleft":ui.lineEdit_rightstickleft,
                "rightstickright":ui.lineEdit_rightstickright,
                "righttrigger":ui.lineEdit_righttrigger,
                "rightbummer":ui.lineEdit_rightbummer,
                "startbutton":ui.lineEdit_startbutton,
                "abutton":ui.lineEdit_abutton,
                "bbutton":ui.lineEdit_bbutton,
                "xbutton":ui.lineEdit_xbutton,
                "ybutton":ui.lineEdit_ybutton

            }
            key_maps[self.current_key].setText(ascil_to_key[key])
            self.close()

class error_ifconfigisnotexists(QMainWindow): 
    def __init__(self):
        super().__init__()
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Icon.Critical)
  
    # setting message for Message Box 
        msg.setText("Error: config.toml is missing") 
      
    # setting Message box window title 
        msg.setWindowTitle("Error") 
      
    # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok) 
      
    # start the app 
        msg.exec_() 

class TempWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.setWindowTitle("Loading Data")
        self.resize(320,240)
        button = QLabel("Retrieving data.Wait for seconds")
        button.setFont(font)
        self.setCentralWidget(button)

    def dxdiag_test(self):
        if os.path.isfile("gpuspecs.xml"):
            self.close()
            return True
        else:
            print("Hello")
            self.show()
            if not self.isHidden():
                subprocess.run("dxdiag /x gpuspecs")
            self.close()
        return True

  

if __name__ == "__main__":
    appdata_path = os.getenv('APPDATA')
    file_path = f"{appdata_path}/UnleashedRecomp/config.toml"
    check_file = os.path.exists(file_path)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('qt.ico'))
    splash = TempWindow()
    
    if check_file and splash.dxdiag_test():
        Dialog = QtWidgets.QDialog()
        window2 = KeyInputWindow()
        window3 = TempWindow()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.init_values()
        Dialog.show()
        sys.exit(app.exec_())
    else:
        window = error_ifconfigisnotexists()
        sys.exit(app.exec_())

def dxdiag_test():
    if os.path.isfile("gpuspecs.xml"):
        return True
    else:
        subprocess.run("dxdiag /x gpuspecs")
    return True