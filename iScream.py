import turtle

sc=turtle.Screen()
Amin=turtle.Turtle()
turtle.tracer(10)
sc.bgcolor("cadetblue")
Amin.up()
Amin.setx(-70)
Amin.sety(-160)    
Amin.down()
Amin.color("darkgoldenrod")
Amin.right(90)
def f(t,Step,alpha) :
    t.forward(Step)
    t.left(alpha)
for a in range(16) :######################################
    f(Amin,9.5,0.05)  ###8--->9.5
def g(t,Step,alpha) :
    t.forward(Step)
    t.left(alpha)
for a in range(36) :
    g(Amin,2.5,5)
Amin.right(0.75)
Amin.forward(125)
Amin.left(90)
Amin.forward(10)
Amin.up()
Amin.goto(-70.0,-160.0)
Amin.left(90)
Amin.color("darkgoldenrod","darkgoldenrod")
Amin.begin_fill()
Amin.up()
for a in range(16) : #####################
    f(Amin,9.5,0.01) ###### 8---->9.5
for a in range(36) :
    g(Amin,2.5,5)
Amin.right(0.75)
Amin.forward(125)
Amin.left(90)
Amin.forward(10)
Amin.goto(-70.0,-160.0)
Amin.end_fill()
Amin.begin_fill()#########################################################
Amin.goto(-180.0,-99.0)############## 5.0-->-19.0
Amin.left(90)
Amin.color("white","white")
Amin.down()
for a in range(70) :
    Amin.forward(55/70)
    Amin.right(1/70)
    t=1
for a in range (20) :
    t=t*1.005
    Amin.forward(t)
    Amin.left(t)
for a in range(30) :
    Amin.forward(20/30)
    Amin.left(55/30)
Amin.left(360-344.54401101450003)

Amin.left(5)
Amin.forward(5)
t=1
for a in range(9) :
    Amin.left(t)
    Amin.forward(20/9)
    t=t+1
Amin.forward(7)
for a in range(80) :
    Amin.forward(5/80)
    Amin.right(45/80)
Amin.right(5)
for a in range(2) :
    Amin.forward(2.75)
for a in range(100) : #Begin Corner
    Amin.right(90/100)
    Amin.forward(1/10) #End corner
for a in range(400) :
    Amin.right(0.00/100)
    Amin.forward(90/400)
for a in range(100) :
    Amin.left(180/100)
    Amin.forward(2/10)
for a in range(75) :
    Amin.forward(1)
Amin.circle(-20,90)
for a in range(100) :
    Amin.forward(5/100)
#forward(50)
#right(90)
for a in range(200) :
    Amin.forward(35/200)
    Amin.right(90/200)
Amin.left(90)
for a in range(100) :
    Amin.forward(5/100)
Amin.left(90)
for a in range(100) : #Begin Corner
    Amin.right(90/100)
    Amin.forward(2/10) #End corner
    
#Right(30)
for a in range(200) :
    Amin.right(30/200)
    Amin.forward(6/200)
for a in range(10) :
    Amin.forward(1)
for a in range(200) :
    Amin.left(30/200)
    Amin.forward(6/200)
for a in range(35) :
    Amin.forward(1)
#Right(60)
Amin.circle(-20,60)
for a in range(10) :
    Amin.forward(1)
for a in range(120) :
    Amin.left(1)
    Amin.forward(10/120)
for a in range(10) :
    Amin.forward(0.5)
    Amin.left(1.2)
for a in range(15) :
    Amin.forward(1)
Amin.circle(-10,72)
for a in range(30) :
    Amin.forward(1)
#left(50)
for a in range(10) :
    Amin.left(50/10)
    Amin.forward(2)
#left(40)
for a in range(500) :
    Amin.forward(50/500)
    Amin.left(4/50)
for a in range(50) :
    Amin.forward(30.10/50)

Amin.left(90)
####Amin.color("red")#####
for a in range(5) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(5/400)
    Amin.left(65/400)
for a in range(5) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(130/400)
for a in range(6) :
    Amin.forward(1)

##Left(65)
for a in range(500) :
    Amin.forward(5/500)
    Amin.left(65/500)
##Left(90)
for a in range(500) :
    Amin.left(90/500)
    Amin.forward(15/500)
for a in range(35) :
    Amin.forward(1)
##Right(90)
for a in range(900) :
    Amin.right(90/900)
    Amin.forward(8/900)
##Right(90)
for a in range(200) :
    Amin.right(90/200)
    Amin.forward(8/200)
for a in range(36) :
    Amin.forward(1)
#Left(90)
for a in range(200) :
    Amin.left(9/20)
    Amin.forward(12/200)
