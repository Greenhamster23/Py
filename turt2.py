#turt2.py
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
#turtle.tracer(0,0)

dist = -150
for i in range(375):        #TIME
    t.fd(dist)
    t.pencolor('#000000')
    t.speed(9999999999999)
    t.rt(229)
    turtle.bgcolor('#FFFF00')
    dist += 0# dist = 0 dist + 0
    print(dist)
    t.goto(-300,250)
 
dist = -150
for i in range(400):        #TIME
    t.fd(dist)
    t.pencolor('#000000')
    t.speed(9999999999999) 
    t.rt(1)
    turtle.bgcolor('##FFFF00')
    dist += 0# dist = 0 dist + 0
    print(dist)
    t.goto(300,250)
    
dist = -150
for i in range(400):        #TIME
    t.fd(dist)
    t.pencolor('#000000')
    t.speed(9999999999999) 
    t.rt(1)
    turtle.bgcolor('#FFFFFF')
    dist += 0# dist = 0 dist + 0
    print(dist)
    t.goto(-150,-125)

     
#turtle.update()
screen.exitonclick() 


