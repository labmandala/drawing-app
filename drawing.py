import turtle as turtle
import random

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)

turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  # Star
  for i in range(0,5):
    turtle.pencolor("gold")
    turtle.forward(110)
    turtle.right(216)

def square():
  # Square
  for i in range(0,4):
    turtle.pencolor("purple")
    turtle.forward(100)
    turtle.right(90)
   
def hexagon():
  # Hexagon
  for i in range(0,6):
    turtle.pencolor("black")
    turtle.forward(100)
    turtle.right(60)

def circle():
  # Circle
  for i in range(0,1):
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.circle(60)
    turtle.end_fill()

def triangle():
  # Equilateral Triangle
  for i in range(3):
    turtle.pencolor("black")
    turtle.forward(100)
    turtle.left(120)

def pentagon():
  # Pentagon
  for i in range(0,5):
    turtle.pencolor("green")
    turtle.forward(100)
    turtle.right(72)

selection = input("1. Star\n2. Square\n3. Hexagon\n4. Circle\n5. Triangle\n6. Pentagon\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
  turtle.done()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
  turtle.done()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
  turtle.done()
elif selection == "4":
  print("Excellent choice! Go to the result tab to see your creation.")
  circle()
  turtle.done()
elif selection == "5":
  print("Excellent choice! Go to the result tab to see your creation.")
  triangle()
  turtle.done()
elif selection == "6":
  print("Excellent choice! Go to the result tab to see your creation.")
  pentagon()
  turtle.done()
  