#Left(55)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(10/200)
for a in range(1) :
    Amin.forward(1)
##Right(55)
for a in range(200) :
    Amin.forward(10/200)
    Amin.right(55/200)
for a in range(6) :
    Amin.forward(1)
#Right(95)
for a in range (400) :
    Amin.right(95/400)
    Amin.forward(12/400)
Amin.left(35)
#Left(60)
for a in range(200) :
    Amin.forward(5/200)
    Amin.left(60/200)
#left(90)
for a in range(400) :
    Amin.forward(10/400)
    Amin.left(90/400)
for a in range(20) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(5/400)
    Amin.right(80/400)
for a in range(5) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(3/200)
    Amin.right(10/200)
#Right(90)
for a in range(200) :
    Amin.forward(5/200)
    Amin.right(90/200)
    
a=17
while a!=0 :
    Amin.forward(1)
    a=a-1
#Right(15)
for a in range(100) :
    Amin.forward(4/100)
    Amin.right(15/100)
for a in range(10) :
    Amin.forward(1)
#left(135)
for a in range(400) :
    Amin.forward(18/400)
    Amin.left(144/400)
for a in range(10) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(20/400)
Amin.right(19)
Amin.left(60)
#Right(60)
############Amin.color("crimson")#########
for a in range(20) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(20/200)
    Amin.right(60/200)
for a in range(55) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(80/400)
    Amin.forward(60/400)
##Amin.color("red")#####
#left(80)
for a in range(8) :
    Amin.forward(1)
for a in range(100) :
    Amin.forward(10/100)
    Amin.left(80/100)
#left(45)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(7/200)
for a in range(15) :
    Amin.forward(1)
#Right(55)
for a in range(400) :
    Amin.forward(13/400)
    Amin.right(55/400)
Amin.goto(-180.0,-99.00)
Amin.end_fill()
# RRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDDDDDDDDDDDD
Amin.goto(123.21,-99.00)
"Amin.left(90)"########################################
Amin.color("red")
for a in range(5) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(5/400)
    Amin.left(65/400)
for a in range(5) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(130/400)
for a in range(6) :
    Amin.forward(1)

##Left(65)
for a in range(500) :
    Amin.forward(5/500)
    Amin.left(65/500)
##Left(90)
for a in range(500) :
    Amin.left(90/500)
    Amin.forward(15/500)
for a in range(35) :
    Amin.forward(1)
##Right(90)
for a in range(900) :
    Amin.right(90/900)
    Amin.forward(8/900)
##Right(90)
for a in range(200) :
    Amin.right(90/200)
    Amin.forward(8/200)
for a in range(36) :
    Amin.forward(1)
#Left(90)
for a in range(200) :
    Amin.left(9/20)
    Amin.forward(12/200)
#Left(55)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(10/200)
for a in range(1) :
    Amin.forward(1)
##Right(55)
for a in range(200) :
    Amin.forward(10/200)
    Amin.right(55/200)
for a in range(6) :
    Amin.forward(1)
#Right(95)
for a in range (400) :
    Amin.right(95/400)
    Amin.forward(12/400)
Amin.left(35)
#Left(60)
for a in range(200) :
    Amin.forward(5/200)
    Amin.left(60/200)
#left(90)
for a in range(400) :
    Amin.forward(10/400)
    Amin.left(90/400)
for a in range(20) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(5/400)
    Amin.right(80/400)
for a in range(5) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(3/200)
    Amin.right(10/200)
#Right(90)
for a in range(200) :
    Amin.forward(5/200)
    Amin.right(90/200)
    
a=17
while a!=0 :
    Amin.forward(1)
    a=a-1
#Right(15)
for a in range(100) :
    Amin.forward(4/100)
    Amin.right(15/100)
for a in range(10) :
    Amin.forward(1)
#left(135)
for a in range(400) :
    Amin.forward(18/400)
    Amin.left(144/400)
for a in range(10) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(20/400)
Amin.right(19)
Amin.left(60)
#Right(60)
Amin.color("crimson")

for a in range(20) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(20/200)
    Amin.right(60/200)
for a in range(55) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(80/400)
    Amin.forward(60/400)

Amin.color("red")
#left(80)
for a in range(8) :
    Amin.forward(1)
for a in range(100) :
    Amin.forward(10/100)
    Amin.left(80/100)
#left(45)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(7/200)
for a in range(15) :
    Amin.forward(1)
#Right(55)
for a in range(400) :
    Amin.forward(13/400)
    Amin.right(55/400)
Amin.goto(-180.0,-99.00)
#
#
#
#
#
#
#
#
Amin.right(90) #########    LEFT IScReaM
#right(30)
for a in range(400) :
    Amin.forward(400/400)
    Amin.right(30/400)


