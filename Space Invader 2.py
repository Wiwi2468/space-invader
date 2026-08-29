import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 600)

# Player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Aliens
aliens = []

for i in range(5):
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("square")
    alien.penup()
    alien.goto(
        random.randint(-250, 250),
        random.randint(50, 250)
    )
    aliens.append(alien)

# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.hideturtle()

# Move aliens randomly

def move_aliens():
    for alien in aliens:
        alien.setx(alien.xcor() + random.randint(-20, 20))
        alien.sety(alien.ycor() + random.randint(-20, 20))
        while alien.xcor() > 600 or alien.ycor() > 600:
            alien.setx(alien.xcor() + random.randint(-20, 20))
            alien.sety(alien.ycor() + random.randint(-20, 20))
        

    screen.ontimer(move_aliens, 200)

def left():
    player.setx(player.xcor() - 20)

def right():
    player.setx(player.xcor() + 20)

def shoot():
    bullet.goto(player.xcor(), player.ycor())
    bullet.showturtle()

    while bullet.ycor() < 300:
        bullet.sety(bullet.ycor() + 10)

        # Hit alien
        for alien in aliens:
            if alien.isvisible() and bullet.distance(alien) < 25:
                alien.hideturtle()
                bullet.hideturtle()
                print("Alien hit!")
                return

    bullet.hideturtle()

screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(shoot, "space")

move_aliens()

screen.mainloop()