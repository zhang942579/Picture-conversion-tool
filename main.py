from PyQt5 import QtWidgets
import sys
from Resource import app
"""
启动文件
"""

if __name__ == '__main__':

    ap = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    ui = app()  # 实例化Game_UI
    ui.show()  # 调用ui的show()以显示。同样show()是源于父类QtWidgets.QWidget的
    sys.exit(ap.exec_())  # 不加这句，程序界面会一闪而过
