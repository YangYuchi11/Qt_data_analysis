import sys
from common import get_messages
import matplotlib.pyplot as plt
from localization_pb2 import Localization  # 导入你的 Protobuf 生成的 Python 类
from chassis_info_pb2 import ChassisInfo  
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtCore
from Ui_Mainwindow import Ui_MainWindow  # 导入生成的 UI 类

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面
        self.initUI()
        self._file_name = ""

    def initUI(self):
        # 设置按钮点击事件
        self.pushButton.clicked.connect(self.show_position_plot)  # 位置图按钮
        self.pushButton_2.clicked.connect(self.show_speed_plot)  # 速度图按钮
        self.pushButton_3.clicked.connect(self.show_ab_error_plot)  # AB误差图按钮
        self.actionopen.triggered.connect(self.open_file)  # 打开文件菜单项

    def show_position_plot(self):
        QMessageBox.information(self, "位置图", "生成位置图的功能")
        
        if self._file_name == "":
            QMessageBox.information(self, "位置图", "请先打开文件")
            return
        
        x = []
        heading = []
        count = 0  # 修正了拼写错误 conunt -> count
        
        # 读取消息（get_messages 返回的是 Protobuf 消息的二进制列表）
        messages = get_messages(self._file_name)
        
        for message in messages:
            # 反序列化 Protobuf 消息
            localization = Localization()  # 使用正确的生成类
            try:
                localization.ParseFromString(message)
            except Exception as e:
                print(f"Protobuf 反序列化失败: {e}")
                return
            
            # 处理数据：检查 ENU 和 header 信息
            if localization.HasField('enu') and localization.HasField('header') and localization.header.module_name == 'Localization':
                count += 1
                x.append(count)  # 记录 X 轴数据
                heading.append(localization.enu.theta)  # 记录 Y 轴数据（航向角）

        # 绘制图形
        plt.plot(x, heading, label="Heading")
        plt.title("Position Heading Plot")  # 设置标题
        plt.xlabel("Index (X)")  # 设置 X 轴标签
        plt.ylabel("Heading")  # 设置 Y 轴标签
        plt.grid(True)  # 显示网格
        plt.legend()  # 显示图例
        plt.show()  # 显示图形


    def show_speed_plot(self):
        QMessageBox.information(self, "方向盘角度", "已完成方向盘角度的绘制")
        
        if self._file_name == "":
            QMessageBox.information(self, "方向盘角度", "请先打开文件")
            return
        
        x = []
        elec = []
        pose = []
        speed = []
        count = 0  
        
        # 读取消息（get_messages 返回的是 Protobuf 消息的二进制列表）
        messages = get_messages(self._file_name)
        
        for message in messages:
            # 反序列化 Protobuf 消息
            chassis_info = ChassisInfo()  # 使用正确的生成类
            try:
                chassis_info.ParseFromString(message)
            except Exception as e:
                print(f"Protobuf 反序列化失败: {e}")
                return
            
            # 处理数据：检查 ENU 和 header 信息
            if chassis_info.HasField('chassis') and chassis_info.HasField('header') and chassis_info.header.module_name == 'ChassisInfo':
                count += 1

        # 绘制图形
        plt.plot(x, heading, label="Heading")
        plt.title("Position Heading Plot")  # 设置标题
        plt.xlabel("Index (X)")  # 设置 X 轴标签
        plt.ylabel("Heading")  # 设置 Y 轴标签
        plt.grid(True)  # 显示网格
        plt.legend()  # 显示图例
        plt.show()  # 显示图形

    def show_ab_error_plot(self):
        QMessageBox.information(self, "AB误差图", "生成AB误差图的功能")

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        if file_name:
            self.Filelabel.setText(f"已打开文件: {file_name}")
            self._file_name = file_name
