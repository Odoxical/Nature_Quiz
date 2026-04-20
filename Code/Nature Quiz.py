import FreeSimpleGUI as sg
import json
import os
########################################################################################################################################################################################################

# Build absolute paths to resource files relative to the script's location, so the quiz works when it is not launched from a intepretor.
base_dir = os.path.dirname(os.path.abspath(__file__))
questions_path = os.path.join(base_dir, "questions.json")
score_path = os.path.join(base_dir, "highscore.txt")

def save(correct_answers,historical_correct_answers):
    """Write a new high score to disk if the current run beat the previous record.
    
    Accepts a TypeError on historical_correct_answers in case the file was
    empty or unreadable, treating any prior value as zero so a new score will
    always be set and acting as a baseline score.
    """
    try:
        if correct_answers>historical_correct_answers:
            # Only overwrite the file when the player sets a new record.
            historical_correct_answers=correct_answers
            with open(score_path,"w") as file:
                file.write(str(historical_correct_answers))
            return historical_correct_answers
        else:
            pass
    except TypeError:
        # historical_correct_answers was None or non-numeric; treat as a fresh start.
        historical_correct_answers=correct_answers
        with open(score_path,"w") as file:
            file.write(str(historical_correct_answers))
        return historical_correct_answers
    
def load_score():
    """Read and return the high score as an integer.
    Returns 0 if the file does not exist yet or contains non-numeric data.
    """
    try:
        with open(score_path,"r") as file:
            return int(file.read())
    except FileNotFoundError:
            return 0
            print("But nothing came")
    except ValueError:
            return 0
########################################################################################################################################################################################################
# Master dictionary that will hold all question data keyed by integer index.
questions = {}



try:
    with open(questions_path,"r") as file:
        raw_data = json.load(file)
        for key, value in raw_data.items():
            questions[int(key)] = value
            
except json.JSONDecodeError:
    # The file exists but has been corrupted, or edited in a way such that it is invalid json.
    sg.popup(f"I am sorry, but the list of questions has been corrupted", title="Final Score", background_color='#0e3947')
    
except FileNotFoundError:
    # questions.json is missing.
    sg.popup(f"I am sorry but something has gone very wrong. the list of questions cannot be found", title="Final Score", background_color='#0e3947')

########################################################################################################################################################################################################
will_iterate = 1          # Tracks which question number we are currently on.
answer_chosen=False
current_question = questions[will_iterate]
answers = current_question["answers"]
historical_correct_answers=load_score()  # Best score from a previous session.
correct_answers=0                        # Running tally for the current session.
load_score()

# Clamp the stored high score to a valid range in case the file was manually edited to a nonsensical value.
if historical_correct_answers < 0 or historical_correct_answers > len(questions):
    save(0,-1)
    load_score()    


# Main menu: two rows of buttons for starting the quiz and managing the score.
menu = [
[sg.Button("Play Quiz", font=("calibri",25, "bold") ), 
sg.Button("See Highscore", font=("calibri",20, "bold"))],
[sg.Button("leave", font=("calibri",20, "bold")),
sg.Button("Clear Highscore", font=("calibri",20, "bold"))],
]

# Layout for multiple-choice (four-answer) questions. Each button corresponds to one of the four answer options. The trivia text and "Next question" button are hidden until the player answers.
four_buttons = [ 
[sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-FOUR_QUESTION_TEXT-", background_color='#0e3947')],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON1-", font=("calibri", 25), size=(40,5), button_color=('#000000','#B5FA42'), border_width = (0)),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON2-", button_color=('#000000','#42FAE3') , size=(40,5), border_width = (0))],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON3-", font=("calibri", 25),button_color=('#000000','#8742FA') ,size=(40,5), border_width = (0)),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON4-", size=(40,5), button_color=('#000000','#FA4259'), border_width = (0))],
[sg.Text("", key="-FOUR_QUESTION_TRIVIA-",font=("calibri"),size=(85,12), background_color='#0e3947'),
 sg.Button("Next question", font =("calibri", 25), key = "-NEXT-", size=(40,5), visible = False)]

]

