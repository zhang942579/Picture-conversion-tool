from .OCRServe import OCRServe
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import os
import imghdr
import pyperclip
from .Ui_MainWindow import Ui_MainWindow
from .MessageBox import MessageBox

"""
程序主要逻辑与应用
"""


class app(MessageBox, Ui_MainWindow):

    def __init__(self, parent=None):
        self.is_internet = True
        super().__init__(parent)
        self.filename = None
        self.setupUi(self)
        self.slot_init()
        self.OcrServe = OCRServe()

    def slot_init(self):
        self.change.clicked.connect(self.clicked_change)
        self.add.clicked.connect(self.clicked_add)
        self.delete.clicked.connect(self.clicked_delete)
        self.reduction.clicked.connect(self.clicked_reduction)
        self.output.clicked.connect(self.clicked_edit)
        self.copy.clicked.connect(self.clicked_copy)

    def clicked_change(self):
        if(self.is_internet):
            self.is_internet = False
            self.show_Tips("已经切换为离线模式")
        else:
            self.is_internet = True
            self.show_Tips("已经切换为联网模式")

    def clicked_add(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;*.jpg;;*.png;;*.jpeg;;*.bmp")
        if len(filename[0]) == 0:
            self.show_error("请选择文件")
        else:
            self.filename = filename[0][0]
            if imghdr.what(self.filename) is None:
                self.show_Tips("请选择正确的文件(jpg、png···)")
            else:
                self.Image.setPixmap(QtGui.QPixmap(self.filename).scaled(self.Image.width(), self.Image.height()))

                text = self.OcrServe.to_word(self.filename, self.is_internet)
                if text is None:
                    return
                for i in text:
                    self.Text.append(i)

    def clicked_delete(self):
        tips = self.show_Tips("确认清除照片吗？")
        if tips == QMessageBox.Yes:
            self.Image.setPixmap(QPixmap(""))
        else:
            return

    def clicked_reduction(self):
        tips = self.show_Tips("确认清除文本吗？")
        if tips == QMessageBox.Yes:
            self.Text.clear()
        else:
            return

    def clicked_edit(self):
        return

    def clicked_copy(self):
        pyperclip.copy(self.Text.toPlainText())

    def closeEvent(self, event):  # 关闭窗口触发以下事件
        a = QMessageBox.question(self, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QMessageBox.Yes:
                event.accept()  # 接受关闭事件
        else:
                event.ignore()  # 忽略关闭事件
