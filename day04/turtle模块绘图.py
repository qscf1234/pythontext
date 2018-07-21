'''
简单的绘图工具
提供一个小海龟，可以理解为一个机器人，只能听得懂有限的命令

绘图窗口的原点（0，0）在正中间，默认海龟的方向向右侧

运动命令
forward(d)     向前移动d长度
backward（d） 向后移动d长度
right(d)      向右转动d度
left(d)       向左转动d度
goto(x,y)     移动到坐标为（x,y）的位置
speed(d)      笔画速度为[0,10]
circle(radius, extent = None, steps = None)   绘制一个圆，r为半径，e为角度，steps为几就是几边形


笔画控制命令
up()           笔画抬起，在移动的时候不会画图
down()         笔画落下，移动会绘图
setheading()   改变海龟的朝向
pensize(d)     笔画的宽度
pencolor()     笔画的颜色
reset()        清空窗口，恢复所有设置，重置turtle状态
clear()        清空窗口
begin_fill()
fillcolor(colorstr)
end_fill()

其他命令
done()         程序继续执行
undo()         撤销上一次动作
hideturtle()   隐藏海龟
showturtle()   显示海龟
screensize(self, canvwidth=None, canvheight=None, bg=None)
               宽度，高度，开始的颜色。。。。。。。
'''
# 导入turtle库
import turtle
turtle.screensize(2000,1500)
turtle.forward(100)
# turtle.right(45)
# turtle.backward(200)
# turtle.goto(-100, -200)
# turtle.circle(50, steps=5)
turtle.done()