#right(60)
for a in range(400) :
    Amin.forward(60/400)
    Amin.right(60/400)
#right(30)
for a in range(17) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(30/400)
    Amin.forward(30/400)
for a in range(5) :
    Amin.forward(1)

Amin.left(30)
Amin.left(60)
for a in range(400) :
    Amin.forward(40/400)
    Amin.right(53/400)
for a in range(50) :
    Amin.forward(1)
Amin.circle(-200,23)

#Right(67)
for a in range(400) :
    Amin.forward(40/400)
    Amin.right(74/400)
for a in range(5) :
    Amin.forward(1)

#left 16
for a in range(400) :
    Amin.forward(5/400)
    Amin.right(25/400)
for a in range(500) :
    Amin.forward(360/500)
    Amin.left(24/500)
Amin.down()
Amin.goto(123.21,-99.00)

#####################################    Fill COLoR ColoR RED
Amin.left(1)
Amin.begin_fill()
Amin.right(90)
Amin.color("darkseagreen","darkseagreen")
for a in range(5) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(5/400)
    Amin.left(65/400)
for a in range(5) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(130/400)
for a in range(6) :
    Amin.forward(1)

##Left(65)
for a in range(500) :
    Amin.forward(5/500)
    Amin.left(65/500)
##Left(90)
for a in range(500) :
    Amin.left(90/500)
    Amin.forward(15/500)
for a in range(35) :
    Amin.forward(1)
##Right(90)
for a in range(900) :
    Amin.right(90/900)
    Amin.forward(8/900)
##Right(90)
for a in range(200) :
    Amin.right(90/200)
    Amin.forward(8/200)
for a in range(36) :
    Amin.forward(1)
#Left(90)
for a in range(200) :
    Amin.left(9/20)
    Amin.forward(12/200)
#Left(55)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(10/200)
for a in range(1) :
    Amin.forward(1)
##Right(55)
for a in range(200) :
    Amin.forward(10/200)
    Amin.right(55/200)
for a in range(6) :
    Amin.forward(1)
#Right(95)
for a in range (400) :
    Amin.right(95/400)
    Amin.forward(12/400)
Amin.left(35)
#Left(60)
for a in range(200) :
    Amin.forward(5/200)
    Amin.left(60/200)
#left(90)
for a in range(400) :
    Amin.forward(10/400)
    Amin.left(90/400)
for a in range(20) :
    Amin.forward(1)
#Right(80)
for a in range(400) :
    Amin.forward(5/400)
    Amin.right(80/400)
for a in range(5) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(3/200)
    Amin.right(10/200)
#Right(90)
for a in range(200) :
    Amin.forward(5/200)
    Amin.right(90/200)
    
a=17
while a!=0 :
    Amin.forward(1)
    a=a-1
#Right(15)
for a in range(100) :
    Amin.forward(4/100)
    Amin.right(15/100)
for a in range(10) :
    Amin.forward(1)
#left(135)
for a in range(400) :
    Amin.forward(18/400)
    Amin.left(144/400)
for a in range(10) :
    Amin.forward(1)
for a in range(400) :
    Amin.forward(10/400)
    Amin.right(20/400)
Amin.right(19)
Amin.left(60)
#Right(60)
Amin.color("darkseagreen")
for a in range(20) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(20/200)
    Amin.right(60/200)
for a in range(55) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(80/400)
    Amin.forward(60/400)

#left(80)
for a in range(8) :
    Amin.forward(1)
for a in range(100) :
    Amin.forward(10/100)
    Amin.left(80/100)
#left(45)
for a in range(200) :
    Amin.left(55/200)
    Amin.forward(7/200)
for a in range(15) :
    Amin.forward(1)
#Right(55)
for a in range(400) :
    Amin.forward(13/400)
    Amin.right(55/400)
Amin.goto(-180.0,-99.00)


Amin.right(90)
#right(30)
for a in range(400) :
    Amin.forward(400/400)
    Amin.right(30/400)


#right(60)
for a in range(400) :
    Amin.forward(60/400)
    Amin.right(60/400)
#right(30)
for a in range(17) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(30/400)
    Amin.forward(30/400)
for a in range(5) :
    Amin.forward(1)
Amin.left(30)
Amin.left(60)
for a in range(400) :
    Amin.forward(40/400)
    Amin.right(53/400)
for a in range(50) :
    Amin.forward(1)
Amin.circle(-200,23)

#Right(67)
for a in range(400) :
    Amin.forward(40/400)
    Amin.right(74/400)
