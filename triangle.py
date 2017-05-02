import turtle

def draw_square(some_turtle):
    #for j in range(1,37):
        #some_turtle.left(10)
        some_turtle.forward(100)
        some_turtle.right(135)
        some_turtle.forward(75)
        some_turtle.right(90)
        some_turtle.forward(75)
        #some_turtle.right(45)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red");

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    draw_square(brad)

    window.exitonclick()

draw_art()
