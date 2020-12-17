# -*- coding:utf-8 -*- 
# @Time: 2020/5/23 23:25
# @Author: zxw
# @Name: demo3
# @Software: PyCharm

#蓝二哥哥

import turtle as t


def drawpic():

    t.pu()
    t.goto(-52, 144)   #额头向左
    t.pd()
    t.seth(150)
    t.fd(16)
    t.seth(-60)
    t.fd(12)
    t.seth(150)
    t.fd(5)
    t.seth(160)
    t.fd(5)
    t.seth(170)
    t.fd(10)
    t.seth(175)
    t.fd(8)
    t.seth(180)
    t.fd(8)
    t.seth(-30)
    t.fd(12)
    for i in range(10):
        t.seth(170 + i * 2)
        t.fd(2.5)

    t.pu()
    t.goto(-52, 148)  # 额头
    t.pd()

    for i in range(30):
        t.seth(140 + i)
        t.fd(1)
    for i in range(30):
        t.seth(190 + i)
        t.fd(1)

    for i in range(30):
        t.seth(240 + i)
        t.fd(3)

    t.seth(270)
    t.fd(30)
    t.seth(285)
    t.fd(10)
    t.seth(270)
    t.fd(10)
    for i in range(18):
        t.seth(270 + i * 5)
        t.fd(6)
    t.fd(30)

    t.pu()
    t.goto(-52, 144)   #额头向右
    t.pd()

    for i in range(30):
        t.seth(15 - i)
        t.fd(2)
    t.fd(20)

    t.pu()
    t.goto(-52, 145)    #额头向右
    t.pd()

    for i in range(45):
        t.seth(40 - i)
        t.fd(1.3)
    for i in range(60):
        t.seth(-5 - i)
        t.fd(0.5)
    for i in range(50):
        t.seth(-65 - i*0.5)
        t.fd(0.5)
    for i in range(60):
        t.fd(1)
    for i in range(60):
        t.seth(-90 + i*0.5)
        t.fd(1)

    t.pu()
    t.goto(42, 64)    #右侧头发
    t.pd()

    for i in range(15):
        t.seth(-90 + i)
        t.fd(4)

    t.pu()
    t.goto(42, 64)
    t.pd()

    for i in range(6):
        t.seth(-80 - i)
        t.fd(15)

    for i in range(4):
        t.seth(-90 - i*1.5)
        t.fd(10)
    for i in range(6):
        t.seth(-92 - i*8)
        t.fd(6)

    t.pu()
    t.goto(60, 80)
    t.pd()

    for i in range(10):
        t.seth(-80 - i)
        t.fd(10)

    for i in range(4):
        t.seth(-90 - i*1.5)
        t.fd(10)

    for i in range(6):
        t.seth(-92 - i*5)
        t.fd(9)

    t.pu()
    t.goto(68, -50)
    t.pd()

    for i in range(6):
        t.seth(-100 - i*8)
        t.fd(8)

    t.pu()
    t.goto(52, -45)    #右下颌
    t.pd()

    for i in range(10):
        t.seth(-160 - i*0.5)
        t.fd(5)

    t.pu()
    t.goto(-52, 148)  # 额头
    t.pd()

    for i in range(10):
        t.seth(45 - i*0.5)
        t.fd(2)
    for i in range(10):
        t.seth(40 - i)
        t.fd(2)
    for i in range(10):
        t.seth(30 - i*2)
        t.fd(2)
    for i in range(30):
        t.seth(10 - i*3)
        t.fd(3)
    for i in range(20):
        t.seth(-80 - i*0.5)
        t.fd(8)
    for i in range(30):
        t.seth(-90 - i)
        t.fd(3)

    t.pu()
    t.goto(77, 38)  # 耳朵
    t.pd()

    for i in range(15):
        t.seth(45 - i*3)
        t.fd(2)
    for i in range(30):
        t.seth(-30 - i*4)
        t.fd(2)
    t.fd(28)

    t.pu()
    t.goto(-52, 160)  # 额头
    t.pd()

    for i in range(30):
        t.seth(140 + i)
        t.fd(1)
    for i in range(30):
        t.seth(190 + i)
        t.fd(2)
    for i in range(10):
        t.seth(240 + i)
        t.fd(5)
    for i in range(10):
        t.seth(265 + i*0.5)
        t.fd(5)
    for i in range(10):
        t.seth(270 - i)
        t.fd(6)
    for i in range(10):
        t.seth(270 - i*0.55)
        t.fd(6)
    for i in range(20):
        t.seth(-70 + i)
        t.fd(4)

    t.pu()
    t.goto(-140, 10)  # 左侧头发
    t.pd()
    t.seth(270)
    t.fd(80)
    for i in range(20):
        t.seth(270 + i)
        t.fd(3)

    t.pu()
    t.goto(-140, 10)  # 左侧头发
    t.pd()
    for i in range(30):
        t.seth(270 + i*0.5)
        t.fd(6)

    t.pu()
    t.goto(-136, 145)  # 上侧头发1
    t.pd()

    for i in range(40):
        t.seth(80 - i*1.5)
        t.fd(2)

    t.pu()
    t.goto(-115, 160)  # 上侧头发2
    t.pd()

    for i in range(30):
        t.seth(80 - i * 2.5)
        t.fd(3)

    t.pu()
    t.goto(-90, 173)  # 上侧头发3
    t.pd()

    for i in range(22):
        t.seth(80 - i * 4)
        t.fd(4)

    t.pu()
    t.goto(-50, 200)  # 上侧头发4
    t.pd()

    for i in range(32):
        t.seth(60 - i * 3)
        t.fd(3)

    t.pu()
    t.goto(-40, 200)  # 上侧头发5
    t.pd()

    for i in range(50):
        t.seth(30 - i * 2)
        t.fd(4)

    t.pu()
    t.goto(-36, 170)  # 上侧头发6
    t.pd()

    for i in range(30):
        t.seth(60 - i * 2.5)
        t.fd(3)

    t.pu()
    t.goto(-26, 175)  # 上侧头发7
    t.pd()

    for i in range(30):
        t.seth(30 - i * 2.5)
        t.fd(4)

    t.pu()
    t.goto(70, 150)  # 右侧发丝1
    t.pd()
    t.seth(10)
    t.fd(45)

    t.pu()
    t.goto(75, 130)  # 右侧发丝2
    t.pd()
    t.seth(30)
    t.fd(40)

    t.pu()
    t.goto(115, 113)  # 右侧发丝3
    t.pd()
    for i in range(26):
        t.seth(-130 - i)
        t.fd(2)

    t.pu()
    t.goto(120, 116)  # 右侧发丝4
    t.pd()
    for i in range(30):
        t.seth(-100 - i)
        t.fd(2)

    t.pu()
    t.goto(124, 116)  # 右侧发丝5
    t.pd()
    t.seth(-90)
    t.fd(120)

    t.pu()
    t.goto(60, 210)  # 发髻1
    t.pd()
    for i in range(15):
        t.seth(60 - i*4)
        t.fd(2)
    for i in range(30):
        t.seth(0 - i*3)
        t.fd(3)
    t.fd(20)
    t.seth(-110)
    t.fd(30)

    t.pu()
    t.goto(80, 210)  # 发髻2
    t.pd()
    for i in range(30):
        t.seth(0 - i * 3)
        t.fd(2.5)
    t.fd(280)
    for i in range(10):
        t.seth(-90 - i*2)
        t.fd(4)

    t.pu()
    t.goto(-30, -60)  # 衣领1
    t.pd()
    for i in range(10):
        t.seth(-85 + i )
        t.fd(4)

    t.pu()
    t.goto(5, -60)  # 衣领2
    t.pd()
    for i in range(30):
        t.seth(-135 + i*1.5)
        t.fd(4)

    t.pu()
    t.goto(-40, -60)  # 衣领3
    t.pd()
    for i in range(10):
        t.seth(-90 + i)
        t.fd(6)

    t.pu()
    t.goto(25, -56)  # 衣领4
    t.pd()
    for i in range(30):
        t.seth(-135 + i*1.5)
        t.fd(4)

    t.pu()
    t.goto(-40, -60)  # 袖子左1
    t.pd()
    t.seth(-152)
    t.fd(45)

    t.pu()
    t.goto(-80, -85)  # 袖子左2
    t.pd()
    for i in range(10):
        t.seth(-70 + i)
        t.fd(5)

    t.pu()
    t.goto(-56, -100)  # 袖子左3
    t.pd()
    t.seth(-95)
    t.fd(65)

    t.pu()
    t.goto(-74, -100)  # 袖子左4
    t.pd()
    t.seth(-125)
    t.fd(60)
    t.seth(-60)
    t.fd(5)
    t.seth(-130)
    t.fd(15)
    for i in range(30):
        t.seth(45 - i*3)
        t.fd(2)
    t.pu()
    t.goto(-115, -165)
    t.pd()
    for i in range(15):
        t.seth(15 - i*2)
        t.fd(2)

    t.pu()
    t.goto(-115, -165)   # 左手
    t.pd()
    t.seth(-100)
    t.fd(15)
    t.seth(15)
    t.fd(8)
    t.seth(-60)
    t.fd(8)
    t.seth(60)
    t.fd(8)
    t.seth(-60)
    t.fd(8)
    t.seth(60)
    t.fd(7)
    t.seth(-45)
    t.fd(8)
    t.seth(100)
    t.fd(10)
    t.seth(-80)
    t.fd(6)
    t.seth(0)
    t.fd(6)
    t.seth(100)
    t.fd(16)

    t.pu()
    t.goto(25, -56)  # 袖子右1
    t.pd()
    t.seth(-20)
    t.fd(30)

    t.pu()
    t.goto(62, -68)  # 袖子右2
    t.pd()
    t.seth(-25)
    t.fd(6)

    t.pu()
    t.goto(70, -83)  # 袖子右3
    t.pd()
    t.seth(-80)
    t.fd(85)

    t.pu()
    t.goto(50, -90)  # 袖子右4
    t.pd()
    t.seth(-120)
    t.fd(35)
    t.seth(-90)
    t.fd(5)
    t.seth(-135)
    t.fd(26)
    t.seth(-70)
    t.fd(5)
    for i in range(16):
        t.seth(-i*2)
        t.fd(4)

    t.pu()
    t.goto(16, -148)  # 袖子右4
    t.pd()
    t.seth(-135)
    t.fd(12)
    for i in range(11):
        t.seth(-i*2)
        t.fd(4)

    t.pu()
    t.goto(7, -157)  # 右手
    t.pd()
    t.seth(-135)
    t.fd(15)
    t.seth(0)
    t.fd(5)
    t.seth(30)
    t.fd(10)
    t.seth(-130)
    t.fd(14)
    t.seth(0)
    t.fd(3)
    t.seth(40)
    t.fd(10)
    t.seth(-80)
    t.fd(10)
    t.seth(45)
    t.fd(10)
    t.seth(-90)
    t.fd(10)
    t.seth(45)
    t.fd(10)
    t.seth(-60)
    t.fd(10)
    t.seth(45)
    t.fd(10)
    t.seth(70)
    t.fd(15)

    t.pu()
    t.goto(-170, -165)  # 琴身
    t.pd()
    t.seth(-150)
    t.fd(80)
    for i in range(10):
        t.seth(-150+i*15)
        t.fd(2)
    t.seth(0)
    t.fd(330)
    for i in range(10):
        t.seth(-i)
        t.fd(2)
    t.seth(45)
    t.fd(60)
    for i in range(10):
        t.seth(80+i)
        t.fd(1)
    for i in range(10):
        t.seth(90+i*9)
        t.fd(1)
    for i in range(10):
        t.seth(180+i*4)
        t.fd(1)
    t.seth(180)
    t.fd(90)
    t.pu()
    t.goto(0, -165)
    t.pd()
    t.seth(180)
    t.fd(90)
    t.pu()
    t.goto(-120, -165)
    t.pd()
    t.seth(180)
    t.fd(50)

    t.pu()
    t.goto(-165, -170)   #琴柱左
    t.pd()
    t.seth(-150)
    t.fd(75)
    t.seth(0)
    t.fd(10)
    t.seth(30)
    t.fd(75)
    t.seth(180)
    t.fd(10)

    t.seth(0)
    t.pu()
    t.goto(-165, -175)  #弦1
    t.pd()
    t.fd(49)
    t.pu()
    t.goto(-85, -175)
    t.pd()
    t.fd(100)
    t.pu()
    t.goto(36, -175)
    t.pd()
    t.fd(92)
    t.pu()
    t.goto(-175, -182)  #弦2
    t.pd()
    t.fd(297)
    t.pu()
    t.goto(-185, -189)  #弦3
    t.pd()
    t.fd(300)
    t.pu()
    t.goto(-197, -196)  #弦4
    t.pd()
    t.fd(305)
    t.pu()
    t.goto(-209, -203)  #弦5
    t.pd()
    t.fd(309)

    t.pu()
    t.goto(135, -170)   #琴柱右
    t.pd()
    t.seth(-135)
    t.fd(60)
    t.seth(0)
    t.fd(10)
    t.seth(45)
    t.fd(60)
    t.seth(180)
    t.fd(10)

    t.pu()
    t.goto(-240, -220)  # 琴底盘
    t.pd()
    for i in range(10):
        t.seth(-70 + i * 4)
        t.fd(2)
    t.seth(0)
    t.fd(332)
    t.seth(45)
    t.fd(75)
    t.seth(90)
    t.fd(5)

    t.pu()
    t.goto(-140, -235)  # 衣服下摆
    t.pd()
    for i in range(14):
        t.seth(-70 + i * 5)
        t.fd(4)
    t.seth(0)
    t.fd(45)
    for i in range(10):
        t.seth(0 - i * 4)
        t.fd(1)
    for i in range(20):
        t.seth(-40 + i * 4)
        t.fd(1)
    for i in range(10):
        t.seth(40 + i * 2)
        t.fd(4.5)
    t.pu()
    t.goto(-18, -265)
    t.pd()
    t.seth(0)
    t.fd(50)
    for i in range(27):
        t.seth(i * 3)
        t.fd(2)


    t.pensize(3)
    t.pu()
    t.goto(-116, 125) #抹额
    t.pd()
    for i in range(10):
        t.seth(-5 + i)
        t.fd(14.5)
    t.pu()
    t.goto(65, 125)
    t.pd()
    for i in range(10):
        t.seth(5+i)
        t.fd(5.8)
    t.seth(-80)
    t.fd(20)
    t.pu()
    t.goto(-120, 95)
    t.pd()
    for i in range(10):
        t.seth(-5 + i)
        t.fd(15)
    t.pu()
    t.goto(70, 95)
    t.pd()
    for i in range(10):
        t.seth(5 + i*3)
        t.fd(6)

    t.pencolor(175,222,232)   #抹额蓝色
    t.pu()
    t.goto(-70, 105)
    t.pd()
    for i in range(10):
        t.seth(160 + i*4)
        t.fd(2)
    for i in range(20):
        t.seth(200 + i * 8)
        t.fd(0.5)
    t.pu()
    t.goto(-60, 110)
    t.pd()
    for i in range(15):
        t.seth(180 + i*18)
        t.fd(2)
    for i in range(10):
        t.seth(90 + i*18)
        t.fd(1)
    t.pu()
    t.goto(-40, 105)
    t.pd()
    for i in range(10):
        t.seth(90 + i * 18)
        t.fd(1)
    for i in range(15):
        t.seth(270 + i * 18)
        t.fd(2.2)
    t.pu()
    t.goto(-25, 105)
    t.pd()
    for i in range(10):
        t.seth(20 - i*4)
        t.fd(2.2)
    for i in range(20):
        t.seth(-20 - i * 8)
        t.fd(0.5)

    t.pencolor(0, 0, 0)  # 左眉
    t.pensize(4)
    t.pu()
    t.goto(-70, 65)
    t.pd()
    t.seth(175)
    t.fd(50)

    t.pu()            # 右眉
    t.goto(-20, 65)
    t.pd()
    t.seth(5)
    t.fd(50)

    t.pensize(3)    # 左眼
    t.pu()
    t.goto(-118, 35)
    t.pd()
    for i in range(20):
        t.seth(20 - i * 3)
        t.fd(2.6)
    t.pu()
    t.goto(-110, 35)
    t.pd()
    for i in range(20):
        t.seth(-100 + i * 10)
        t.fd(3)
    t.pu()
    t.goto(-100, 27)
    t.pd()
    t.circle(4)
    t.pu()
    t.goto(-96, 24)
    t.pd()
    t.circle(3)

    t.pensize(2)
    t.pu()
    t.goto(-113, 13)
    t.pd()
    t.seth(0)
    t.fd(40)

    t.pensize(3)  # 右眼
    t.pu()
    t.goto(-10, 32)
    t.pd()
    for i in range(20):
        t.seth(20 - i * 3)
        t.fd(2.6)
    t.pu()
    t.goto(0, 35)
    t.pd()
    for i in range(13):
        t.seth(-130 + i * 10)
        t.fd(2.5)
    for i in range(10):
        t.seth(0 + i * 9)
        t.fd(3.2)
    t.pu()
    t.goto(18, 25)
    t.pd()
    t.circle(3)
    t.pu()
    t.goto(23, 27)
    t.pd()
    t.circle(4)

    t.pensize(2)
    t.pu()
    t.goto(0, 10)
    t.pd()
    t.seth(0)
    t.fd(30)

    t.pensize(3)    # 嘴
    t.pu()
    t.goto(-40, -20)
    t.pd()
    t.seth(0)
    t.fd(8)


if __name__ == '__main__':
    t.pensize(2)
    t.hideturtle()
    t.colormode(255)
    t.setup(640, 640)
    t.speed(50)
    drawpic()
    t.done()






