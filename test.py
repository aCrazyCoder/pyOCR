# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(-10, 0, 976, 548))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setMaximumSize(QtCore.QSize(976, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setMinimumSize(QtCore.QSize(30, 30))
        self.label_logo.setMaximumSize(QtCore.QSize(30, 30))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_3.addWidget(self.label_logo)
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setMinimumSize(QtCore.QSize(50, 50))
        self.label_title.setMaximumSize(QtCore.QSize(50, 50))
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_3.addWidget(self.label_title)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.comboBox_choose = QtWidgets.QComboBox(self.frame)
        self.comboBox_choose.setMinimumSize(QtCore.QSize(250, 30))
        self.comboBox_choose.setObjectName("comboBox_choose")
        self.horizontalLayout_4.addWidget(self.comboBox_choose)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_login.setText("")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_2.addWidget(self.btn_login)
        self.btn_setting = QtWidgets.QPushButton(self.frame)
        self.btn_setting.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_setting.setText("")
        self.btn_setting.setObjectName("btn_setting")
        self.horizontalLayout_2.addWidget(self.btn_setting)
        self.btn_min = QtWidgets.QPushButton(self.frame)
        self.btn_min.setMaximumSize(QtCore.QSize(13, 13))
        self.btn_min.setText("")
        self.btn_min.setObjectName("btn_min")
        self.horizontalLayout_2.addWidget(self.btn_min)
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setMaximumSize(QtCore.QSize(13, 13))
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cameraShow = QCameraViewfinder(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraShow.sizePolicy().hasHeightForWidth())
        self.cameraShow.setSizePolicy(sizePolicy)
        self.cameraShow.setMinimumSize(QtCore.QSize(640, 480))
        self.cameraShow.setMaximumSize(QtCore.QSize(640, 480))
        self.cameraShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cameraShow.setObjectName("cameraShow")
        self.horizontalLayout.addWidget(self.cameraShow)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.caputurePhoto = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caputurePhoto.sizePolicy().hasHeightForWidth())
        self.caputurePhoto.setSizePolicy(sizePolicy)
        self.caputurePhoto.setMinimumSize(QtCore.QSize(320, 240))
        self.caputurePhoto.setMaximumSize(QtCore.QSize(320, 240))
        self.caputurePhoto.setText("")
        self.caputurePhoto.setObjectName("caputurePhoto")
        self.verticalLayout.addWidget(self.caputurePhoto)
        self.ocrInfo = QtWidgets.QTextEdit(self.layoutWidget)
        self.ocrInfo.setMinimumSize(QtCore.QSize(320, 170))
        self.ocrInfo.setMaximumSize(QtCore.QSize(320, 170))
        self.ocrInfo.setReadOnly(True)
        self.ocrInfo.setObjectName("ocrInfo")
        self.verticalLayout.addWidget(self.ocrInfo)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.captureBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.captureBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.captureBtn.setObjectName("captureBtn")
        self.horizontalLayout_5.addWidget(self.captureBtn)
        self.checkBox_cam = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_cam.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkBox_cam.setObjectName("checkBox_cam")
        self.horizontalLayout_5.addWidget(self.checkBox_cam)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.captureBtn.setText(_translate("MainWindow", "open"))
        self.checkBox_cam.setText(_translate("MainWindow", "camera"))
