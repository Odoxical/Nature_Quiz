import FreeSimpleGUI as sg
will_iterate = 1
########################################################################################################################################################################################################
def Save():
    pass
########################################################################################################################################################################################################

questions = {1:{"question_text":"Which of these animals has the most lethal venom",
                "type":"four",
                "answers":["Snake","Spider","JellyFish","Snail"],
                "answer":"Snail",
                "trivia":"""The Neurotoxin of the sydney tunnelweb will kill you withen hours, the inland taipans potent mix of neurotoxin,
hemotoxin, and mytotoxin will kill you within the hour, and the box jellyfishs toxins can kill you in less than five minutes. But
What can be huarenteed, is that they all have potent antivenoms that have been developed. What has neither a antivenom nor a antidote
is Conus geographus, otherwise known as the geography cone, or the cone snail. its conotoxin laced harpoon will kill you within 5 hours, if the fact that
it is a aquatic creature with potent full body paralysis doesnt kill you first."""
                },
2:{"question_text":"Which plant is responsible for the most plant-related poisonings worldwide",
   "type":"four",
   "answers":["Deadly Nightshade","Oleander","Castor Bean","Foxglove"],
   "answer":"Oleander",
   "trivia":"""Oleander is an extremely toxic ornamental shrub found in gardens around the world. Every part of the plant contains
cardiac glycosides that disrupt heart rhythm. Even small amounts can cause vomiting, seizures, and fatal heart arrhythmias.
People have been poisoned by eating the leaves, inhaling smoke from burning branches, or even using the twigs as skewers while cooking."""
   },

3:{"question_text":"There is a plant that is known for using appendages as frag grenades to defend itself from herbivores",
   "type":"true_or_false",
   "answers":["True","False"],
   "answer":"False",
   "trivia":"""There is a plant, coloquially called the dynamite tree, that occasionly releases appendages that relase particulates in all directions at 300+ Kph.
This however, is not a self defence strategy, but a strategy to spread its seed. These apendages are seed pods."""
   },

4:{"question_text":"Which fish is considered the most venomous fish in the world",
   "type":"four",
   "answers":["Lionfish","Stonefish","Pufferfish","Stingray"],
   "answer":"Stonefish",
   "trivia":"""Stonefish are masters of camouflage and look exactly like rocks on the seafloor. When stepped on, they inject venom
through sharp dorsal spines capable of delivering an intense dose of toxins that cause extreme pain, tissue death, shock,
and sometimes heart failure. The pain is often described as the worst pain a person can experience."""
   },

5:{"question_text":"Which plant produces ricin, one of the most deadly natural toxins known",
   "type":"four",
   "answers":["Castor Bean Plant","Hemlock","Yew Tree","Monkshood"],
   "answer":"Castor Bean Plant",
   "trivia":"""The castor bean plant produces ricin inside its seeds. Ricin is a protein toxin that stops cells from producing
essential proteins, causing organ failure. Just a tiny amount can be lethal if inhaled, ingested, or injected. Despite this,
the plant is widely grown because the seeds are also used to make castor oil once the toxin is removed."""
   },

6:{"question_text":"Which seemingly harmless animal causes the most deaths per year",
   "type":"four",
   "answers":["Mosquito","Hippo","Snake","Dog"],
   "answer":"Mosquito",
   "trivia":"""Mosquitoes are responsible for more human deaths every year than any other animal on Earth. They spread diseases
like malaria, dengue fever, Zika, and yellow fever. Malaria alone kills hundreds of thousands of people annually. Despite their
tiny size, they are considered the most dangerous animals to humans in terms of yearly fatalities."""
   }
}

########################################################################################################################################################################################################
             
current_question = questions[will_iterate]
answers = current_question["answers"]

menu = [
[sg.pin(sg.Button("Play Quiz", font=("calibri",25, "bold")))], #####
[sg.pin(sg.Text("", key="-MENU-"))],
[sg.Button("Score", font=("calibri",20, "bold"))],
[sg.pin(sg.Text("", key="-MENU-"))],
[sg.pin(sg.Button("leave", font=("calibri",2, "bold")))],
[sg.pin(sg.Text("", key="-MENU-"))]
]

