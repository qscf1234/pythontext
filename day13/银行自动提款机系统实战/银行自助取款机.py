'''
分析：
人
类名：Person
属性：姓名，身份证号，电话号，卡
行为：

卡
类名：Card
属性：卡号，密码，余额
行为：

银行
类名：bank
属性：用户列表，提款机
行为：


提款机:
类名：ATM
属性：
行为：卡户，查询，取款，存储，转账，锁定，解锁，补卡，销户，退出

界面：
类名：View
属性：
行为：管理员登录，管理员界面，系统功能界面

'''
import os
from admin import Admin
from atm import ATM
import pickle

def main():
    # 管理员对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1
    # 提款机对象
    filepath = os.path.join(os.getcwd(), "allusers1.txt")
    if not os.path.isfile(filepath):
        with open(filepath, 'a') as f1:
            pass
    f = open(filepath, "rb")
    if not f.readline():
        allUsers = {}
    else:
        f.seek(0)
        allUsers = pickle.load(f)
    print("*******")
    print(allUsers)
    atm = ATM(allUsers)
    while True:
        admin.sysFunctionView()
        # 等待用户的操作
        option = input("请输入您的操作：")
        if option == "1":
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            print("存储")
            atm.saveMoney()
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            print("补卡")
        elif option == "0":
            print("销户")
        elif option == "t":
            if not admin.adminOption():
                # 将当前系统中的用户信息保存到文件中
                f = open(filepath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1

if __name__ == "__main__":
    main()
