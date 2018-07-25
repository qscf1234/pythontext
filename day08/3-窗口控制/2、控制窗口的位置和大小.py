import win32con  # 定义
import win32gui  # 界面
import random

# 找出窗体的编号               类              标题
# QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
# 参数1 ：控制的窗体
# 参数2：大致方位  HWND_TOPMOST上方
# 参数3: 位置X
# 参数4: 位置Y
# 参数5: 长度
# 参数6: 宽度
# win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 100, 100, 300, 300, win32con.SWP_SHOWWINDOW)

while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    x = random.randrange(600)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y, 300, 300, win32con.SWP_SHOWWINDOW)
