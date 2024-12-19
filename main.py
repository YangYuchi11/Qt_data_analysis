import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow  # 导入我们修改后的 MainWindow 类

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建主窗口实例
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 启动事件循环
