#Grace Anspach and Breanna Eafon
import turtle

riley=turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range (5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

def mood(value):
    if value=="happy":
        draw_star("pink")
    if value=="sad":
        draw_star("blue")
    if value=="sleepy":
        draw_star("green")
    if value=="angry":
        draw_star("red")
my_mood=input("How is your mood?\n")
mood(my_mood)
