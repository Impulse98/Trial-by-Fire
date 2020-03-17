#Trial By Fire
#By Impulse98

import turtle
import time 
import random 
import sys
print (sys.path)
import pygame
from pygame import mixer
pygame.mixer.init()

delay = 0.1

#Score
score = 0 #Score is zero when game begins. initializes the score variable
high_score = 0 # initializes highscore variable to zero

#music
mixer.music.load("poke.mp3")
mixer.music.play(-1)


#screen
wn = turtle.Screen() #window object
wn.title("Trial by fire") #title of the program top bar
wn.bgcolor("black") #background colour
#wn.bgpic("grass1.gif") #background image
wn.setup(width=600, height=600) #size of the window
wn.tracer(0)

#snake head
#wn.register_shape("rightmouth.gif")
#wn.register_shape("leftmouth.gif")
#wn.register_shape("upmouth.gif")
#wn.register_shape("downmouth.gif")
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
#head.shape("rightmouth.gif")
head.color("gold")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.shapesize(0.7)
food.penup()
food.goto(0,100)

segments = []

#snake super food
s_food = turtle.Turtle()
s_food.speed(0)
s_food.shape("circle")
s_food.color("pink")
s_food.shapesize(0.7)
s_food.penup()
s_food.goto(0,150)

#obstacles
bomb1 = turtle.Turtle()
bomb1.color("violetred4")
bomb1.shape("square")
bomb1.speed(0)
bomb1.penup()
bomb1.shapesize(1.5)
a = random.randint(-280, 280)
b = random.randint(-280, 280)
bomb1.goto(a, b)

bomb2 = turtle.Turtle()
bomb2.color("blue")
bomb2.shape("square")
bomb2.speed(0)
bomb2.penup()
bomb2.shapesize(1.5)
c = random.randint(-280, 280)
d = random.randint(-280, 280)
bomb2.goto(c, d)

bomb3 = turtle.Turtle()
bomb3.color("red")
bomb3.shape("square")
bomb3.speed(0)
bomb3.penup()
bomb3.shapesize(1.5)
e = random.randint(-280, 280)
f = random.randint(-280, 280)
bomb3.goto(e, f)

bomb4 = turtle.Turtle()
bomb4.color("yellow")
bomb4.shape("square")
bomb4.speed(0)
bomb4.penup()
bomb4.shapesize(1.5)

g = random.randint(-280, 280)
h = random.randint(-280, 280)
bomb4.goto(g, h)

bomb5 = turtle.Turtle()
bomb5.color("brown")
bomb5.shape("square")
bomb5.speed(0)
bomb5.penup()
bomb5.shapesize(1.5)
i = random.randint(-280, 280)
j = random.randint(-280, 280)
bomb5.goto(i, j)

segments = []


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal", "bold"))

#Functions
def go_up():#up direction
    if head.direction != "down":
        head.direction = "up"
        #head.shape("upmouth.gif")

def go_down():#down direction
    if head.direction != "up":
        head.direction = "down"
        #head.shape("downmouth.gif")

def go_left():#left direction
    if head.direction != "right":
        head.direction = "left"
        #head.shape("leftmouth.gif")

def go_right():#right direction
    if head.direction != "left":
        head.direction = "right"
        #head.shape("rightmouth.gif")

def pause():
    if head.direction != "left" or "right" or "up" or "down":
        head.direction = "pause"            

def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor() #y coordinate
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor() #x coordinate
        head.setx(x-20)
    
    if head.direction == "right":
        x = head.xcor() #x coordinate
        head.setx(x+20)

    if head.direction == "pause":
        x = head.xcor() #x coordinate
        head.setx(x)   

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "Right")
wn.onkeypress(pause, " ")

#main game loop
while True:
    wn.update()

    if food.distance(bomb1) < 40 or food.distance(bomb2) < 40 or food.distance(bomb3) < 40 \
            or food.distance(bomb4) < 40 or food.distance(bomb5) < 40:
        food.goto(random.randint(-250, 250), random.randint(-250, 250))    
        wn.update() 
    
    if bomb1.distance(bomb2 or bomb3) < 40:
        bomb1.goto(random.randint(-250, 250), random.randint(-250,250))
        wn.update()


    #Check border collision        
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor()<-290 or head.distance(bomb1) < 30 or head.distance(bomb2) < 30 or head.distance(bomb3) < 30 or head.distance(bomb4) < 30 or head.distance(bomb5) < 30:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        bomb5.goto(i, j)
        bomb1.goto(a, b)
        bomb2.goto(c, d)
        bomb3.goto(e, f)
        bomb4.goto(g, h)
        

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments list
        segments.clear()

        #Reset score
        score = 0

        #Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal", "bold"))

    #superfood
    if head.distance(s_food) <20:
        #move s_food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        s_food.goto(x,y)

        #bonus segments
        bonus_segment = turtle.Turtle()
        bonus_segment.speed(0)
        bonus_segment.shape("circle")
        bonus_segment.color("blue")
        bonus_segment.penup()
        segments.append(bonus_segment)

        #Shorten the delay
        delay = delay - 0.003

        #increase score
        score = score + 10

        if score > high_score:
            high_score= score

        #Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal", "bold"))

    #move end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to head
    if len(segments) > 0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)



    #food collision
    if head.distance(food) < 20:
        #move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay = delay - 0.001

        #increase score
        score = score + 10

        if score > high_score:
            high_score= score

        #Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal", "bold"))

    #move end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to head
    if len(segments) > 0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head to body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments list
            segments.clear()

            #Reset score
            score = 0

            #Reset the delay
            delay = 0.1

            #Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()




#theres a glitch in the controls where sharp turns is classified as touching the body