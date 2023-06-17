from PyQt5 import uic
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QIcon, QPixmap, QRegularExpressionValidator, QValidator, QCursor
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from pyqt5_plugins.examplebutton import QtWidgets

from ui.py.tools import Tools
from interface import interface

# 加载 .ui 文件
ui_path = "ui/index.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_path)
ui_icon = 'ui/img/spider.png'
ui_pointer = 'ui/img/finger.png'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(ui_icon))
        self.pixmap = QPixmap(ui_pointer)
        self.smaller_pixmap = self.pixmap.scaled(24, 24)  # 将图像调整为 32x32 的尺寸
        # 设置鼠标跟踪
        self.setMouseTracking(True)
        # 初始化数据
        self.scanner_data = []
        self.file_data = []
        self.interface = interface()
        self.Tools = Tools()
        self.log_data = []

        # 槽函数 功能
        self.ui.start.clicked.connect(self.crawl_web)
        self.ui.open.clicked.connect(self.open_file)
        self.ui.xss.stateChanged.connect(self.xss_trace)

        self.ui.findlog.clicked.connect(self.find_log)
        self.ui.clearlog.clicked.connect(self.clear_log)

    def crawl_web(self):
        validator = QRegularExpressionValidator(QRegularExpression(r'[a-zA-z]+://[^\s]*'), self)
        url, ok = QInputDialog.getText(self, "爬取网址", "请输入网址:")

        if validator.validate(url, 0)[0] == QValidator.Acceptable:
            self.scanner_data = self.interface.spider_interface(url)
        else:
            QMessageBox.warning(self, "输入错误", "请输入有效的网址！", QMessageBox.Ok)
        self.Tools.addFilesToTreeView(data=self.scanner_data, component=self.ui.scanner)

    def open_file(self):
        self.file_data = self.Tools.handleHeaderClicked()
        self.Tools.addFilesToTreeView(data=self.file_data, component=self.ui.webfile)

    def xss_trace(self):
        # print('yes')
        target_list = self.Tools.model.getCheckedItems()
        xss_logs = []
        for item in target_list:
            xss_per_log = self.interface.xss_interface(item)
            self.ui.log.append(xss_per_log)
            xss_logs.append(xss_per_log)
        # print(xss_logs)

    def clear_log(self):
        self.ui.log.clear()

    def find_log(self):
        self.Tools.open_log_folder()

    # override
    def enterEvent(self, event):
        # 鼠标进入部件时更换光标
        # 创建自定义光标对象
        cursor = QCursor(self.smaller_pixmap)
        self.setCursor(cursor)

    def leaveEvent(self, event):
        # 鼠标离开部件时，恢复默认光标样式
        self.unsetCursor()
