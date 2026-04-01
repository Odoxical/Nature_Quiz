import FreeSimpleGUI as sg

########################################################################################################################################################################################################
questions = {1:{"question_text":"Which of these animals has the most lethal venom",
                "type":"four",
                "answers":["Snake","Spider","JellyFish","Snail"],
                "true answer":"Snail",
                "trivia":"""The Neurotoxin of the sydney tunnelweb will kill you withen hours..."""
                },
2:{"question_text":"Which plant is responsible for the most plant-related poisonings worldwide",
   "type":"four",
   "answers":["Deadly Nightshade","Oleander","Castor Bean","Foxglove"],
   "true answer":"Oleander",
   "trivia":"""Oleander is an extremely toxic ornamental shrub..."""
   },
3:{"question_text":"There is a plant that is known for using appendages as frag grenades to defend itself from herbivores",
   "type":"true_or_false",
   "answers":["True","False"],
   "true answer":"False",
   "trivia":"""There is a plant, coloquially called the dynamite tree..."""
   },
4:{"question_text":"Which fish is considered the most venomous fish in the world",
   "type":"four",
   "answers":["Lionfish","Stonefish","Pufferfish","Stingray"],
   "true answer":"Stonefish",
   "trivia":"""Stonefish are masters of camouflage..."""
   },
5:{"question_text":"Which plant produces ricin, one of the most deadly natural toxins known",
   "type":"four",
   "answers":["Castor Bean Plant","Hemlock","Yew Tree","Monkshood"],
   "true answer":"Castor Bean Plant",
   "trivia":"""The castor bean plant produces ricin inside its seeds..."""
   },
6: {"question_text": "Carnivorous plants subsist solely on insects.",
    "type": "true_or_false",
    "answers": ["True", "False"],
    "true answer": "False",
    "trivia": """Carnivorous plants only get nitrogen, phosphorus, and potassium from insects."""
  },
7: {"question_text": "Which of these trees is the deadliest?",
    "type": "four",
    "answers": ["Australian Ironwood", "Dragon's Blood", "Strangler Fig", "The Manchineel Tree"],
    "true answer": "The Manchineel Tree",
    "trivia": """The Manchineel tree, also known as the tree of death..."""
  },
8: {"question_text": "True or false, There is a tree that utilises fragmentation grenade-like items to defend itself against herbivores.",
    "type": "true_or_false",
    "answers": ["True", "False"],
    "true answer": "False",
    "trivia": """False. There is a plant that uses an item that explodes..."""
  }
}

########################################################################################################################################################################################################

will_iterate = 1
answer_chosen = False
correct_answers = 0
current_question = questions[will_iterate]
answers = current_question["answers"]

menu = [
    [sg.Button("Play Quiz", font=("calibri", 25, "bold"))],
    [sg.Button("Score", font=("calibri", 20, "bold"))],
    [sg.Button("leave", font=("calibri", 15, "bold"))],
]

four_buttons = [
    [sg.Text("", key="-FOUR_QUESTION_TEXT-", font=("calibri", 20, "bold"))],
    [sg.Button("", key="-BUTTON1-", font=("calibri", 25), size=(40, 5), button_color=('#000000', '#B5FA42')),
     sg.Button("", key="-BUTTON2-", font=("calibri", 25), size=(40, 5), button_color=('#000000', '#42FAE3'))],
    [sg.Button("", key="-BUTTON3-", font=("calibri", 25), size=(40, 5), button_color=('#000000', '#8742FA')),
     sg.Button("", key="-BUTTON4-", font=("calibri", 25), size=(40, 5), button_color=('#000000', '#FA4259'))],
    [sg.Text("", key="-FOUR_QUESTION_TRIVIA-", font=("calibri", 14), size=(80, 5))],
]

