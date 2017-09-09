# /usr/bin/env python
# -*- coding : utf-8 -*-
import os
import sys
import time

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.filePath = ''
        self.categoryPath = './file/category.io'
        self.kk = []
        self.setupUi()

    def setupUi(self):
        ww = QWidget()
        self.setWindowTitle("书籍摘录助手")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.resize(1280, 720)
        self.setWindowState(Qt.WindowMaximized)
        mainlayout = QHBoxLayout()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        ww1 = QWidget()
        ww1.setStyleSheet("font-size:20px;font-style:SansSerif")
        l11 = QVBoxLayout()
        newfile = QPushButton("新建文件")
        opfile = QPushButton("打开文件")
        newfile.setMinimumHeight(40)
        opfile.setMinimumHeight(40)
        l11.setContentsMargins(20, 40, 20, 0)
        l11.setSpacing(40)
        newfile.setFont(QFont('SansSerif', 20))
        opfile.setFont(QFont('SansSerif', 20))
        opfile.resize(opfile.sizeHint())
        l11.addWidget(newfile)
        l11.addWidget(opfile)
        l11.addStretch(6)
        ww1.setLayout(l11)
        layout1.addWidget(ww1)

        l22 = QHBoxLayout()
        kk = QWidget()
        kk.setStyleSheet("font-size:20px;font-style:SansSerif")
        searchBu = QPushButton("搜索")
        searchBu.setFont(QFont('SansSerif', 20))
        searchBu.setMinimumHeight(40)
        searchEd = QLineEdit()
        searchEd.setMinimumHeight(30)
        searchEd.setFont(QFont('SansSerif', 20))
        searchEd.resize(searchEd.sizeHint())
        l22.addWidget(searchEd)
        l22.addWidget(searchBu)
        kk.setLayout(l22)

        kk1 = QWidget()
        kk1.setStyleSheet("font-size:20px;font-style:SansSerif")
        l21 = QFormLayout()
        label = QLabel("搜索列表：")
        l21.addRow(label)
        kk1.setLayout(l21)

        l21.setContentsMargins(0, 0, 0, 0)
        l22.setContentsMargins(0, 0, 0, 0)
        layout2.setContentsMargins(20, 40, 20, 0)

        layout2.addWidget(kk)
        layout2.addWidget(kk1)
        layout2.addStretch(0)

        ww3 = QWidget()
        ww3.setStyleSheet("font-size:20px;font-style:SansSerif")
        l31 = QFormLayout()
        createLabel = QLabel("创建时间：")
        createTime = QLabel()
        createTime.setText(self.getTime(0))
        lastLabel = QLabel("更新时间：")
        lastTime = QLabel()
        lastTime.setText(self.getTime(1))
        nameLabel = QLabel("书名")
        nameEd = QLineEdit()
        cateLable = QLabel("类别")
        nameEd.setMinimumHeight(30)
        self.category = QComboBox()
        self.category.setMinimumHeight(35)
        self.getCategory()
        changeBu = QPushButton("修改标签")
        changeBu.setMinimumHeight(40)
        changeBu.clicked.connect(self.change)
        zhaiLabel = QLabel("摘记")
        zhaijiEd = QTextEdit()
        zhaijiEd.setMinimumHeight(250)
        pingLable = QLabel("评注")
        pingZhuEd = QTextEdit()
        pingZhuEd.setMinimumHeight(250)

        l311 = QHBoxLayout()
        l311.addWidget(createLabel)
        l311.addWidget(createTime)
        l311.addWidget(lastLabel)
        l311.addWidget(lastTime)
        l311.setStretchFactor(createLabel, 1)
        l311.setStretchFactor(createTime, 3)
        l311.setStretchFactor(lastLabel, 1)
        l311.setStretchFactor(lastTime, 3)
        l311.setContentsMargins(0, 0, 0, 0)

        l312 = QHBoxLayout()
        l312.addWidget(nameLabel)
        l312.addWidget(nameEd)
        l312.addStretch(11)
        l312.setStretchFactor(nameLabel, 3)
        l312.setStretchFactor(nameEd, 9)
        l312.setContentsMargins(0, 0, 0, 0)

        l313 = QHBoxLayout()
        l313.addWidget(cateLable)
        l313.addWidget(self.category)
        l313.addWidget(changeBu)
        l313.addStretch(7)
        l313.setStretchFactor(cateLable, 3)
        l313.setStretchFactor(self.category, 9)
        l313.setStretchFactor(changeBu, 2)
        l313.setContentsMargins(0, 0, 0, 0)

        l314 = QHBoxLayout()
        l314.addWidget(zhaiLabel)
        l314.addWidget(zhaijiEd)
        l314.setContentsMargins(0, 0, 0, 0)

        l315 = QHBoxLayout()
        l315.addWidget(pingLable)
        l315.addWidget(pingZhuEd)

        l31.setContentsMargins(0, 0, 0, 0)
        l31.addRow(l311)
        l31.addRow(l312)
        l31.addRow(l313)
        l31.addRow(l314)
        l31.addRow(l315)
        ww3.setLayout(l31)

        layout3.setContentsMargins(20, 40, 20, 0)
        layout3.addWidget(ww3)

        mainlayout.addLayout(layout1)
        mainlayout.addLayout(layout2)
        mainlayout.addLayout(layout3)
        mainlayout.setStretchFactor(layout1, 1)
        mainlayout.setStretchFactor(layout2, 2)
        mainlayout.setStretchFactor(layout3, 4)

        ww.setLayout(mainlayout)
        self.setCentralWidget(ww)

    def change(self):
        self.chage = ChangeWindow()
        self.chage.work()
        self.chage.myclicked.connect(self.getCategory)

    def getCategory(self):
        self.category.clear()
        fo = open(self.categoryPath, 'r', encoding='utf8')
        stri = fo.read()
        fo.close()
        kk = stri.split('&&')
        for k in kk:
            self.category.addItem(k)

    def getTime(self, index):
        if self.filePath is '':
            return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        else:
            return self.kk[index]


