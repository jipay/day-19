from turtle import Turtle, Screen
from myturtle import MyTurtle


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_start = 100.0
is_race_on = False

if user_bet:
    is_race_on = True
for c in colors:
    turtles.append(MyTurtle(x=-230.0, y=y_start, color=c))
    y_start -= 50.0

while is_race_on:
    for turtle in turtles:
        if turtle.t.xcor() > 230:
            if user_bet == turtle.t.color():
                print(f"You won your bet, the {turtle.id} turtle wins!")
            else:
                print(f"You loose your bet, the {turtle.id} turtle wins!")
            is_race_on = False
            break
        turtle.movefrwd()

screen.exitonclick()