true_or_false = [
    [sg.Text("", key="-TRUE_FALSE_TEXT-", font=("calibri", 20, "bold"))],
    [sg.Button("", key="-TOF_BUTTON1-", font=("calibri", 25), size=(40, 10), button_color=('#000000', '#B5FA42'))],
    [sg.Button("", key="-TOF_BUTTON2-", font=("calibri", 25), size=(40, 10), button_color=('#000000', '#8742FA'))],
    [sg.Text("", key="-TRUE_FALSE_TRIVIA-", font=("calibri", 14), size=(80, 5))],
]

master_layout = [
    [sg.Column(four_buttons, key="-FOUR_QUESTION-", visible=False)],
    [sg.Column(true_or_false, key="-TRUE_FALSE-", visible=False)],
    [sg.Column(menu, key="-MENU-", visible=True)],
]

window = sg.Window("Nature Quiz", master_layout, background_color='#0e3947')


########################################################################################################################################################################################################

def load_question():
    """Update all UI elements to show the current question."""
    global current_question, answers
    current_question = questions[will_iterate]
    answers = current_question["answers"]

    # Clear any trivia from last question
    window["-FOUR_QUESTION_TRIVIA-"].update("")
    window["-TRUE_FALSE_TRIVIA-"].update("")

    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TEXT-"].update(current_question["question_text"])
        for i, answer in enumerate(answers):
            window[f"-BUTTON{i+1}-"].update(answer)
        window["-MENU-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=False)
        window["-FOUR_QUESTION-"].update(visible=True)

    elif current_question["type"] == "true_or_false":
        window["-TRUE_FALSE_TEXT-"].update(current_question["question_text"])
        window["-TOF_BUTTON1-"].update(answers[0])
        window["-TOF_BUTTON2-"].update(answers[1])
        window["-MENU-"].update(visible=False)
        window["-FOUR_QUESTION-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=True)


def handle_answer(chosen):
    """Check the answer, show trivia, and advance or end the quiz."""
    global will_iterate, correct_answers

    if chosen == current_question["true answer"]:
        correct_answers += 1
        result = "Correct!"
    else:
        result = f"Incorrect! The answer was: {current_question['true answer']}"

    trivia = f"{result}\n\n{current_question['trivia']}"

    # Show result + trivia, then a Next button
    if current_question["type"] == "four":
        window["-FOUR_QUESTION_TRIVIA-"].update(trivia)
    else:
        window["-TRUE_FALSE_TRIVIA-"].update(trivia)

    # Disable answer buttons until Next is clicked
    # (we track this with answer_chosen below)


########################################################################################################################################################################################################

waiting_for_next = False  # True when trivia is showing and we're waiting for the user to click Next

running = True
while running:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "leave":
        break

    elif event == "Play Quiz":
        will_iterate = 1
        correct_answers = 0
        waiting_for_next = False
        load_question()

    elif event == "Score":
        sg.popup(f"You got {correct_answers} out of {len(questions)} correct!", title="Score")

    # --- Four-answer question buttons ---
    elif event in ["-BUTTON1-", "-BUTTON2-", "-BUTTON3-", "-BUTTON4-"] and not waiting_for_next:
        index = int(event[-2]) - 1  # extracts 1,2,3,4 from key, converts to 0-3
        chosen = answers[index]
        handle_answer(chosen)
        waiting_for_next = True

    # --- True/False question buttons ---
    elif event in ["-TOF_BUTTON1-", "-TOF_BUTTON2-"] and not waiting_for_next:
        index = 0 if event == "-TOF_BUTTON1-" else 1
        chosen = answers[index]
        handle_answer(chosen)
        waiting_for_next = True

    # Clicking anywhere on the trivia advances to next question
    # Better: add a Next button. But for simplicity, re-read on any event:
    elif waiting_for_next:
        will_iterate += 1
        waiting_for_next = False
        if will_iterate <= len(questions):
            load_question()
        else:
            # Quiz finished
            window["-FOUR_QUESTION-"].update(visible=False)
            window["-TRUE_FALSE-"].update(visible=False)
            window["-MENU-"].update(visible=True)
            sg.popup(f"Quiz complete! You got {correct_answers} out of {len(questions)} correct!", title="Final Score")

window.close()
