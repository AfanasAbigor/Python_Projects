import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
"""
#to get the x,y value of the states(50_states.csv):::

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() 
"""

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Press Exit to Close {len(guessed_state)}/50 ", prompt="What's The Another State Name: ").title()

    if answer_state == "Exit":
        missing_states = []
        for i_state in all_states:
            if i_state not in guessed_state:
                missing_states.append(i_state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())








