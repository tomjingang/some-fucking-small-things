import turtle as t #turtle库是python的内部库，直接import使用即可
def draw_diamond(turt):
    for i in range(1,3):
        turt.forward(100) #向前走100步🐢
        turt.right(45) #海龟头向右转45度
        turt.forward(100) #继续向前走100步🐢
        turt.right(135) #海龟头再向右转135度

def draw_art():
    window = t.Screen() #创建画布
    window.bgcolor("green") #设置画布颜色
    brad = t.Turtle() #创建一个Turtle的实例
    brad.shape('turtle') #形状是一个海归turtle，也可以是圆圈circle，箭头(默认)等等
    brad.color("red") #海龟的颜色是红色red，橙色orange等
    brad.speed('fast') #海龟画图的速度是快速fast，或者slow等
    for i in range(1,37): #循环36次
        draw_diamond(brad) #海龟画一个形状/花瓣，也就是菱形
        brad.right(10) #后海龟头向右旋转10度
        brad.right(90) #当图形画完一圈后，把海龟头向右转90度
        brad.forward(300) #画一根长线/海龟往前走300步
    window.exitonclick() #点击屏幕退出
draw_art() #调用函数开始画图