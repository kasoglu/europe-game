import turtle
import pandas

screen = turtle.Screen()
screen.title("Europe Countries Game")
image = "europe-countries.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("europe.csv")
all_countries = data.country.to_list()

guessed_countries = []

while len(guessed_countries) < len(data):
    user_answer = screen.textinput(title=f"{len(guessed_countries)}/{len(data)} Countries Correct",
                                    prompt="What's the country name?").title()

    if user_answer in all_countries:
        guessed_countries.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == user_answer]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(user_answer)
