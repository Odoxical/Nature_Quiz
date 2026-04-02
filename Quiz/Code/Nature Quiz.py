import FreeSimpleGUI as sg
########################################################################################################################################################################################################
def save():
    pass
def load_score():
    pass
########################################################################################################################################################################################################

questions = {1:{"question_text":"Which of these animals has the most lethal venom",
                "type":"four",
                "answers":["Snake","Spider","JellyFish","Snail"],
                "true answer":"Snail",
                "trivia":"""The Neurotoxin of the sydney tunnelweb will kill you withen hours, the inland taipans potent mix of neurotoxin,
hemotoxin, and mytotoxin will kill you within the hour, and the box jellyfishs toxins can kill you in less than five minutes. But
What can be huarenteed, is that they all have potent antivenoms that have been developed. What has neither a antivenom nor a antidote
is Conus geographus, otherwise known as the geography cone, or the cone snail. its conotoxin laced harpoon will kill you within 5 hours, if the fact that
it is a aquatic creature with potent full body paralysis doesnt kill you first."""
                },
2:{"question_text":"Which plant is responsible for the most plant-related poisonings worldwide",
   "type":"four",
   "answers":["Deadly Nightshade","Oleander","Castor Bean","Foxglove"],
   "true answer":"Oleander",
   "trivia":"""Oleander is an extremely toxic ornamental shrub found in gardens around the world. Every part of the plant contains
cardiac glycosides that disrupt heart rhythm. Even small amounts can cause vomiting, seizures, and fatal heart arrhythmias.
People have been poisoned by eating the leaves, inhaling smoke from burning branches, or even using the twigs as skewers while cooking."""
   },

3:{"question_text":"There is a plant that is known for using appendages as frag grenades to defend itself from herbivores",
   "type":"true_or_false",
   "answers":["True","False"],
   "true answer":"False",
   "trivia":"""There is a plant, coloquially called the dynamite tree, that occasionly releases appendages that relase particulates in all directions at 300+ Kph.
This however, is not a self defence strategy, but a strategy to spread its seed. These apendages are seed pods."""
   },

4:{"question_text":"Which fish is considered the most venomous fish in the world",
   "type":"four",
   "answers":["Lionfish","Stonefish","Pufferfish","Stingray"],
   "true answer":"Stonefish",
   "trivia":"""Stonefish are masters of camouflage and look exactly like rocks on the seafloor. When stepped on, they inject venom
through sharp dorsal spines capable of delivering an intense dose of toxins that cause extreme pain, tissue death, shock,
and sometimes heart failure. The pain is often described as the worst pain a person can experience."""
   },

5:{"question_text":"Which plant produces ricin, one of the most deadly natural toxins known",
   "type":"four",
   "answers":["Castor Bean Plant","Hemlock","Yew Tree","Monkshood"],
   "true answer":"Castor Bean Plant",
   "trivia":"""The castor bean plant produces ricin inside its seeds. Ricin is a protein toxin that stops cells from producing
essential proteins, causing organ failure. Just a tiny amount can be lethal if inhaled, ingested, or injected. Despite this,
the plant is widely grown because the seeds are also used to make castor oil once the toxin is removed."""
   },

  6: {
    "question_text": "Carnivorous plants subsist solely on insects.",
    "type": "true_or_false",
    "answers": ["True", "False"],
    "true answer": "False",
    "trivia": """Carnivorous plants only get nitrogen, phosphorus, and potassium from insects.
They still need sunlight and water."""
  },

  7: {
    "question_text": "Which of these trees is the deadliest?",
    "type": "four",
    "answers": ["Australian Ironwood", "Dragon's Blood", "Strangler Fig", "The Manchineel Tree"],
    "true answer": "The Manchineel Tree",
    "trivia": """The Manchineel tree, also known as the tree of death, is deadly in every single piece. This is due to
its sap, which causes second and third degree burns, intense pain, blisters, dermatitis, blindness, lung damage, and more.
This sap is found in every part of the tree, which is even worse because this tree looks no different than any other
tropical american tree. This tree is also illegal to cut down because it is endangered.
The Strangler Fig can only strangle other trees. It is harmless to animal life.
The Dragon's Blood tree has thick, crimson sap, and berries that are commonly described as fleshy. Other than giving
your dog depression, it is completely harmless and was even used in medicine.
Other than being poisonous when eaten or burned, because its Australia, the Australian Ironwood tree is completely harmless."""
  },

  8: {
    "question_text": "True or false, There is a tree that utilises fragmentation grenade-like items to defend itself against herbivores.",
    "type": "true_or_false",
    "answers": ["True", "False"],
    "true answer": "False",
    "trivia": """False. There is a plant that uses an item that explodes and sends detritus at 240 kilometres per hour,
but it doesn't do this as a defence mechanism. It does this to spread its seeds.
This tree is called the Dynamite Tree."""
  }
}


########################################################################################################################################################################################################

will_iterate = 1
answer_chosen=False
current_question = questions[will_iterate]
answers = current_question["answers"] #I had completely forgot about this bit of code. Thank you, me. or is it just thank me? an intresting conundrum.
historical_correct_answers=0
correct_answers=0

menu = [
[sg.pin(sg.Button("Play Quiz", font=("calibri",25, "bold")))], 
[sg.Button("Score", font=("calibri",20, "bold"))],
[sg.pin(sg.Button("leave", font=("calibri",2, "bold")))],
]

four_buttons = [ 
[sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-FOUR_QUESTION_TEXT-")],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON1-", font=("calibri", 25), size=(40,5), button_color=('#000000','#B5FA42')),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON2-", button_color=('#000000','#42FAE3') , size=(40,5))],
[sg.Button("If you're seeing this, the question iteration code broke", key="-BUTTON3-", font=("calibri", 25),button_color=('#000000','#8742FA') ,size=(40,5)),
sg.Button("If you're seeing this, the question iteration code broke", font=("calibri", 25), key="-BUTTON4-", size=(40,5), button_color=('#000000','#FA4259'))],
[sg.Text("", key="-FOUR_QUESTION_TRIVIA-",font=("calibri"),size=(80,12))],

]
true_or_false = [
    [sg.Text(current_question["question_text"], font=("calibri",20,  "bold"), key = "-TRUE_FALSE_TEXT-")],
    [sg.Button("", key="-TRUE_OR_FALSE_BUTTON1-", font=("calibri", 25), size=(40,15), button_color=('#000000','#B5FA42')),
    sg.Button("", key="-TRUE_OR_FALSE_BUTTON2-", font=("calibri", 25), size=(40,15), button_color=('#000000','#8742FA'))],
    [sg.Text("", key="-TRUE_FALSE_TRIVIA-")]
    ]

master_layout = [
    [sg.Column(four_buttons,key = "-FOUR_QUESTION-", visible = False),
    sg.Column(true_or_false,key = "-TRUE_FALSE-", visible = False), #####
    sg.Column(menu, key= "-MENU-", visible = True)]
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
        window["-FOUR_QUESTION-"].update(visible=True)
    else:
        window["-TRUE_FALSE_TEXT-"].update(current_question["question_text"])
        window["-MENU-"].update(visible=False)
        window["-TRUE_FALSE-"].update(visible=True)
        window["-FOUR_QUESTION-"].update(visible=False)

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
        save()
        exit()
    elif event == "Play Quiz": #####
        will_iterate=1
        correct_answers = 0
        waiting = False
        load()
        print(will_iterate)
    elif event == "Score":
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
            sg.popup(f"Quiz complete! You got {correct_answers} out of {len(questions)} correct!", title="Final Score")
                    



exit()
