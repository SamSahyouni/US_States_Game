import turtle as t
import pandas as p
from write import Writer
screen = t.Screen()
screen.setup(height=600,width=800)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
write_state = Writer()
guessed_states = []

while len(guessed_states) < 50:
    # Get user to guess the states, convert to title case
    answer_state = screen.textinput(title="Guess the State", prompt= f"What's another State's name? {len(guessed_states)}/50").title()
    # Exit and export unknown states to csv
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        unknown_states = p.DataFrame(missing_states)
        unknown_states.to_csv("states_to_learn.csv")
        break
    # Check with .csv to see if state was correct
    states_data = p.read_csv("50_states.csv")
    states_list = states_data["state"].to_list()
    if answer_state in states_list:
    # if correct, print it on the map, and increase correct/50 in the text box
        guessed_states.append(answer_state)
        print("yes")
        # get a hold of state's coordinates
        correct_row = states_data[states_data.state == answer_state]
        x = correct_row.x
        x_coord = x.to_list()
        y = correct_row.y
        y_coord = y.to_list()
        coordinates = (x_coord[0],y_coord[0])
        # use write class to write the state on the map
        write_state.update_map(coordinates,answer_state)
    # if incorrect, guess again
    else:
        answer_state = screen.textinput(title="Guess the State", prompt=f"What's another State's name? {len(guessed_states)}/50").title()


