import win32con  # 定义
import win32gui  # 界面
import time  # 时间

# 找出窗体的编号               类              标题
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

# 隐藏窗体
# win32gui.ShowWindow(QQWin, win32con.SW_HIDE)

# 显示窗体
# win32gui.ShowWindow(QQWin, win32con.SW_SHOW)

while True:
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(1)
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(1)