for a in range(5) :
    Amin.forward(1)

#left 16
for a in range(400) :
    Amin.forward(5/400)
    Amin.right(25/400)
for a in range(500) :
    Amin.forward(360/500)
    Amin.left(24/500)
Amin.down()
Amin.goto(123.21,-99.00)


Amin.end_fill()
Amin.up()
Amin.goto(21.65,301.56)
Amin.down()
Amin.color("black")

Amin.right(29)
Amin.pensize(0.125)
for a in range(200) :
    Amin.forward(100/200)
    Amin.left(7/200)
  
Amin.up()
Amin.goto(-52.97,217.14)
####################################    EYE

Amin.pensize(3)
Amin.down()
Amin.right(67)
Amin.left(3)
for a in range(400) :
    Amin.forward(32/400)
    Amin.left(45/400)

Amin.up()
Amin.goto(37.97,209.14)

Amin.down()

Amin.left(132.0)
Amin.right(40)

for a in range(400) :
    Amin.forward(25/400)
    Amin.right(50/400)

Amin.up()
Amin.pensize(1)
Amin.goto(182.94,322.73)
Amin.down()
Amin.color("saddlebrown")
Amin.right(25)

t=1
for a in range(500) :
    
    Amin.forward(442/500)
    Amin.left(25.25/500)

Amin.right(0.25)
#################################################   Begin MouTH
Amin.up()
Amin.goto(-113.71,-20.73)


Amin.left(180)
Amin.right(5)
Amin.down()
Amin.color("black")
############################################################## 
for a in range(400) :

    Amin.forward(160/400)
    Amin.right(13/400)
############################################################
#Right(72)
#left(7)

for a in range(200) :
    Amin.forward(10/200)
    Amin.right(63.5/200)
for a in range(200) :
    Amin.forward(55/200)
    Amin.right(8.5/200)

for a in range(400) :
    Amin.forward(60/400)
    Amin.right(30/400)

Amin.right(60)
for a in range(15) :
    Amin.forward(1)

Amin.right(8)
for a in range(400) :
    Amin.forward(194/400)
for a in range(400) :
    Amin.forward(24/400)
    Amin.right(92/400)
Amin.forward(3.5)
##########################################   EnD MouTH
########################################## ColoRing MouTH

Amin.left(100)
Amin.color("black","black")
Amin.begin_fill()
Amin.up()
Amin.goto(-113.71,-20.73)

Amin.left(180)
Amin.right(5)
Amin.down()
Amin.color("black")
############################################################## 
for a in range(400) :

    Amin.forward(160/400)
    Amin.right(13/400)
############################################################
#Right(72)
#left(7)

for a in range(200) :
    Amin.forward(10/200)
    Amin.right(63.5/200)
for a in range(200) :
    Amin.forward(55/200)
    Amin.right(8.5/200)

for a in range(400) :
    Amin.forward(60/400)
    Amin.right(30/400)

Amin.right(60)
for a in range(15) :
    Amin.forward(1)
Amin.right(8)
for a in range(400) :
    Amin.forward(194/400)
for a in range(400) :
    Amin.forward(24/400)
    Amin.right(92/400)
Amin.forward(3.5)
Amin.end_fill()
########################################## End ColoRing MouTH
Amin.up()
Amin.goto(-9.94,-99.40)
Amin.color("crimson")

Amin.right(80)

Amin.down()
for a in range(400) :
    Amin.forward(100/400)
    Amin.right(36.5/400)

Amin.up()
Amin.goto(-133.71,-90.73)
Amin.down()
Amin.left(46.5)
Amin.right(26.25)

for a in range(400) :
    Amin.forward(75/400)

for a in range(400) :
    Amin.forward(85/400)
    Amin.right(93.75/400)
Amin.left(20)
Amin.left(20)
#Right(40)
for a in range(400) :
    Amin.forward(70/400)
    Amin.right(50/400)
Amin.goto(20.78,-6.00)

################################ Tongue  Tongue
Amin.pensize(1)
Amin.color("crimson","crimson")
Amin.begin_fill()
Amin.right(60)
Amin.right(36.5)
for a in range(400) :
    Amin.forward(100/400)
    Amin.left(36.5/400)
Amin.right(30)

for a in range(20) :
    Amin.forward(1)
for a in range(200) :
    Amin.forward(20/200)
    Amin.right(60/200)
for a in range(55) :
    Amin.forward(1)
for a in range(400) :
    Amin.right(80/400)
    Amin.forward(60/400)



Amin.right(26.25)
for a in range(400) :
    Amin.forward(75/400)

for a in range(400) :
    Amin.forward(85/400)
    Amin.right(93.75/400)

