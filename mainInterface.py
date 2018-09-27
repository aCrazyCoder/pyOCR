# -*- coding: utf-8 -*-

# The main function

from login import Ui_Form
from ocr import ocr
import threading
from os import path
from PyQt5.Qt import Qt, QMenu, QAction
from API import CIBuffers, CIUrls, CIFiles
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo, QCameraViewfinderSettings
from PyQt5.QtWidgets import qApp, QMessageBox, QSystemTrayIcon, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice, QSize, pyqtSignal
from mainWidget import Ui_mainWidget


class mainInterface(QWidget):

    # 定义信号
    processFinished = pyqtSignal(dict)

    def __init__(self):
        """
        初始化
        :return: null
        """
        # 超类初始化
        super().__init__()

        # UI初始化
        self.ui = Ui_mainWidget()
        self.ui.setupUi(self)
        self.grabKeyboard()
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 初始化相机
        self.camera = QCamera()
        self.imageCapture = QCameraImageCapture(self.camera)
        self.viewsetting = QCameraViewfinderSettings()
        self.initimplement()

        # 初始化标题栏
        self.initTitleBar()

        # 初始化系统托盘
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('OCR.ico'))
        self.initTray()

        # OCR识别部分
        self.OCR = ocr()
        self.OCR.setappid('1257206643')
        self.OCR.setsecretid('AKIDFTddWEg9Ncsz0sE7oOpBNOExdDdeCUJ3')
        self.OCR.setsecretkey('FQitsgUND8yfrZK0RrBMOJB5tWhCm5Ol')

        # 初始化登录部分
        self.logWidget = QWidget()
        self.logui = Ui_Form()
        self.logui.setupUi(self.logWidget)
        self.logWidget.setWindowFlags(Qt.FramelessWindowHint)
        self.logWidget.setWindowModality(Qt.ApplicationModal)
        self.logui.close_btn.clicked.connect(self.logWidget.close)

        # 初始化变量
        self.mousePressd = False
        self.mousePoint = None
        self.result = {}
        self.isFirst = False

        # 初始化字定义信号连接
        self.processFinished.connect(self.updateOCRInfo)
        self.ui.btn_login.clicked.connect(self.logWidget.show)

    def initTitleBar(self):
        """
        初始化标题栏
        :return: null
        """
        self.ui.frame.setStyleSheet("QFrame#frame{background-color:rgb(244, 76, 76);}")
        self.ui.label_logo.setStyleSheet("QLabel{border-image:url(./image/ocr.png);}")
        self.ui.label_title.setStyleSheet("QLabel{border-image:url(./image/iOCR.png);}")
        self.ui.comboBox_choose.setStyleSheet(
            "QComboBox {border-radius:15px;border: 2px solid #4AFFF4;font-family:'楷体';font-size:20px;}"
            "QComboBox QAbstractItemView::item{height:50px;width:200px;}"
            "QComboBox::down-arrow{image: url(./image/arrow.png);width:25px;height:25px;}"
            "QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position:top right;border:none;margin-right:30px;}"
            "QComboBox::down-arrow:hover{image:url(./image/arrow_hover.png);width:25px;height:25px;}"
            "QComboBox::down-arrow:on {top: 1px;left: 1px;}")
        self.ui.comboBox_choose.insertItem(0, '       印刷体识别')
        self.ui.comboBox_choose.insertItem(1, '       手写体识别')
        self.ui.comboBox_choose.insertItem(2, '       身份证识别')
        self.ui.comboBox_choose.insertItem(3, '       银行卡识别')
        self.ui.btn_login.setStyleSheet("QPushButton{border-image:url(./image/default-portrait.png);}")
        self.ui.btn_setting.setStyleSheet("QPushButton{border-image:url(./image/settings.png);}"
                                          "QPushButton:hover{border-image:url(./image/qcconfig-hover.png);}")
        self.ui.btn_min.setStyleSheet("QPushButton{border-image:url(./image/mini_new.png);}"
                                      "QPushButton:hover{border-image:url(./image/mini_hover_new.png);}")
        self.ui.btn_close.setStyleSheet("QPushButton{border-image:url(./image/close.png);}"
                                        "QPushButton:hover{border-image:url(./image/close-hover.png);}")
        self.ui.checkBox_cam.setStyleSheet("QCheckBox{spacing: 5px;font-size: 24px;vertical-align:middle}"
                                           "QCheckBox::indicator { width: 45px;height: 45px;}"
                                           "QCheckBox::indicator::unchecked {image: url(./image/close_cam.png);}"
                                           "QCheckBox::indicator::checked { image: url(./image/open_cam.png);}")
        self.ui.captureBtn.setStyleSheet(
            "QPushButton{border-style: outset;border-width: 2px;border-color: rgb(82,215,100);border-radius: 5px;font-size: 24px;}"
            "QPushButton:pressed{background-color: rgb(176,215,181);border-style: inset;}")

        self.ui.checkBox_cam.setChecked(True)

        self.ui.btn_close.clicked.connect(lambda: qApp.quit())
        self.ui.btn_min.clicked.connect(self.miniToTray)
        self.ui.checkBox_cam.stateChanged.connect(self.camControl)

    def initTray(self):
        """
        初始化系统托盘信息
        :return:
        """
        tray_menu = QMenu()
        restoreAction = QAction('&Show', self)
        quitAction = QAction('&Quit', self)
        tray_menu.addAction(restoreAction)
        tray_menu.addAction(quitAction)
        self.tray.setContextMenu(tray_menu)
        restoreAction.triggered.connect(self.trayActivatedEvent)
        quitAction.triggered.connect(qApp.quit)
        self.tray.activated.connect(self.trayActivatedEvent)

    def initimplement(self):
        """
        初始化实现端口
        :return: ui
        """
        camInfo = QCameraInfo(self.camera)
        if camInfo.defaultCamera().isNull():
            QMessageBox.warning(self, 'Warning', 'No available camera!', QMessageBox.Ok)
            return -1
        else:
            self.ui.caputurePhoto.setText(camInfo.description())
            self.camera.setViewfinder(self.ui.cameraShow)
            self.camera.setCaptureMode(QCamera.CaptureStillImage)
            self.camera.load()
            resolution = self.camera.supportedViewfinderResolutions()
            if len(resolution) != 0:
                if QSize(640, 480) in resolution:
                    self.viewsetting.setResolution(QSize(640, 480))
                elif QSize(640, 360) in resolution:
                    self.viewsetting.setResolution(QSize(640, 360))
                else:
                    self.viewsetting.setResolution(resolution[0])
                self.camera.setViewfinderSettings(self.viewsetting)

            # ------------------------------Note--------------------------------
            # 此种方法利用摄像头准备捕捉图像的状态来进行捕捉图像，readyForCapture
            # 为true时，才进行捕捉图像，详见下面捕捉函数槽函数。这种方法将进行不
            # 停的捕捉，将每次捕捉的相邻图像进行图像相似度判断。当图像相似度低于
            # 阈值时，认定为新图像，才进行OCR识别。否则仅捕捉图像而不进行识别。当
            # 然捕捉图像速度过于太快时，可以用定时器，每隔0.5秒，去检查readyFor
            # Capture状态位，进而有效控制程序资源。
            # 本应用中采用按键捕捉方式，非自动，详见下面按键捕捉事件
            # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            # self.imageCapture.readyForCaptureChanged.connect(self.captureimage)

            self.camera.start()

        self.ui.caputurePhoto.setScaledContents(True)

        self.imageCapture.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)

        self.imageCapture.imageCaptured.connect(self.displayimage)

        self.ui.captureBtn.clicked.connect(self.openDlg)

    def displayimage(self, num, image):
        """
        显示图形
        :param num: number
        :param image: image
        :return: null
        """
        self.ui.caputurePhoto.setPixmap(QPixmap.fromImage(image))
        self.ui.ocrInfo.setText('识别中......')
        t = threading.Thread(target=self.ocrForImage, args=(image,))
        t.start()

    # def captureimage(self, state):
    #     """
    #     捕捉图像槽函数
    #     :state: 状态变量
    #     :return: null
    #     """
    #     if state is True:
    #         self.camera.searchAndLock()
    #         self.imageCapture.capture()
    #         self.camera.unlock()

    # def saveimage(self):
    #     """
    #     保存图像槽函数
    #     :return: null
    #     """
    #     pix = QPixmap(self.ui.caputurePhoto.pixmap())
    #     if pix:
    #         pix.save(r'D://1.png', 'PNG')
    #         QMessageBox.information(self, 'Message', 'Capture Successfully', QMessageBox.Ok)

    def ocrForImage(self, image):
        """
        为截取的图片进行ocr识别
        :param image: QImage
        :return: null
        """
        # Note:子线程里不能对ui界面做改动，ui界面修改只能在主线程中修改，下面注释的做法是错误的
        # self.ui.ocrInfo.setText('识别中......')
        byte = QByteArray()
        buffer = QBuffer(byte)
        buffer.open(QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        self.result = self.OCR.client.general_detect(CIBuffers([byte.data()]))
        self.processFinished.emit(self.result)

    def updateOCRInfo(self, res):
        """
        将ocr识别结果显示在信息框中
        :param res:
        :return:
        """
        if res['code'] == 0 and res['message'] == 'OK':
            self.ui.ocrInfo.setText('OK')
            ocrInfo = []
            for i in range(len(self.result['data']['items'])):
                ocrInfo.append(self.result['data']['items'][i]['itemstring'])
            self.ui.ocrInfo.setText(''.join(ocrInfo))
        else:
            self.ui.ocrInfo.setText('识别失败！')

    def camControl(self, state):
        """
        槽函数
        控制相机开关
        :param state: checkbox开关状态
        :return:null
        """
        if state == Qt.Unchecked:
            self.ui.cameraShow.setUpdatesEnabled(False)
        elif state == Qt.Checked:
            self.ui.cameraShow.setUpdatesEnabled(True)
        else:
            return -1

    def miniToTray(self):
        """
        槽函数
        最小化到系统托盘
        :return:null
        """
        if not self.tray.isVisible():
            self.tray.show()
        if self.tray.isVisible():
            if self.isFirst is False:
                QMessageBox.information(self, "Systray", "The program will keep running in the "
                                                                    "system tray. To terminate the program, "
                                                                    "choose <b>Quit</b> in the context menu "
                                                                    "of the system tray entry.")
                self.isFirst = True
            self.hide()

    def trayActivatedEvent(self, reason):
        """
        槽函数
        响应点击托盘图标
        :param reason: 响应原因
        :return: null
        """
        if reason == QSystemTrayIcon.Context:
            pass
        else:
            self.tray.hide()
            self.show()

    def openDlg(self):
        """
        槽函数
        打开对话框选取文件
        :return:文件名
        """
        filename, filetype = QFileDialog.getOpenFileName(self, '选取图片', path.expanduser('~'), "Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.displayimage(0, QImage(filename))

    def keyPressEvent(self, e):
        """
        槽函数
        键盘按键响应事件
        :param e: 按键事件
        :return: null
        """
        if e.key() == Qt.Key_Space:
            if self.imageCapture.isReadyForCapture():
                self.camera.searchAndLock()
                self.imageCapture.capture()
                self.camera.unlock()

    def mouseMoveEvent(self, e):
        """
        槽函数
        定义鼠标移动事件
        :param e: QMouseEvent
        :return: null
        """
        if (e.buttons() == Qt.LeftButton) and self.mousePressd:
            self.move(e.globalPos() - self.mousePoint)
            e.accept()

    def mousePressEvent(self, e):
        """
        槽函数
        定义鼠标按下事件
        :param e: QMouseEvent
        :return: null
        """
        if e.button() == Qt.LeftButton:
            self.mousePressd = True
            self.mousePoint = e.globalPos() - self.pos()
            e.accept()

    def mouseReleaseEvent(self, e):
        """
        槽函数
        定义鼠标松开事件
        :param e: QMouseEvent
        :return: null
        """
        self.mousePressd = False


