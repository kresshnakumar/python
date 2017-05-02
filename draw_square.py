import turtle

def draw_square(some_turtle):
    for j in range(1,37):
        some_turtle.left(10)
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red");

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    draw_square(brad)

    window.exitonclick()

draw_art()
