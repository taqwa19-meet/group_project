from turtle import *
import turtle
import random
screen = turtle.getscreen()
turtle.shape("circle")
size = 5
turtle.shapesize(size)
turtle.penup()
Screen()
title("Turtle Keys")
turtle_a = None
turtle_b = None
turtle_c = None
turtle_d = None
turtle_e = None
turtle_f = None
circles=[]
letters=[]
dares = ["bring water to all the group you are playing with", "nice job!!! now u own your friends 10 dollars", "Continuously talk for 2 minutes without stopping", " Smell a dirty sock for 10 seconds", " Give a tree in your yard, a big hug.", "Act like a dog and get petted by everyone", "Ask a total stranger for their number","Let someone write a word on your forehead in permanent marker", "Post an embarrassing picture of yourself online", "Imitate a monkey as best you can", "Eat a raw egg", "sing a song all the way through to the end", "Do a model runway walk outside on the sidewalk", "Jump on one leg for 20 seconds with both hands on your head", "Dance Crazy", "Wrap yourself up in toilet paper and take a picture",
"Whenever someone says 'like' you must say 'there you go again' for the next hour","drink five cups of water","Dance crazy with no music","Go outside and tell the first person you see that you like/love/hate them","Have the person on your right do your hair any way they want and you have to keep it like that for the rest of the game" ]
turtle_dare= turtle.clone()
turtle_dare.hideturtle()

def a():
     global turtle_a
     turtle_a = turtle.clone()
     turtle_a.goto(-550,-100)
     turtle_a.showturtle()
     turtle_a.color("red")
     circles.append(turtle_a)
     turtle_a2=turtle.clone()
     turtle_a2.goto(-575,-130)
     turtle_a2.write("A",font=("Arial", 50, "normal"))
     letters.append(turtle_a2)
     
def b():
     global turtle_b
     turtle_b = turtle.clone()
     turtle_b.goto(-550,50)
     turtle_b.showturtle()
     turtle_b.color("gray")
     circles.append(turtle_b)
     turtle_b2=turtle.clone()
     turtle_b2.goto(-570,18)
     turtle_b2.write("B",font=("Arial", 50, "normal"))
     letters.append(turtle_b2)
     
def c():
     global turtle_c
     turtle_c = turtle.clone()
     turtle_c.goto(-550,200)
     turtle_c.showturtle()
     turtle_c.color("yellow")
     circles.append(turtle_c)
     turtle_c2=turtle.clone()
     turtle_c2.goto(-575,165)
     turtle_c2.write("C",font=("Arial", 50, "normal"))
     letters.append(turtle_c2)
     
def d():
     global turtle_d
     turtle_d = turtle.clone()
     turtle_d.goto(550,-100)
     turtle_d.showturtle()
     turtle_d.color("purple")
     circles.append(turtle_d)
     turtle_d2=turtle.clone()
     turtle_d2.goto(530,-135)
     turtle_d2.clear()
     turtle_d2.write("D",font=("Arial", 50, "normal"))
     letters.append(turtle_d2)
     
def e():
     global turtle_e
     turtle_e = turtle.clone()
     turtle_e.goto(550,50)
     turtle_e.showturtle()
     turtle_e.color("white")
     circles.append(turtle_e)
     turtle_e2=turtle.clone()
     turtle_e2.goto(530,15)
     turtle_e2.write("E",font=("Arial", 50, "normal"))
     letters.append(turtle_e2)
     
def f():
     global turtle_f
     turtle_f = turtle.clone()
     turtle_f.goto(550,200)
     turtle_f.showturtle()
     turtle_f.color("blue")
     circles.append(turtle_f)
     turtle_f2=turtle.clone()
     turtle_f2.goto(530,165)
     turtle_f2.write("F",font=("Arial", 50, "normal"))
     letters.append(turtle_f2)

def pick_circle():
##     global turtle_a2
##     global turtle_b2
##     global turtle_c2
##     global turtle_d2
##     global turtle_e2
##     global turtle_f2
     random_circle = random.choice(circles)
     random_circle.goto(0, 120)
     turtle_dare.clear()
     chosen_dare=random.choice(dares)
     turtle_dare.goto(-550,250)
     turtle_dare.write(chosen_dare,font=("Arial", 30, "normal"))
##     if random_circle == turtle_a:
##          turtle_a2.goto(0,0)
##     elif random_circle == turtle_b:
##          turtle_b2.goto(0,0)
##     elif random_circle == turtle_c:
##          turtle_c2.goto(0,0)
##     elif random_circle == turtle_d:
##          turtle_d2.goto(0,0)
##     elif random_circle == turtle_e:
##          turtle_e2.goto(0,0)
##     elif random_circle == turtle_f:
##          turtle_f2.goto(0,0)

for i in circles:
     i.shapesize(size)
     if size>=5:
          size = size - 1
     elif size<=5:
          size = size + 1

onkey(a, "a")
onkey(b, "b")
onkey(c, "c")
onkey(d, "d")
onkey(e, "e")
onkey(f, "f")
onkey(pick_circle, "space")

turtle.bgpic("logo2.gif")

listen()
turtle.hideturtle()
#mainloop()

