#coding=utf-8
from turtle import *
screensize(None,None,'black')
begin_fill #轮廓
'''
while True:
   color('black', 'white')
    speed(5)
    penup()
    goto(0,-100)
    pendown()
    circle(100,360)
    penup()
    goto(-98.3,-18.6)
    pendown()
    goto(-64.3,2.4)
    goto(-28.6,95.8)
    goto(-28.6,-95.8)
    goto(-5.3,-58.2)
    goto(98.3,-18.6)
    goto(-98.3,-18.6)
    penup()
    goto(-95.8,-28.6)
    pendown()
    goto(-58.2,-5.3)
    goto(-18.6,98.3)
    goto(-18.6,-98.3)
    goto(2.4,-64.3)
    goto(95.8,-28.6)
    goto(-95.8,-28.6)
    break
end_fill
'''
begin_fill() #左翅膀
while True:
    color('Deeppink2', 'Deeppink2')
    speed(4)
    penup()
    goto(-79.6,-18.6)
    pendown()
    goto(-58.2,-5.3)
    goto(-28.6,72.1)
    goto(-28.6,-18.6)
    goto(-79.6,-18.6)
    penup()
    break
end_fill()

begin_fill() #右翅膀
while True:
    speed(4)
    color('green2', 'green2')
    penup()
    goto(-18.6,-28.6)
    pendown()
    goto(72.1,-28.6)
    goto(-5.3,-58.2)
    goto(-18.6,-79.6)
    goto(-18.6,-28.6)
    penup()
    break
end_fill()

begin_fill()
while True: #右翅膀右
    speed(4)
    color('green4','green4')
    penup()
    goto(-18.6,-98.3)
    pendown()
    seth(-10.72)
    circle(100,84.1)
    goto(2.4,-64.3)
    goto(-18.6,-98.3)
    break
end_fill()

begin_fill()
while True:
    speed(4)
    color('dodger blue','dodger blue')
    penup()
    goto(-18.6,-18.6)
    pendown()
    goto(98.3,-18.6)
    seth(79.28)
    circle(100,111.45)
    goto(-18.6,98.3)
    goto(-18.6,-18.6)
    break
end_fill()

begin_fill()
while True:
    speed(3)
    color('HotPink1','HotPink1')
    penup()
    goto(-98.3,-18.6)
    pendown()
    seth(100.72)
    circle(-100,84.1)
    goto(-64.3,2.4)
    goto(-98.3,-18.6)
    break
end_fill()

begin_fill()
while True:
    speed(3)
    color('sandy brown','sandy brown')
    penup()
    goto(-28.6,-28.6)
    pendown()
    goto(-95.8,-28.6)
    seth(286.62)
    circle(100,56.75)
    goto(-28.6,-28.6)
    break
end_fill()

#begin_fill()
#while True:

   
color('cyan','cyan')

write("QIUTOPIA", font=('Arial', 40, 'normal'))
penup()
goto(-200,-100)
pendown()
write("BY DIGUA", font=('Arial', 20, 'normal'))
done()
