import turtle
import pandas
import string

screen = turtle.Screen()
writer = turtle.Turtle()

writer.penup()
writer.hideturtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Name the states")
screen.tracer(0)

states = pandas.read_csv("50_states.csv")
total = len(states["state"])
# ans = screen.textinput(title=f"Score = {score}/{total}", prompt="What's another state name?")
#
# ans = string.capwords(ans)
game_is_on = []
while len(game_is_on) < 50:
    screen.update()
    ans = screen.textinput(title=f"Score = {len(game_is_on)}/{total}", prompt="What's another state name?")
    ans = string.capwords(ans)
    if ans == "Exit":
        break
    for state in states["state"]:
        if state == ans:
            game_is_on.append(ans)
            row = states[states["state"] == ans]
            posx = row["x"].tolist()
            posy = row["y"].tolist()
            pos = (posx[0], posy[0])
            writer.goto(pos)
            writer.write(arg=ans, align="center", font=("Courier", 8, "normal"))
l = [state for state in states["state"] if state not in game_is_on]
missing_dict = {
    "Missed States": l
}
df = pandas.DataFrame(missing_dict)
df.to_csv("Missing_States.csv")
