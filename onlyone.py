# -*- coding:utf-8 -*-
# created by CYMX on 17/9/1

# 文件创建时间：theFirst   最后一次保存时间：theLast
# 输入框：书名bookName；
# 下拉框： 类别category 支持增删 按钮add,del,
# 输入框：摘记
# 输入框：评注
# 表格布局 书籍基本信息
# 	作者：
# 	出版社：
# 	出版时间：（时间选择框？）
# 	其他：
# 附件选择按钮  导出为word文件

import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

qtCreatorFile = "mainwindow.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.chooseFile.clicked.connect(self.thefile)
        self.GOGOGO.clicked.connect(self.goToFly)
        self.add.clicked.connect(self.addFlag)
        self.dele.clicked.connect(self.delFlag)
        self.addFile.connect(self.addFile)

        pass

    def setupUi(self):
        self.theFirstt.setText('2017/09/01')
        self.theLast.setText('2017/09/01')
        # 从数据库取出数据

        pass

    # 应该弹出新的对话框：
    # 标签名称flagName
    # 提示重复文本，默认为NULL
    # 确定按钮 取消按钮
    # 在按确定后执行一边查重
    def addFlag(self):
        self.addblog = WorkWindow()
        self.addblog.work()
        pass

    # 应该弹出包含所有标签复选框的对话框
    # 确定按钮 取消按钮
    def delFlag(self):
        pass

    def addFile(self):
        absolute_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选取文件夹', '.')
        print(absolute_path)
        self.filePath.setText(absolute_path)
        pass

class WorkWindow(QWidget):
    logs = []
    threads = []

    def __init__(self):
        QWidget.__init__(self)
        self.flagName = ""
        self.setupUi()
        self.causel.clicked.connect(self.close)

    def setupUi(self):
        self.resize(400, 40+120*self.threadNum)
        for i in range(0, self.threadNum):
            log = QtWidgets.QTextEdit(self)
            log.setGeometry(QtCore.QRect(10, 10+120*i, 380, 110))
            log.setObjectName("log"+str(i))
            log.setReadOnly(True)
            self.logs.append(log)
        self.causel = QtWidgets.QPushButton(self)
        self.causel.setGeometry(QtCore.QRect(180, 10+120*self.threadNum, 40, 20))
        self.causel.setText("取 消")
        self.causel.setObjectName("causel")

    def work(self):
        if not self.isVisible():
            self.show()