# Layout for true/false questions. Two large buttons fill the screen; their labels are set dynamically by load().
true_or_false = [
    [sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-TRUE_FALSE_TEXT-", background_color='#0e3947')],
    [sg.Button("", key="-TRUE_OR_FALSE_BUTTON1-", font=("calibri", 25), size=(40,15), button_color=('#000000','#B5FA42'), border_width = (0)),
    sg.Button("", key="-TRUE_OR_FALSE_BUTTON2-", font=("calibri", 25), size=(40,15), button_color=('#000000','#8742FA'), border_width = (0))],
    [sg.Text("", key="-TRUE_FALSE_TRIVIA-", background_color='#0e3947')]
    ]

# The master layout contains all three "screens" as Columns. Only one screen is visible at a time; the others are hidden until needed.
master_layout = [
    [sg.Column(four_buttons,key = "-FOUR_QUESTION-", visible = False, background_color='#0e3947'),
    sg.Column(true_or_false,key = "-TRUE_FALSE-", visible = False, background_color='#0e3947'), #####
    sg.Column(menu, key= "-MENU-", visible = True, background_color='#0e3947')]
    ]


window = sg.Window("Nature Quiz", master_layout, background_color='#0e3947')    
    

########################################################################################################################################################################################################
def load():
    """Show the current question by updating all relevant buttons and text pieces."""
    global current_question, answers
    current_question = questions[will_iterate]
    answers = current_question["answers"]

    # Clear the last question's trivia and hide the Next button so they only appear after answering.
    window["-FOUR_QUESTION_TRIVIA-"].update("")
    window["-TRUE_FALSE_TRIVIA-"].update("")
    window["-NEXT-"].update(visible=False)
    
    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TEXT-"].update(current_question["question_text"])
        #Update the questions text
        for i, answer in enumerate(answers):
            window[f"-BUTTON{i+1}-"].update(answer)
        # Switch to the four-answer screen.
        window["-MENU-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=False)
        window["-FOUR_QUESTION-"].update(visible=True)
    else:
        # Switch to the true/false screen and label the two buttons.
        window["-TRUE_FALSE_TEXT-"].update(current_question["question_text"])
        window["-TRUE_OR_FALSE_BUTTON1-"].update(answers[0])
        window["-TRUE_OR_FALSE_BUTTON2-"].update(answers[1])
        window["-MENU-"].update(visible=False)
        window["-FOUR_QUESTION-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=True)
    window.refresh()
    window.move_to_center()

def on_action(chosen):
    """Evaluate the player's answer, update the score, and reveal the trivia.
    
    Also makes the Next button visible (four-answer layout) or repurposes the
    true/false buttons as a continue prompt, since that layout has no space for a
    dedicated Next button.
    """
    global will_iterate, correct_answers
    window["-NEXT-"].update(visible=True)
    
    if chosen == current_question["true answer"]:
        correct_answers += 1
        result = "Correct!"
    else:
        result = f"Incorrect! The answer was: {current_question['true answer']}"
        pass
    # Combine the result line with the educational trivia blurb for display.
    trivia = f"{result}\n\n{current_question['trivia']}"
    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TRIVIA-"].update(trivia)
    else:
        window["-TRUE_FALSE_TRIVIA-"].update(trivia)
        # Repurpose both true/false buttons as "continue" prompts after answering, since this layout has no space for a separate Next button.
        window["-TRUE_OR_FALSE_BUTTON1-"].update("Press me to continue")
        window["-TRUE_OR_FALSE_BUTTON2-"].update("You could also press me to continue")

        
########################################################################################################################################################################################################
# --- Main event loop ---
running=True
waiting = False  # Waits until a question is anwsered

while running == True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "leave":
        #Trigers if a) the quiz leave button is pressed, b) the x button on the window is pressed, c) the program crashed, or d) the program is terminated by task manager
        #I have no idea how this code triggers on C and D, but as the old sayings goes, dont look a gifted horse in the mouth, and also if it aint broke, don't fix it.
        #check if the score is higher than the highscore, if so, make the highscore the current score.
        save(correct_answers,historical_correct_answers)
        exit()
    elif event == "Play Quiz": #####
        #start from question 1.
        will_iterate=1
        correct_answers = 0
        waiting = False
        load()
        print(will_iterate)
    elif event == "See Highscore":
        # Re-read from disk in case another session updated the file.
        historical_correct_answers = load_score()
        sg.popup(f"The high score is:{historical_correct_answers}", title="High Score", background_color='#0e3947')
    elif event == "Clear Highscore":
        # Overwrite the high score with 0 by passing -1 as the previous high score, guaranteeing that 0 is treated as an improvement by save().
        save(0,-1)
        load_score()
    elif event in ["-BUTTON1-", "-BUTTON2-", "-BUTTON3-", "-BUTTON4-"] and not waiting:
        # Derive the answer index from the last digit of the button key string.
        index = int(event[-2]) -1
        on_action(answers[index])
        waiting = True

    elif event in ["-TRUE_OR_FALSE_BUTTON1-", "-TRUE_OR_FALSE_BUTTON2-"] and not waiting:
        # Map each button to its corresponding anwser in the answers list.
        if event == "-TRUE_OR_FALSE_BUTTON1-":
            index = 0
        else:
            index = 1
        chosen = answers[index]
        on_action(chosen)
        waiting = True  # Block further answer clicks until the player continues.

    elif waiting == True:
        # Any event while waiting advances to the next question.
        will_iterate += 1
        waiting = False
        if will_iterate <= len(questions):
            load()#If there are more questions, load the next question.
        else:
            # All questions exhausted: return to the menu and show the final score.
            window["-FOUR_QUESTION-"].update(visible=False)
            window["-TRUE_FALSE-"].update(visible=False)
            window["-MENU-"].update(visible=True)
            sg.popup(f"Quiz complete! You got {correct_answers} out of {len(questions)} correct!", title="Final Score", background_color='#0e3947')
            save(correct_answers,historical_correct_answers)
                    



exit()
