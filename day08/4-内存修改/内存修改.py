import win32process # 进程模块
import win32con # 系统定义
import win32api # 调用系统模块
import ctypes # c语言类型
import win32gui #界面
import time

# 系统常量，标识最高权限打开一个进程
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF) # |位运算， 0x 十六进制

window = win32gui.FindWindow("MainWindow","植物大战僵尸中文版") # 查找窗体

# 根据窗体抓取进程编号（pid 是进程编号 hid和pid一般描述一个进程信息）
hid, pid = win32process.GetWindowThreadProcessId(window)

# phand 打开一个进程（参数意思是使用最高权限非安全打这个进程）
phand = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
print(phand)
# c语言整数类型，读取数据
date = ctypes.c_long()

# 调用系统内核模块(Kerne123.dll windows内核)
mydll = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32.dll")


while True:
    # 读取内存(“4”表示占4个字节，types.byref(date)表示转递地址信息，写入的结果到date中)
    # int(phand)打开的进程编号   “411410192”需要读取的内存的地址
    mydll.ReadProcessMemory(int(phand), 411410192, ctypes.byref(date), 4, None)

    # 将读取到的内存输出 （可以获取内存中对应的数据）
    print(date.value)

    if date.value < 2450:
        newdata = ctypes.c_long(2450) # 设定修改的数据
        mydll.WriteProcessMemory(int(phand), 411410192, ctypes.byref(newdata), 4, None)
    time.sleep(1)