four_buttons = [ 
[sg.Text(current_question["question_text"], font=("calibri",20,  "bold"))],
[sg.Text("", key="Text")],
[sg.pin(sg.Button(answers[0], font=("calibri", 25), size=(40,5), button_color=('#000000','#B5FA42'))), sg.pin(sg.Button(answers[1], font=("calibri", 25),button_color=('#000000','#42FAE3') , size=(40,5) ))],
[sg.Text("", key="-FOUR_QUESTION-")],
[sg.pin(sg.Button(answers[2], font=("calibri", 25),button_color=('#000000','#8742FA') ,size=(40,5), )), sg.pin(sg.Button(answers[3], font=("calibri", 25), size=(40,5), button_color=('#000000','#FA4259') ))],
[sg.Text("", key="-FOUR_QUESTION-")],

]
true_or_false = [
    [sg.Text(current_question["question_text"], font=("calibri",20,  "bold"))],
    [sg.pin(sg.Button(answers[0], font=("calibri", 25), size=(40,10), button_color=('#000000','#B5FA42')))],
    [sg.Text("", key="-TRUE_FALSE-")],
    [sg.pin(sg.Button(answers[1], font=("calibri", 25), size=(40,10), button_color=('#000000','#8742FA')))],
    [sg.Text("", key="-TRUE_FALSE-")]
    ]

layout = [
    [sg.Column(four_buttons,key = "-FOUR_QUESTION-", visible = False)],
    [sg.Column(true_or_false,key = "-TESTING-", visible = False)], #####
    [sg.Column(menu, key= "-MENU-", visible = True)]
    ]
historical_correct_awnsers=0
correct_awnsers=0
was_last_awnser_correct=None

window = sg.Window("Nature Quiz", layout, background_color='#0e3947')    
    

########################################################################################################################################################################################################
running=True
playing = False
while running == True:
    event, values = window.read()
    if event == answers[0]:
        if answers[0] == current_question["answer"]:
            window["-FOUR_QUESTION-"].update("Correct.")
            window["-TRUE_FALSE-"].update("Correct.")
            correct_awnsers+=1
            was_last_awnser_correct=True
        else:
            window["-FOUR_QUESTION-"].update("incorrect.")
            window["-TRUE_FALSE-"].update("incorrect.")
            was_last_awnser_correct=False
    elif event == answers[1]:
        if answers[1] == "answer":
            window["-TRUE_FALSE-"].update("Correct.")
            window["-FOUR_QUESTION-"].update("Correct.")
            correct_awnsers+=1
            was_last_awnser_correct=True
        else:
            window["-FOUR_QUESTION-"].update("incorrect.")
            window["-TRUE_FALSE-"].update("incorrect.")
            was_last_awnser_correct=False
    elif event == answers[2]:
        if answers[2] == "answer":
            window["-FOUR_QUESTION-"].update("Correct.")
            correct_awnsers+=1
            was_last_awnser_correct=True
        else:
            window["-FOUR_QUESTION-"].update("incorrect.")
            was_last_awnser_correct=False
    elif event == answers[3]:
        if answers[3] == current_question["answer"]:
            window["-FOUR_QUESTION-"].update("Correct.")
            correct_awnsers+=1
            was_last_awnser_correct=True
        else:
            window["-FOUR_QUESTION-"].update("incorrect.")
            was_last_awnser_correct=False
    if event == sg.WIN_CLOSED:
        break


########################################################################################################################################################################################################
    if event == "Play Quiz": #####
        will_iterate=1
        print(will_iterate)
        # Update the text when button is clicked
        window["-FOUR_QUESTION-"].update("This  make it play.")
        for question in questions.keys():
            print(question)
            if was_last_awnser_correct is None:
                print(was_last_awnser_correct)
                print(current_question["type"])
                if current_question["type"] == "four":
                    print(current_question["type"]+"Four question type")
                    window["-MENU-"].update(visible=False)
                    window["-FOUR_QUESTION-"].update(visible=True)
                elif current_question["type"] == "true_or_false":
                    print(current_question["type"]+"True or false question type")
                    window["-MENU-"].update(visible=False)
                    window["-TRUE_FALSE-"].update(visible=True)


                    
            elif was_last_awnser_correct==True:
                correct_awnsers += 1
                if current_question["type"] == "four":
                    window["-TRUE_FALSE-"].update(visible=False)
                    window["-FOUR_QUESTION-"].update(visible=True)
                elif current_question["type"] == "true_or_false":
                    window["-TRUE_FALSE-"].update(visible=True)
                    window["-FOUR_QUESTION-"].update(visible=False)


                    
            elif was_last_awnser_correct==False:
                print("Wrong answer")
                exit()
                    
                will_iterate=will_iterate+1
            else:
                pass


            
    elif event == "Score":
        sg.easy_print("This displays the list of awnsers", answers[0],answers[1],answers[2],answers[3], "This is the current window", window.Key )
        window["-MENU-"].update("This should show your score.")
        window["-FOUR_QUESTION-"].update("If this is shown, then the button position of the first shown window ovewrites all others")
    elif event == "leave":
        window["-MENU-"].update("this should make you leave.")

##    correct_anwsers = 0
##    wrong_awnsers = 0

    while playing == True:
        pass