Amin.left(20)
Amin.left(20)
#Right(40)
for a in range(400) :
    Amin.forward(70/400)
    Amin.right(50/400)
Amin.goto(20.78,-6.00)
Amin.end_fill()
Amin.up()
Amin.goto(-45.30,15.74)

Amin.right(130)
Amin.left(30)
Amin.down()
Amin.color("black")
Amin.pensize(1)
for a in range(500) :
    Amin.left(42/500)
    Amin.forward(100/500)
Amin.right(60)
Amin.left(58.0)
Amin.up()
Amin.goto(-82.90,132.68) # T...U...R...T...L...E
Amin.begin_fill()
Amin.left(90)
Amin.down()
Amin.color("snow","snow")

    
for a in range(7) :
    Amin.forward(1)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
Amin.forward(10)
Amin.right(90)
for a in range(50) :
    Amin.forward(3/50)
Amin.right(90)
Amin.forward(9)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
Amin.forward(5)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
    ######################   ThiRd TooTH
Amin.forward(10)
Amin.right(90)
for a in range(50) :
    Amin.forward(3/50)
Amin.right(90)
Amin.forward(9)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
Amin.forward(5)
for a in range(100) :
    Amin.left(80/100)
    Amin.forward(7/100)
    #########################  FouRth TooTH
Amin.forward(10)
Amin.right(80)
for a in range(50) :
    Amin.forward(3/50)
Amin.right(100)

Amin.forward(9)
for a in range(100) :
    Amin.left(100/100)
    Amin.forward(9/100)
Amin.forward(4)
for a in range(100) :
    Amin.left(80/100)
    Amin.forward(7/100)
    ##############################   FifTH TooTH
Amin.forward(10)
Amin.right(80)
for a in range(50) :
    Amin.forward(3/50)
Amin.right(100)

Amin.forward(9)
for a in range(100) :
    Amin.left(100/100)
    Amin.forward(9/100)
Amin.forward(4)
for a in range(100) :
    Amin.left(80/100)
    Amin.forward(7/100)
    ################################  SixTH TooTH
Amin.forward(10)
Amin.right(80)
for a in range(50) :
    Amin.forward(3/50)
Amin.right(103)
Amin.forward(8)
for a in range(100) :
    Amin.left(100/100)
    Amin.forward(10/100)
Amin.forward(5)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
   #################################  SeVenTH TooTH
Amin.forward(8)
Amin.right(12)
Amin.forward(3)
Amin.right(90)
Amin.forward(1)
for a in range(100) :
    Amin.right(90/100)
    Amin.forward(5/100)
Amin.forward(9)
for a in range(100) :
    Amin.forward(7/100)
    Amin.left(90/100)
Amin.forward(5)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
    ############################# LAST ONE
Amin.forward(6)
Amin.right(105)
Amin.forward(4)
Amin.right(80)
Amin.forward(7)
for a in range(100) :
    Amin.left(90/100)
    Amin.forward(7/100)
for a in range(15) :
    Amin.forward(1)
    ############################## Finish TeeTH
Amin.left(20)
Amin.left(90)
Amin.forward(10)
Amin.forward(30)
Amin.left(90)
for a in range(160) :
    Amin.forward(1)
Amin.goto(-82.90,132.68)
Amin.end_fill()
#######################################   CleaNing
Amin.begin_fill()
Amin.left(90)
Amin.up()
Amin.goto(-113.71,-20.73)


Amin.left(180)
Amin.right(5)
Amin.down()
Amin.color("darkseagreen","darkseagreen")
############################################################## 
for a in range(400) :
    Amin.forward(160/400)
    Amin.right(13/400)
############################################################
#Right(72)
#left(7)

for a in range(200) :
    Amin.forward(10/200)
    Amin.right(63.5/200)
for a in range(200) :
    Amin.forward(55/200)
    Amin.right(8.5/200)

for a in range(400) :
    Amin.forward(60/400)
    Amin.right(30/400)

Amin.right(60)
for a in range(15) :
    Amin.forward(1)

Amin.right(8)
for a in range(400) :
    Amin.forward(194/400)
Amin.right(262.0)
for a in range(50) :
    Amin.forward(1)
Amin.left(90)
for a in range(100) :
    Amin.forward(1)
for a in range(100) :
    Amin.forward(1.55)
Amin.left(90)
a=180
while a!=0 :
    Amin.forward(1)
    a=a-1
Amin.left(90)
for a in range(100) :
    Amin.forward(1)
Amin.up()
Amin.goto(-113.71,-20.73)
Amin.end_fill()
###############################

#######################################   EnD CleaninG

Amin.shape("blank")

