from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets


class MessageBox(QtWidgets.QMainWindow):
    def show_Tips(self, msg):
        return QMessageBox.information(self, "提示", msg, QMessageBox.Yes | QMessageBox.No)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

    def show_error(self, msg):
        QMessageBox.critical(self, "错误", msg)

    def show_warning(self, msg):
        QMessageBox.warning(self, "警告", msg, QMessageBox.Cancel)