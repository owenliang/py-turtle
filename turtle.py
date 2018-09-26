import turtle

# 坐标系模式改为scratch模式
turtle.mode('logo')

# 位置
#position = turtle.position()

# 前进
#turtle.forward(100)

# 后退
#turtle.backward(100)

# 右转
#turtle.right(90)

# 左转
#turtle.left(45)

# 移动到(x,y)
#turtle.goto(10, 10)

# 移动到x
#turtle.setx(20)

# 移动到y
#turtle.sety(50)

# 设置方向
#turtle.setheading(270)

# 回到原点(0,0), 方向为90°
#turtle.home()

# 画圆(半径,画多少角度,一共几笔画完)
#turtle.circle(50, 360, 2)

# 画点(大小,颜色)
#turtle.dot(20, 'blue')

# 盖章
#stamp_id = turtle.stamp()
#turtle.forward(100)

# 消除盖章
#turtle.clearstamp(stamp_id)

# 修改运动速度
turtle.speed(1)

# 撤销操作
#turtle.forward(100)
#turtle.undo()

# 小乌龟面向的方向转到towards的直线之间的夹角度数
#turtle.goto(100,100)
#turtle.goto(-100,100)
#print(turtle.towards(0, 0))

# 获取x,y坐标
#turtle.goto(10, 12)
#print(turtle.xcor())
#print(turtle.ycor())

# 获取面向的角度
#print(turtle.heading())

# 乌龟到(x,y)的距离
#print(turtle.distance((30, 40)))

# 抬笔与落笔
#turtle.penup()
#turtle.goto(100,100)
#turtle.down()

# 获取与配置笔的属性
#pen = turtle.pen()
#print(pen)
#turtle.pen(pen, pencolor = 'pink', fillcolor = 'pink')
#turtle.goto(100,100)

# 判断笔是否落下
#if turtle.isdown():
#    turtle.goto(100, 100)

# 修改画笔轮廓颜色
#turtle.pencolor("pink")
#turtle.goto(100, 100)
#print(turtle.pen())

# 修改画笔填充图案的颜色
#turtle.fillcolor("pink")
#turtle.goto(100, 100)

# 修改画笔颜色(同时修改pencolor与fillcolor)
#turtle.color("pink")
#turtle.goto(100, 100)

# 填充图案
#turtle.color("blue", "pink")
#turtle.begin_fill()
#if turtle.filling():
#    turtle.circle(80, 360, 4)
#    turtle.end_fill()

# 重置小乌龟
#turtle.reset()

# 清除屏幕上所有画笔痕迹, 小乌龟不动
#turtle.goto(100,100)
#turtle.clear()

# 写字
#turtle.penup()
#turtle.write('大家好', True, 'Center', ('宋体',18,'normal'))

# 隐藏/显式小乌龟
#turtle.hideturtle()
#turtle.goto(100,100)
#if not turtle.isvisible():
#    turtle.showturtle()

# 改变小乌龟的形状
#turtle.shape('circle')

# 改变小乌龟的大小(不会改变画笔的大小)
#turtle.resizemode("user")
#turtle.turtlesize(2, 2, 2)
#turtle.goto(100, 100)

# 扭曲小乌龟
#turtle.shearfactor(0.2)
#turtle.forward(100)

# 旋转小乌龟图案一定角度, 但不改变其朝向
#turtle.tilt(90)
#turtle.forward(100)

# 获取或者设置小乌龟图案的角度, 不改变朝向
#turtle.tiltangle(90)
#turtle.forward(100)

# 小乌龟的点击事件
#def onclick(x, y):
#    turtle.clear()
#    turtle.home()
#    turtle.write((x,y))
#turtle.onclick(onclick)

# 小乌龟的鼠标松开事件
#def onrelease(x, y):
#    turtle.write('release')
#turtle.onrelease(onrelease)

# 小乌龟的鼠标拖拽事件
#def ondrag(x, y):
#    print(x,y)
#turtle.ondrag(ondrag)

# 获取屏幕screen
#screen = turtle.getscreen()
#print(screen)

# 设置背景颜色
#turtle.bgcolor('orange')

# 设置背景图片
#turtle.bgpic("landscape.gif")

# 设置screen大小+window大小
#turtle.screensize(400, 400, 'orange')
#turtle.setup(width = 400, height = 400)
#turtle.forward(200)

# 设置screen的坐标系大小(宽度100px,高度15px)
#turtle.setworldcoordinates(-50,-7.5,50,7.5)
#turtle.left(90)
#turtle.forward(7)

# 每次绘画动作的延迟时间
#turtle.delay(100)
#turtle.goto(100,100)

# 监听键盘松开
#def onkeyrelease():
#    turtle.forward(10)
#turtle.onkey(onkeyrelease, 'space')

# 监听键盘按下
#def onkeypress():
#    turtle.forward(10)
#turtle.onkey(onkeypress, 'space')

# 监听点击事件
#def onclick(x,y):
#    print(x,y)
#turtle.onscreenclick(onclick)

# 收集按键事件
#turtle.listen()

# 定时器
#def ontimer():
#    turtle.forward(10)
#    turtle.ontimer(ontimer, 1000)
#ontimer()

# 输入文本
#name = turtle.textinput('你的名字', '请输入')
#turtle.write(name)

# 输入数字
#age = turtle.numinput('你的年龄', '在1到100之间', 20, minval = 1, maxval = 100)
#turtle.write(int(age))

# 自定义shape
#shape = turtle.Shape('polygon', ((0,0), (50,0), (50, 50), ))
# 注册shape
#turtle.addshape('myshape', shape)
# 修改画笔颜色
#turtle.color('pink')
# 绘制shape
#turtle.penup()
#turtle.forward(100)
#turtle.shape('myshape')

