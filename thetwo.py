# /usr/bin/env python
# -*- coding : utf-8 -*-
import os
import re
import sys
import time
import zipfile

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.FindPath = './data/his/'
        self.theinfo = '&&&&&&'
        QtWidgets.QMainWindow.__init__(self)
        self.filePath = ''
        self.categoryPath = './data/file/category.io'
        self.kk = []
        self.bookin = None
        self.files = None
        self.setupUi()
        self.cli = False
        self.listtemp = QListWidget()

    def setupUi(self):
        ww = QWidget()

        self.setWindowTitle("书籍摘录助手")
        self.setFixedSize(1280, 720)
        menuList = QWidget()
        menuList.setStyleSheet("font-size:20px;font-style:SansSerif;")
        layout0 = QVBoxLayout()
        layoutMenu = QHBoxLayout()
        layoutMenu.setSpacing(10)
        newFile = QPushButton("新建笔记")
        newFile.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        newFile.setIcon(QIcon("./img/newfile.png"))
        newFile.setIconSize(QSize(20, 20))
        newFile.clicked.connect(self.thenew)
        newFile.setMinimumHeight(40)
        delFile = QPushButton("删除笔记")
        delFile.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        delFile.setIcon(QIcon("./img/delete.jpg"))
        delFile.setIconSize(QSize(20, 20))
        delFile.clicked.connect(self.delfile)
        delFile.setMinimumHeight(40)
        importFile = QPushButton("笔记导入")
        importFile.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        importFile.setIcon(QIcon("./img/import.png"))
        importFile.setIconSize(QSize(20, 20))
        importFile.clicked.connect(self.importfile)
        importFile.setMinimumHeight(40)
        toWord = QPushButton("导出为word")
        toWord.setMinimumHeight(40)
        toWord.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        toWord.setIcon(QIcon("./img/output.jpg"))
        toWord.setIconSize(QSize(20, 20))
        # toWord.clicked.connect(self.toword)
        exportFile = QPushButton("笔记备份")
        exportFile.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        exportFile.setIcon(QIcon("./img/output.jpg"))
        exportFile.setIconSize(QSize(20, 20))
        exportFile.clicked.connect(self.exportfile)
        exportFile.setMinimumHeight(40)
        cateAdmin = QPushButton("类别管理")
        cateAdmin.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        cateAdmin.setIcon(QIcon("./img/manager.jpg"))
        cateAdmin.setIconSize(QSize(20, 20))
        cateAdmin.setMinimumHeight(40)
        cateAdmin.clicked.connect(self.change)
        saveBu = QPushButton("保  存")
        saveBu.setStyleSheet("QPushButton{border-style:none;border-radius:5px}QPushButton:hover{background:#B0E0E6}")
        saveBu.setIcon(QIcon("./img/save.jpg"))
        saveBu.setIconSize(QSize(20, 20))
        saveBu.setMinimumHeight(40)
        saveBu.clicked.connect(self.save)
        layoutMenu.setContentsMargins(4, 0, 4, 0)
        menuList.setLayout(layoutMenu)
        layoutMenu.addWidget(newFile)
        layoutMenu.addWidget(delFile)
        layoutMenu.addWidget(importFile)
        layoutMenu.addWidget(toWord)
        layoutMenu.addWidget(exportFile)
        layoutMenu.addWidget(cateAdmin)
        layoutMenu.addWidget(saveBu)
        layoutMenu.addStretch()
        layout0.setContentsMargins(0, 0, 0, 0)

        ww0 = QWidget()
        ww0.setStyleSheet("font-size:20px;font-style:SansSerif;background:#4f535e")
        mainlayout = QHBoxLayout()
        mainlayout.setContentsMargins(0, 0, 0, 0)
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        ww2 = QWidget()
        ww2.setStyleSheet("font-size:20px;font-style:SansSerif;background:#e6e8e7;border-radius:10px;")
        ww1 = QWidget()
        ww1.setStyleSheet("font-size:20px;font-style:SansSerif;color:white")
        l11 = QVBoxLayout()
        self.treelist = QTreeWidget()
        self.treelist.setHeaderHidden(True)
        self.treelist.setStyleSheet("border-style:none")
        self.treelist.setMinimumHeight(400)
        self.categoryTree = QTreeWidgetItem()
        self.categoryTree.setText(0, '全部类别')
        self.treelist.setColumnCount(1)
        self.treelist.setHeaderLabel("")
        self.treelist.addTopLevelItem(self.categoryTree)
        self.treelist.itemClicked.connect(self.checkFile)

        l11.setContentsMargins(0, 0, 0, 0)
        layout1.setContentsMargins(5, 5, 5, 0)
        l11.setSpacing(55)
        l11.addWidget(self.treelist)
        ww1.setLayout(l11)
        layout1.addWidget(ww1, 8)

        l22 = QHBoxLayout()
        kk = QWidget()
        kk.setStyleSheet("font-size:20px;font-style:SansSerif;border-radius:0px;border-width:1px;border-style:solid;")
        searchBu = QPushButton("搜索")
        searchBu.setIcon(QIcon("./img/search.jpg"))
        searchBu.setIconSize(QSize(20, 20))
        searchBu.setStyleSheet("QPushButton:hover{background:#B0E0E6;border-radius:15px}")
        searchBu.setFont(QFont('SansSerif', 20))
        searchBu.clicked.connect(self.searchfile)
        searchBu.setMinimumHeight(40)
        self.searchEd = QLineEdit()
        self.searchEd.setMinimumHeight(30)
        self.searchEd.setFont(QFont('SansSerif', 20))
        self.searchEd.setStyleSheet("background:white")
        self.searchEd.resize(self.searchEd.sizeHint())
        l22.addWidget(self.searchEd)
        l22.addWidget(searchBu)
        kk.setLayout(l22)

        kk1 = QWidget()
        kk1.setStyleSheet("font-size:20px;font-style:SansSerif;")
        l21 = QVBoxLayout()
        label = QLabel("笔记列表：")
        self.tll = QListWidget()
        self.tll.setStyleSheet("background:white")
        self.tll.clicked.connect(self.open)

        l21.addWidget(label)
        l21.addWidget(self.tll)
        kk1.setLayout(l21)

        l21.setContentsMargins(0, 0, 0, 0)
        l22.setContentsMargins(0, 0, 0, 0)
        layout2.setContentsMargins(5, 5, 5, 5)

        layout2.addWidget(kk)
        layout2.addWidget(kk1)
        layout2.setStretchFactor(kk, 1)
        layout2.setStretchFactor(kk1, 7)

        ww3 = QWidget()
        ww3.setStyleSheet("font-size:20px;font-style:SansSerif;background:white;border-radius:10px;background:#e6e8e7")
        l31 = QFormLayout()
        createLabel = QLabel("创建时间：")
        self.createTime = QLabel()
        self.createTime.setText(self.getTime(0))
        lastLabel = QLabel("更新时间：")
        self.lastTime = QLabel()
        self.lastTime.setText(self.getTime(1))
        nameLabel = QLabel("书名")
        self.nameEd = QLineEdit()
        self.nameEd.setStyleSheet("border-style:solid;border-width:1px;border-radius:0px;background:white")
        otherBu = QPushButton("其他信息")
        otherBu.setStyleSheet("QPushButton:hover{background:#B0E0E6;border-radius:15px}")
        otherBu.clicked.connect(self.info)
        otherBu.setMinimumHeight(40)
        cateLable = QLabel("类别")
        self.nameEd.setMinimumHeight(30)
        self.category = QComboBox()
        self.category.setStyleSheet("border-style:solid;border-width:1px;border-radius:0px;")
        self.category.setMinimumHeight(35)

        self.getCategory()
        ylayout = QVBoxLayout()
        zhaiLabel = QLabel("摘记")
        ylayout.addWidget(zhaiLabel)
        ylayout.addStretch(1)
        self.zhaijiEd = QTextEdit()
        self.zhaijiEd.setStyleSheet("border-style:solid;border-width:1px;border-radius:0px;background:white")
        self.zhaijiEd.setMinimumHeight(270)
        ylayout1 = QVBoxLayout()
        pingLable = QLabel("评注")
        ylayout1.addWidget(pingLable)
        ylayout1.addStretch(1)
        self.pingZhuEd = QTextEdit()
        self.pingZhuEd.setStyleSheet("border-style:solid;border-width:1px;border-radius:0px;background:white")
        self.pingZhuEd.setMinimumHeight(270)

        l311 = QHBoxLayout()
        l311.addWidget(createLabel)
        l311.addWidget(self.createTime)
        l311.addWidget(lastLabel)
        l311.addWidget(self.lastTime)
        l311.setStretchFactor(createLabel, 1)
        l311.setStretchFactor(self.createTime, 3)
        l311.setStretchFactor(lastLabel, 1)
        l311.setStretchFactor(self.lastTime, 3)
        l311.setContentsMargins(0, 0, 0, 0)

        l312 = QHBoxLayout()
        l312.addWidget(nameLabel)
        l312.addWidget(self.nameEd)
        l312.addWidget(otherBu)
        l312.addStretch(7)
        l312.setStretchFactor(nameLabel, 2)
        l312.setStretchFactor(self.nameEd, 9)
        l312.setStretchFactor(otherBu, 3)
        l312.setContentsMargins(0, 0, 0, 0)

        l313 = QHBoxLayout()
        l313.addWidget(cateLable)
        l313.addWidget(self.category)
        l313.addStretch(7)
        l313.setStretchFactor(cateLable, 1)
        l313.setStretchFactor(self.category, 2)
        l313.setContentsMargins(0, 0, 0, 0)

        l314 = QHBoxLayout()
        l314.addLayout(ylayout)
        l314.addWidget(self.zhaijiEd)
        l314.setContentsMargins(0, 0, 0, 0)

        l315 = QHBoxLayout()
        l315.addLayout(ylayout1)
        l315.addWidget(self.pingZhuEd)

        l31.setContentsMargins(0, 0, 5, 0)
        l31.addRow(l311)
        l31.addRow(l312)
        l31.addRow(l313)
        l31.addRow(l314)
        l31.addRow(l315)
        ww3.setLayout(l31)

        layout3.setContentsMargins(5, 5, 5, 5)
        layout3.addWidget(ww3)

        mainlayout.addLayout(layout1)
        ww2.setLayout(layout2)
        llt = QHBoxLayout()
        llt.addWidget(ww2)
        mainlayout.addLayout(llt)
        llt.setContentsMargins(5, 5, 5, 5)

        mainlayout.addLayout(layout3)
        mainlayout.setStretchFactor(layout1, 1)
        mainlayout.setStretchFactor(layout2, 2)
        mainlayout.setStretchFactor(layout3, 4)

        ww0.setLayout(mainlayout)
        layout0.addWidget(menuList)
        layout0.addWidget(ww0)

        ww.setLayout(layout0)
        self.setCentralWidget(ww)

    def searchfile(self):
        text = self.searchEd.text()
        pattern = r'^.*' + text + r'.*$'
        li = []
        message = QMessageBox
        if self.tll.count() == 0:
            message.warning(self, "错误", "没有可供选择的项")
        else:
            if not self.cli:
                self.tll.clear()
                print("in")
                for i in range(self.listtemp.count()):
                    self.tll.addItem(self.listtemp.item(i))
            self.listtemp.clear()
            for i in range(self.tll.count()):
                self.listtemp.addItem(self.tll.item(i))
                if re.match(pattern, self.tll.item(i).text()):
                    li.append(self.tll.item(i).text())
            self.tll.clear()
            self.cli = False
            for l in li:
                item = QListWidgetItem()
                item.setText(l)
                self.tll.addItem(item)

    # def toword(self):
    #     path,_ = QFileDialog.getSaveFileName(self, "转为word", "", "doc files (*.doc);;")
    #     document = Document()
    #     table = document.add_table(rows=7, cols=2)
    #     yy = ['创建时间', '更新时间', '书名', '类型', '作者', '出版社', '出版时间']
    #     i = 0
    #     for y in yy:
    #         table.cell(i, 0).text = y
    #         table.cell(i, 1).text = self.kk[i]
    #         i += 1
    #         if i == 4:
    #             break
    #     while i < 7:
    #         table.cell(i, 0).text = yy[i]
    #         table.cell(i, 1).text = self.kk[i + 2]
    #         i += 1
    #     document.add_heading('摘记', level=4)
    #     zhaiji = document.add_paragraph(self.kk[4])
    #     document.add_heading('评注', level=4)
    #     pingzhu = document.add_paragraph(self.kk[5])
    #     document.save(path)

    def importfile(self):
        reply = QMessageBox.question(self, '警告', '该操作将覆盖原有数据，是否继续？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            filepath, _ = QFileDialog.getOpenFileName(self, "导入数据", "./", "Out files(*.out)")
            if filepath == '':
                return
            zzipfile = zipfile.ZipFile(filepath, 'r')
            files = os.listdir('./data/')
            for file in files:
                self.remove(os.path.join('./data', file))
            os.mkdir('./data')
            for name in zzipfile.namelist():
                data = zzipfile.read(name)
                saveDir = os.path.dirname('./data/' + name)
                if not os.path.exists(saveDir):
                    os.makedirs(saveDir)
                file = open('./data/' + name, 'w+b')
                file.write(data)
                file.close()
            zzipfile.close()
            self.thenew()
            self.getCategory()

    def remove(self, file):
        if os.path.isdir(file):
            ffs = os.listdir(file)
            for ff in ffs:
                self.remove(os.path.join(file, ff))
            if os.path.exists(file):
                os.removedirs(file)
        else:
            if os.path.exists(file):
                os.remove(file)

    def delfile(self):
        self.dd = DelWindow()
        self.dd.setWindowTitle("删除笔记")
        self.dd.resize(480, 272)
        self.dd.setStyleSheet("font-size:20px;font-style:SansSerif")
        self.dd.work()
        self.dd.myclick.connect(self.oo)

    @QtCore.pyqtSlot(str)
    def oo(self, str):
        print("getit")
        self.tll.clear()

    def exportfile(self):
        output_filename, _ = QFileDialog.getSaveFileName(self, "数据备份", "", "out files (*.out);;")
        if output_filename == "":
            return
        self.zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname("./data/"))
        for parent, dirnames, filenames in os.walk("./data/"):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                print(pathfile, arcname)
                self.zipf.write(pathfile, arcname)
        self.zipf.close()

    def thenew(self):
        self.createTime.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        self.lastTime.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        self.nameEd.setText("")
        self.category.setCurrentIndex(0)
        self.zhaijiEd.setText("")
        self.pingZhuEd.setText("")
        self.thesave = ''
        self.filePath = ''
        if self.bookin is not None:
            self.bookin.deleteLater()

    @QtCore.pyqtSlot(str)
    def ss(self, str):
        self.theinfo = str
        self.bookin.deleteLater()
        self.bookin = None
        

    def info(self):
        self.bookin = BookInfo(self.theinfo.split('&&'))
        self.bookin.setStyleSheet("font-size:20px;font-style:SansSerif")
        self.bookin.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.bookin.work()
        self.bookin.myclick.connect(self.ss)

    def scanCategory(self):
        fo = open(self.categoryPath, 'r')
        stri = fo.read()
        fo.close()
        kk = stri.split('&&')
        self.delCategory()
        for k in kk:
            item = QTreeWidgetItem()
            item.setText(0, k)
            self.categoryTree.addChild(item)
            ttz = os.path.join('./data/his', k)
            if not os.path.exists(ttz):
                os.mkdir(ttz)
        files = os.listdir("./data/his/")
        for file in files:
            if file not in kk:
                self.remove("./data/his/" + file)
        

    def delCategory(self):
        self.treelist.clear()
        self.categoryTree = QTreeWidgetItem()
        self.categoryTree.setText(0, "全部类别")
        self.treelist.addTopLevelItem(self.categoryTree)

    def save(self):
        self.pingZhuEd.append('-----添加于' + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + '-----')
        self.zhaijiEd.append('-----添加于' + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + '-----')
        self.bookname = self.nameEd.text()
        self.cate = self.category.currentText()
        self.zhai = self.zhaijiEd.toPlainText()
        self.ping = self.pingZhuEd.toPlainText()
        self.ftime = self.createTime.text()
        self.ltime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        self.thesave = self.ftime + '&&' + self.ltime + '&&' + self.bookname + '&&' + self.cate + '&&' + self.zhai + '&&' + self.ping + '&&' + self.theinfo
        print(self.filePath)
        self.lastTime.setText(self.ltime)
        message = QMessageBox()
        if self.bookname == "":
            message.warning(self, '错误', '书名不能为空')
        else:
            if self.filePath is '':
                self.filePath = './data/his/' + self.cate + '/' + self.bookname + '.io'
            else:
                if self.tttt != self.cate:
                    reply = QMessageBox.question(self, '警告', '类别发生改变，将在新选择类别下生成新的笔记！', QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        if os.path.exists(self.filePath):
                            os.remove(self.filePath)
                        self.filePath = './data/his/' + self.cate + '/' + self.bookname + '.io'
                    else:
                        return
                if self.ttttname != self.bookname:
                    reply = QMessageBox.question(self, '警告', '书名发生改变，将生成新的书籍笔记！', QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        if os.path.exists(self.filePath):
                            os.remove(self.filePath)
                        self.filePath = './data/his/' + self.cate + '/' + self.bookname + '.io'
                    else:
                        return
            if self.filePath is '':
                return
            fo = open(self.filePath, 'w')
            fo.write(self.thesave)
            fo.close()
            message = QtWidgets.QMessageBox(self)
            message.information(self, '提示', '笔记保存成功')
    def checkFile(self):
        self.cli = True
        item = QtWidgets.QTreeWidgetItemIterator(self.categoryTree)
        while item.value():
            if item.value().isSelected():
                if item.value().text(0) != '全部类别':
                    self.ppp = self.FindPath + item.value().text(0) + '/'
                    if os.path.exists(self.ppp):
                        self.files = os.listdir(self.ppp)
                    else:
                        os.makedirs(self.ppp)
                        self.files = os.listdir(self.ppp)
                    self.updateList()

                break
            item = item.__iadd__(1)

    def updateList(self):
        self.tll.clear()
        if self.files is not None:
            for name in self.files:
                item = QListWidgetItem()
                item.setText(name.split('.')[0])
                self.tll.addItem(item)

    def open(self):
        for i in range(self.tll.count()):
            if self.tll.item(i).isSelected():
                self.filePath = self.ppp + self.tll.item(i).text() + '.io'
                print(self.filePath)
                fo = open(self.filePath, 'r')
                stri = fo.read()
                fo.close()
                self.kk = stri.split('&&')
                self.updatezzz()
                break
        

    def updatezzz(self):
        self.createTime.setText(self.kk[0])
        self.lastTime.setText(self.kk[1])
        self.nameEd.setText(self.kk[2])
        self.ttttname = self.kk[2]
        self.category.setCurrentText(self.kk[3])
        self.tttt = self.kk[3]
        self.zhaijiEd.setText(self.kk[4])
        self.pingZhuEd.setText(self.kk[5])
        i = 6
        self.theinfo = ''
        while i < 10:
            self.theinfo = self.theinfo + self.kk[i] + '&&'
            i += 1
        self.theinfo = self.theinfo[:len(self.theinfo) - 2]

    def change(self):
        self.chage = ChangeWindow()
        self.chage.setStyleSheet("font-size:20px;font-style:SansSerif")
        self.chage.work()
        self.chage.myclicked.connect(self.getCategory)

    def getCategory(self):
        self.category.clear()
        fo = open(self.categoryPath, 'r')
        stri = fo.read()
        fo.close()
        kk = stri.split('&&')
        for k in kk:
            self.category.addItem(k)
        self.scanCategory()

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
        self.path = os.path.abspath('./data/file/category.io')
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
        addfl.setMinimumHeight(40)
        addfl.clicked.connect(self.addflag)

        delfl = QtWidgets.QPushButton()
        delfl.setText("删除选中")
        delfl.setObjectName("addflag")
        delfl.setMinimumHeight(40)
        delfl.clicked.connect(self.delflag)

        back = QtWidgets.QPushButton()
        back.setText("确  认")
        back.setObjectName("back")
        back.setMinimumHeight(40)
        back.clicked.connect(self.backMain)

        causel = QtWidgets.QPushButton()
        causel.setText("取  消")
        causel.setObjectName("causel")
        causel.setMinimumHeight(40)
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

class BookInfo(QWidget):
    myclick = QtCore.pyqtSignal(str)

    def __init__(self, kk=None):
        QWidget.__init__(self)
        if kk is not None:
            self.auth = kk[0]
            self.Make = kk[1]
            self.time = kk[2]
            self.path = kk[3]
        else:
            self.auth = ''
            self.Make = ''
            self.time = ''
            self.path = ''
        self.setupUi()

    def setupUi(self):
        self.resize(300, 160)
        self.setWindowTitle("书籍详细信息")
        self.editList = []
        laList = []
        labelList = []
        kk = ['作者    ', '出版社  ', '出版时间', '选择文件']
        i = 0
        while i < 4:
            edit = QLineEdit()
            self.editList.append(edit)
            lla = QHBoxLayout()
            laList.append(lla)
            i += 1
        for k in kk:
            lab = QLabel(k)
            labelList.append(lab)
        i = 0
        for lab in laList:
            lab.addWidget(labelList[i])
            if i < 3:
                lab.addWidget(self.editList[i])
            i += 1
        lala = QVBoxLayout()
        fileBu = QPushButton('选择文件')
        fileBu.setMinimumHeight(40)
        sureBu = QPushButton('确  定')
        sureBu.setMinimumHeight(40)
        sureBu.clicked.connect(self.sure)
        cancellBu = QPushButton('取  消')
        cancellBu.setMinimumHeight(40)
        cancellBu.clicked.connect(self.cancel)
        la = QHBoxLayout()
        la.addWidget(sureBu)
        la.addStretch(1)
        la.addWidget(cancellBu)
        laList.append(la)
        self.filename = MyLabel(path=self.path)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.blue)
        self.filename.setPalette(pe)
        laList[3].addWidget(self.filename)
        laList[3].addStretch(1)
        laList[3].addWidget(fileBu)
        self.editList[0].setText(self.auth)
        self.editList[1].setText(self.Make)
        self.editList[2].setText(self.time)
        self.filename.setText(os.path.basename(self.path))
        for lab in laList:
            lala.addLayout(lab)
        # laList[]
        fileBu.clicked.connect(self.findfile)
        self.setLayout(lala)

    def sure(self):
        self.auth = self.editList[0].text()
        self.Make = self.editList[1].text()
        self.time = self.editList[2].text()
        stri = self.auth + '&&' + self.Make + '&&' + self.time + '&&' + self.path
        self.myclick.emit(stri)
        self.close()

    def cancel(self):
        self.close()

    def findfile(self):
        self.path, _ = QFileDialog.getOpenFileName(self, 'Open file')
        self.filename.setText(os.path.basename(self.path))
        self.filename.path = self.path

    def oo(self):
        os.system(self.path)

    def work(self):
        if not self.isVisible():
            self.show()

class MyLabel(QLabel):
    path = ''
    
    def __init__(self, parent=None, path=None):
        super(MyLabel, self).__init__(parent)
        self.path = path

    def mouseDoubleClickEvent(self, e):
        print(self.path)
        os.system(self.path)


class DelWindow(QWidget):
    myclick = QtCore.pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.filPre = "./data/his/"
        self.pathList = []
        self.setupUi()

    def setupUi(self):
        self.fileList = QListWidget()
        files = os.listdir(self.filPre)
        for file in files:
            ffs = os.listdir(self.filPre + file)
            for ff in ffs:
                item = QListWidgetItem()
                item.setText(ff.split(".")[0])
                item.setCheckState(QtCore.Qt.Unchecked)
                self.pathList.append(self.filPre + file + '/' + ff)
                self.fileList.addItem(item)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.fileList)
        layout1 = QHBoxLayout()
        yeah = QPushButton('确  认')
        yeah.setMinimumHeight(40)
        yeah.clicked.connect(self.gogogo)
        cancell = QPushButton('取  消')
        cancell.setMinimumHeight(40)
        cancell.clicked.connect(self.close)
        layout1.addWidget(yeah)
        layout1.addWidget(cancell)
        mainLayout.addLayout(layout1)
        self.setLayout(mainLayout)
    

    def gogogo(self):
        for i in range(self.fileList.count()):
            print(self.fileList.item(i).checkState())
            if self.fileList.item(i).checkState() == QtCore.Qt.Checked:
                os.remove(self.pathList[i])
                pass
        self.myclick.emit(' ')
        self.close()
        

    def work(self):
        if not self.isVisible():
            self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
