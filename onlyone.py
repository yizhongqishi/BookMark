# -*- coding:utf-8 -*-
# created by CYMX on 17/9/1

# 文件创建时间：theFirst   最后一次保存时间：theLast
# 附件选择按钮  导出为word文件
import os
import sys
import time
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

qtCreatorFile = "mainwindow.ui"  # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.path = ''
        self.theinfo = '&&&&&&'
        self.thesave = ''
        self.bookin = None
        self.setWindowTitle("书籍摘录助手")
        self.nonono.clicked.connect(self.close)
        createAction = QAction('&新建', self)
        createAction.setShortcut('Ctrl+N')
        createAction.setStatusTip('新建摘录')
        createAction.triggered.connect(self.theNew)
        openAction = QAction('&打开', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.theOpen)
        exportAction = QAction('导出 ', self)
        createAction.triggered.connect(self.theExport)
        fileMenu = self.menuBar.addMenu("&文件")
        fileMenu.addAction(createAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exportAction)
        self.yeah.clicked.connect(self.save)
        self.updateTime()
        self.changeCategory.clicked.connect(self.change)
        self.bookInfo.clicked.connect(self.info)
        self.catepath = os.path.abspath('./file/category.io')
        self.getCategory()

    def save(self):
        self.bookname = self.bookName.text()
        self.cate = self.category.currentText()
        self.zhai = self.zhaiji.toPlainText()
        self.ping = self.pingzhu.toPlainText()
        self.ftime = self.theFirst.text()
        self.ltime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        self.thesave = self.ftime + '&&' + self.ltime + '&&' + self.bookname + '&&' + self.cate + '&&' + self.zhai + '&&' + self.ping + '&&'+self.theinfo
        print(self.path)
        self.theLast.setText(self.ltime)
        if self.path is '':
            self.path, _ = QFileDialog.getSaveFileName(self, 'save file', "saveFile", "io files (*.io);;all files(*.*)")
        if self.path is '':
            return
        fo = open(self.path, 'w')
        fo.write(self.thesave)
        fo.close()

    def info(self):
        self.bookin = BookInfo(self.theinfo.split('&&'))
        self.bookin.work()
        self.bookin.myclick.connect(self.ss)

    @QtCore.pyqtSlot(str)
    def ss(self, str):
        self.theinfo = str
        self.bookin.deleteLater()
        pass

    def updateTime(self):
        self.theFirst.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        self.theLast.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

    # 导出为word格式
    def theExport(self):
        pass

    # 打开文件
    def theOpen(self):
        self.path, _ = QFileDialog.getOpenFileName(self, 'Open file', filter="IO Files (*.io)")
        if self.path is '':
            return
        fo = open(self.path, 'r')
        stri = fo.read()
        fo.close()
        kk = stri.split('&&')
        self.theFirst.setText(kk[0])
        self.theLast.setText(kk[1])
        self.bookName.setText(kk[2])
        self.category.setCurrentText(kk[3])
        self.zhaiji.setText(kk[4])
        self.pingzhu.setText(kk[5])
        i = 6
        self.theinfo = ''
        while i < 10:
            self.theinfo = self.theinfo + kk[i] + '&&'
            i += 1
        self.theinfo = self.theinfo[:len(self.theinfo) - 2]
        pass

    # 从数据库中查询所有标签，并且默认显示
    @QtCore.pyqtSlot()
    def getCategory(self):
        self.category.clear()
        fo = open(self.catepath, 'r')
        stri = fo.read()
        fo.close()
        kk = stri.split('&&')
        for k in kk:
            self.category.addItem(k)


    def theNew(self):
        self.theFirst.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        self.theLast.setText(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        self.bookName.setText("")
        self.category.setCurrentIndex(0)
        self.zhaiji.setText("")
        self.pingzhu.setText("")
        self.thesave = ''
        self.path = ''
        if self.bookin is not None:
            self.bookin.deleteLater()

    def change(self):
        self.chage = ChangeWindow()
        self.chage.work()
        self.chage.myclicked.connect(self.getCategory)

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
        back.setText("返  回")
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
        sureBu = QPushButton('确  定')
        sureBu.clicked.connect(self.sure)
        cancellBu = QPushButton('取  消')
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
        stri = self.auth+'&&'+self.Make+'&&'+self.time+'&&'+self.path
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
