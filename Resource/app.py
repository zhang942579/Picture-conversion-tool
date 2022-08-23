from .OCRServe import OCRServe
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import os
import imghdr
import pyperclip
from .Ui_MainWindow import Ui_MainWindow


class app(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
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
        return

    def clicked_add(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;*.jpg;;*.png;;*.jpeg;;*.bmp")
        if len(filename[0]) == 0:
            self.show_error("请选择文件")
        else:
            self.filename = filename[0][0]
            if imghdr.what(self.filename) is None:
                self.show_Tips("请选择正确的文件(jpg、png···)")
                print(imghdr.what(self.filename))
            else:
                print('成功')
                self.Image.setPixmap(QtGui.QPixmap(self.filename).scaled(self.Image.width(), self.Image.height()))
                text = self.OcrServe.to_word(self.filename)
                if text is None:
                    return
                for i in text.result.words_block_list:
                    self.Text.append(i.words)

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

    def show_Tips(self, msg):
        return QMessageBox.information(self, "提示", msg, QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

    def show_error(self, msg):
        QMessageBox.critical(self, "错误", msg)

    def show_warning(self, msg):
        QMessageBox.warning(self, "警告", msg, QMessageBox.Cancel)