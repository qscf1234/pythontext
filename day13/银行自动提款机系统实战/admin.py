import time
class Admin(object):
    admin = '1'
    passwd = '1'
    def printAdminView(self):
        print("*****************************************************************")
        print('*                                                               *')
        print('*                                                               *')
        print('*                         登录我的银行                          *')
        print('*                                                               *')
        print('*                                                               *')
        print("*****************************************************************")

    def sysFunctionView(self):
        print("*****************************************************************")
        print("*        开户(1)                            查询(2)             *")
        print("*        取款(3)                            存款(4)             *")
        print("*        转账(5)                            改密(6)             *")
        print("*        锁定(7)                            解锁(8)             *")
        print("*        补卡(9)                            销户(0)             *")
        print("*                         退出(t)                               *")
        print("*****************************************************************")

    def adminOption(self):
        inputAdmin = input('请输入管理员账号：')
        if self.admin != inputAdmin:
            print('账号输入有误')
            return -1
        inputPasswd = input('请输入管理员密码：')
        if self.passwd != inputPasswd:
            print('密码输入错误')
            return -1
        print('操作成功请稍后.......')
        time.sleep(1)
        return 0
    def adminquit(self):
        if self.adminOption():
            return -1
        else:
            return 0