class ChangeWindow(QWidget):
    myclicked = QtCore.pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.flagName = ""
        self.layout = QGridLayout()
        self.layout1 = QVBoxLayout()
        self.categoryList = []
        self.checkBoxList = []
        self.layoutForButton = QHBoxLayout()
        lala = QVBoxLayout(self)
        lala.addLayout(self.layout, 0)
        lala.addLayout(self.layout1, 1)
        # 打开标签文件读取标签
        self.path = os.path.abspath('./file/category.io')
        fo = open(self.path, 'r')
        stri = fo.read()
        fo.close()
        self.setupUi(stri)
        self.ll = 0

    def setupUi(self, stri):
        self.setWindowTitle("修改标签")
        # 标签
        kk = stri.split('&&')
        i = 0
        y = 20
        for k in kk:
            self.categoryList.append(k)
            checkbox = QCheckBox(k)
            self.checkBoxList.append(checkbox)
            self.layout.addWidget(checkbox, y // 20 - 1, i)
            i += 1
            y += 20 * (i // 4)
            i %= 4
        self.hang = y // 20 - 1
        self.lie = i
        self.ll = y - 20
        self.resize(400, 160 + self.ll)

        widget = QWidget()
        self.layout1.addWidget(widget)
        lalala = QHBoxLayout()
        widget.setLayout(lalala)
        label = QLabel("标签名称", widget)
        self.nn = QLineEdit(widget)
        lalala.addWidget(label)
        lalala.addWidget(self.nn)

        addfl = QtWidgets.QPushButton()
        addfl.setText("增  加")
        addfl.setObjectName("addflag")
        addfl.clicked.connect(self.addflag)

        delfl = QtWidgets.QPushButton()
        delfl.setText("删除选中")
        delfl.setObjectName("addflag")
        delfl.clicked.connect(self.delflag)

        back = QtWidgets.QPushButton()
        back.setText("确  认")
        back.setObjectName("back")
        back.clicked.connect(self.backMain)

        causel = QtWidgets.QPushButton()
        causel.setText("取  消")
        causel.setObjectName("causel")
        causel.clicked.connect(self.close)

        self.layoutForButton.addWidget(addfl)
        self.layoutForButton.addWidget(delfl)
        self.layoutForButton.addWidget(back)
        self.layoutForButton.addWidget(causel)
        self.layout1.addLayout(self.layoutForButton)

    def backMain(self):
        stri = ''
        for category in self.categoryList:
            stri = stri + category + '&&'
        stri = stri[:len(stri) - 2]
        fo = open(self.path, 'w')
        fo.write(stri)
        fo.close()
        self.myclicked.emit(' ')
        self.close()

    def addflag(self):
        message = QtWidgets.QMessageBox(self)
        kk = self.nn.text()
        if kk is '':
            message.warning(self, '错误', '标签名称不能为空')
        else:
            if kk in self.categoryList:
                message.warning(self, '错误', '标签名称不能重复')
            else:
                self.categoryList.append(kk)
                checkBox = QCheckBox(kk)
                self.checkBoxList.append(checkBox)
                self.layout.addWidget(checkBox, self.hang, self.lie)
                self.hang += self.lie // 4
                self.lie = (self.lie + 1) % 4
                self.nn.setText('')

    def delflag(self):
        # 删除标记的标签
        # 删除方法：使用一个temp存储没有标记的标签，用来重新生成标签
        temp = []
        for checkBox in self.checkBoxList:
            if not checkBox.isChecked():
                temp.append(checkBox.text())
            checkBox.deleteLater()
        self.checkBoxList = []
        self.categoryList = temp
        self.up()

    def up(self):
        i = 0
        y = 20
        for category in self.categoryList:
            checkbox = QCheckBox(category, self)
            self.checkBoxList.append(checkbox)
            self.layout.addWidget(checkbox, y // 20 - 1, i)
            i += 1
            y += 20 * (i // 4)
            i %= 4
        self.hang = y // 20 - 1
        self.lie = i
        self.ll = y - 20
        self.resize(400, 160 + self.ll)

    def work(self):
        if not self.isVisible():
            self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
