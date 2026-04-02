import FreeSimpleGUI as sg
import json
########################################################################################################################################################################################################
def save(correct_answers,historical_correct_answers):
    try:
        if correct_answers>historical_correct_answers:
            historical_correct_answers=correct_answers
            with open("highscore.txt","w") as file:
                file.write(str(historical_correct_answers))
            return historical_correct_answers
        else:
            pass
    except TypeError:
        historical_correct_answers=correct_answers
        with open("highscore.txt","w") as file:
            file.write(str(historical_correct_answers))
        return historical_correct_answers
    
def load_score():
    try:
        with open("highscore.txt","r") as file:
            return int(file.read())
    except FileNotFoundError:
            return 0
            print("But nothing came")
########################################################################################################################################################################################################
questions = {}
try:
    with open("questions.json","r") as file:
        raw_data = json.load(file)
        for key, value in raw_data.items():
            questions[int(key)] = value
            
except json.JSONDecodeError:
    sg.popup(f"I am sorry, but the list of questions has been corrupted", title="Final Score", background_color='#0e3947')
except FileNotFoundError:
    sg.popup(f"I am sorry but something has gone very wrong. the list of questions cannot be found", title="Final Score", background_color='#0e3947')


########################################################################################################################################################################################################
will_iterate = 1
answer_chosen=False
current_question = questions[will_iterate]
answers = current_question["answers"]
historical_correct_answers=load_score()
correct_answers=0
load_score()

menu = [
[sg.Button("Play Quiz", font=("calibri",25, "bold") ), 
sg.Button("See Highscore", font=("calibri",20, "bold"))],
[sg.Button("leave", font=("calibri",20, "bold")),
sg.Button("Clear Highscore", font=("calibri",20, "bold"))],
]

four_buttons = [ 
[sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-FOUR_QUESTION_TEXT-", background_color='#0e3947')],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON1-", font=("calibri", 25), size=(40,5), button_color=('#000000','#B5FA42'), border_width = (0)),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON2-", button_color=('#000000','#42FAE3') , size=(40,5), border_width = (0))],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON3-", font=("calibri", 25),button_color=('#000000','#8742FA') ,size=(40,5), border_width = (0)),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON4-", size=(40,5), button_color=('#000000','#FA4259'), border_width = (0))],
[sg.Text("", key="-FOUR_QUESTION_TRIVIA-",font=("calibri"),size=(80,12), background_color='#0e3947')],

]
true_or_false = [
    [sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-TRUE_FALSE_TEXT-", background_color='#0e3947')],
    [sg.Button("", key="-TRUE_OR_FALSE_BUTTON1-", font=("calibri", 25), size=(40,15), button_color=('#000000','#B5FA42'), border_width = (0)),
    sg.Button("", key="-TRUE_OR_FALSE_BUTTON2-", font=("calibri", 25), size=(40,15), button_color=('#000000','#8742FA'), border_width = (0))],
    [sg.Text("", key="-TRUE_FALSE_TRIVIA-", background_color='#0e3947')]
    ]

master_layout = [
    [sg.Column(four_buttons,key = "-FOUR_QUESTION-", visible = False, background_color='#0e3947'),
    sg.Column(true_or_false,key = "-TRUE_FALSE-", visible = False, background_color='#0e3947'), #####
    sg.Column(menu, key= "-MENU-", visible = True, background_color='#0e3947')]
    ]


window = sg.Window("Nature Quiz", master_layout, background_color='#0e3947')    
    

########################################################################################################################################################################################################
def load():
    """show the current question"""
    global current_question, answers
    current_question = questions[will_iterate]
    answers = current_question["answers"]

    window["-FOUR_QUESTION_TRIVIA-"].update("")
    window["-TRUE_FALSE_TRIVIA-"].update("")    
    
    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TEXT-"].update(current_question["question_text"])
        """Update the questions text"""
        for i, answer in enumerate(answers):
            window[f"-BUTTON{i+1}-"].update(answer)
        window["-MENU-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=False)
        window.move_to_center()
        window["-FOUR_QUESTION-"].update(visible=True)
    else:
        window["-TRUE_FALSE_TEXT-"].update(current_question["question_text"])
        window["-TRUE_OR_FALSE_BUTTON1-"].update(answers[0])
        window["-TRUE_OR_FALSE_BUTTON2-"].update(answers[1])
        window["-MENU-"].update(visible=False)
        window["-FOUR_QUESTION-"].update(visible=False)
        window.move_to_center()
        window["-TRUE_FALSE-"].update(visible=True)

def on_action(chosen):
    """check whether answer was correct, show the trivia, advance the quiz, or end the quiz"""
    global will_iterate, correct_answers

    if chosen == current_question["true answer"]:
        correct_answers += 1
        result = "Correct!"
    else:
        result = f"Incorrect! The answer was: {current_question['true answer']}"
        pass
    trivia = f"{result}\n\n{current_question['trivia']}"
    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TRIVIA-"].update(trivia)
    else:
        window["-TRUE_FALSE_TRIVIA-"].update(trivia)

        
########################################################################################################################################################################################################
running=True
waiting = False

while running == True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "leave":
        save(correct_answers,historical_correct_answers)
        exit()
    elif event == "Play Quiz": #####
        will_iterate=1
        correct_answers = 0
        waiting = False
        load()
        print(will_iterate)
    elif event == "See Highscore":
        historical_correct_answers = load_score()
        sg.popup(f"The high score is:{historical_correct_answers}", title="High Score", background_color='#0e3947')
    elif event == "Clear Highscore":
        save(0,-1)
        load_score()
    elif event in ["-BUTTON1-", "-BUTTON2-", "-BUTTON3-", "-BUTTON4-"] and not waiting:
        index = int(event[-2]) -1
        on_action(answers[index])
        waiting = True

    elif event in ["-TRUE_OR_FALSE_BUTTON1-", "-TRUE_OR_FALSE_BUTTON2-"] and not waiting:
        if event == "-TRUE_OR_FALSE_BUTTON1-":
            index = 0
        else:
            index = 1
        chosen = answers[index]
        on_action(chosen)
        waiting = True

    elif waiting == True:
        will_iterate += 1
        waiting = False
        if will_iterate <= len(questions):
            load()
        else:
            window["-FOUR_QUESTION-"].update(visible=False)
            window["-TRUE_FALSE-"].update(visible=False)
            window["-MENU-"].update(visible=True)
            sg.popup(f"Quiz complete! You got {correct_answers} out of {len(questions)} correct!", title="Final Score", background_color='#0e3947')
            save(correct_answers,historical_correct_answers)
                    



exit()
