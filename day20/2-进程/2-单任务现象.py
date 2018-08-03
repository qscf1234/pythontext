from time import sleep

def run():
    while True:
        print('sunck is a nice man')
        sleep(1)

if __name__ == '__main__':
    while True:
        print('sunck is a good man')
        sleep(1)
    # 不会执行到run方法，只有上面的while循环结束才可以执行
    run()
