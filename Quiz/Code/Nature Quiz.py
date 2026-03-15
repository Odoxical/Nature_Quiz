import FreeSimpleGUI as sg
iterate = 1

########################################################################################################################################################################################################

questions = {1:{"question":"Which of these animals has the most lethal venom",
                "type":"four",
                "answers":["Snake","Spider","JellyFish","Snail"],
                "answer":"Snail",
                "trivia":"""The Neurotoxin of the sydney tunnelweb will kill you withen hours, the inland taipans potent mix of neurotoxin,
hemotoxin, and mytotoxin will kill you within the hour, and the box jellyfishs toxins can kill you in less than five minutes. But
What can be huarenteed, is that they all have potent antivenoms that have been developed. What has neither a antivenom nor a antidote
is Conus geographus, otherwise known as the geography cone, or the cone snail. its conotoxin laced harpoon will kill you within 5 hours, if the fact that
it is a aquatic creature with potent full body paralysis doesnt kill you first."""
                },
2:{"question":"Which plant is responsible for the most plant-related poisonings worldwide",
   "type":"four",
   "answers":["Deadly Nightshade","Oleander","Castor Bean","Foxglove"],
   "answer":"Oleander",
   "trivia":"""Oleander is an extremely toxic ornamental shrub found in gardens around the world. Every part of the plant contains
cardiac glycosides that disrupt heart rhythm. Even small amounts can cause vomiting, seizures, and fatal heart arrhythmias.
People have been poisoned by eating the leaves, inhaling smoke from burning branches, or even using the twigs as skewers while cooking."""
   },

3:{"question":"There is a plant that is known for using appendages as frag grenades to defend itself from herbivores",
   "type":"true_or_false",
   "answers":["True","False"],
   "answer":"False",
   "trivia":"""There is a plant, coloquially called the dynamite tree, that occasionly releases appendages that relase particulates in all directions at 300+ Kph.
This however, is not a self defence strategy, but a strategy to spread its seed. These apendages are seed pods."""
   },

4:{"question":"Which fish is considered the most venomous fish in the world",
   "type":"four",
   "answers":["Lionfish","Stonefish","Pufferfish","Stingray"],
   "answer":"Stonefish",
   "trivia":"""Stonefish are masters of camouflage and look exactly like rocks on the seafloor. When stepped on, they inject venom
through sharp dorsal spines capable of delivering an intense dose of toxins that cause extreme pain, tissue death, shock,
and sometimes heart failure. The pain is often described as the worst pain a person can experience."""
   },

5:{"question":"Which plant produces ricin, one of the most deadly natural toxins known",
   "type":"four",
   "answers":["Castor Bean Plant","Hemlock","Yew Tree","Monkshood"],
   "answer":"Castor Bean Plant",
   "trivia":"""The castor bean plant produces ricin inside its seeds. Ricin is a protein toxin that stops cells from producing
essential proteins, causing organ failure. Just a tiny amount can be lethal if inhaled, ingested, or injected. Despite this,
the plant is widely grown because the seeds are also used to make castor oil once the toxin is removed."""
   },

6:{"question":"Which seemingly harmless animal causes the most deaths per year",
   "type":"four",
   "answers":["Mosquito","Hippo","Snake","Dog"],
   "answer":"Mosquito",
   "trivia":"""Mosquitoes are responsible for more human deaths every year than any other animal on Earth. They spread diseases
like malaria, dengue fever, Zika, and yellow fever. Malaria alone kills hundreds of thousands of people annually. Despite their
tiny size, they are considered the most dangerous animals to humans in terms of yearly fatalities."""
   }
}

########################################################################################################################################################################################################
             
question = questions[iterate]
answers = question["answers"]
four_buttons = [ 
##[sg.Button("Play Quiz", font=("calibri",25, "bold"))],
##[sg.Text("", key="-FOUR_QUESTION-")],
##[sg.Button("Score", font=("calibri",20, "bold"))],
##[sg.Text("", key="-FOUR_QUESTION-")],
##[sg.Button("leave", font=("calibri",2, "bold"))],
##[sg.Text("", key="-FOUR_QUESTION-")],


[sg.Text(question["question"], font=("calibri",20,  "bold"))],
[sg.Text("", key="Text")],
[sg.pin(sg.Button(answers[0], font=("calibri", 25), size=(40,5), button_color=('#000000','#B5FA42'))), sg.pin(sg.Button(answers[1], font=("calibri", 25),button_color=('#000000','#42FAE3') , size=(40,5) ))],
[sg.Text("", key="-FOUR_QUESTION-")],
[sg.pin(sg.Button(answers[2], font=("calibri", 25),button_color=('#000000','#8742FA') ,size=(40,5), )), sg.pin(sg.Button(answers[3], font=("calibri", 25), size=(40,5), button_color=('#000000','#FA4259') ))],
[sg.Text("", key="-FOUR_QUESTION-")],

]
true_or_false = [
    [sg.Text(question["question"], font=("calibri",20,  "bold"))],
    [sg.pin(sg.Button(answers[0], font=("calibri", 25), size=(40,10), button_color=('#000000','#B5FA42')))],
    [sg.Text("", key="-TRUE_FALSE-")],
    [sg.pin(sg.Button(answers[1], font=("calibri", 25), size=(40,10), button_color=('#000000','#8742FA')))],
    [sg.Text("", key="-TRUE_FALSE-")]
    ]

layout = [
    [sg.Column(four_buttons,key = "-BUTTONS-", visible = False)],
    [sg.Column(true_or_false,key = "-TESTING-", visible = True)]
    ]
historical_correct_awnsers=0
correct_awnsers=0
was_last_awnser_correct=False

window = sg.Window("Nature Quiz", layout, background_color='#0e3947')    
    

########################################################################################################################################################################################################
running=True
playing = False
while running == True:
    event, values = window.read()
    if event == "Switch to true or false":
        window["-FOUR_QUESTION-"].update(visible=False)
    elif event == answers[0]:
        if answers[0] == question["answer"]:
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
        if answers[3] == question["answer"]:
            window["-FOUR_QUESTION-"].update("Correct.")
            correct_awnsers+=1
            was_last_awnser_correct=True
        else:
            window["-FOUR_QUESTION-"].update("incorrect.")
            was_last_awnser_correct=False
    if event == sg.WIN_CLOSED:
        break


########################################################################################################################################################################################################
    if event == "Play Quiz":
        # Update the text when button is clicked
        window["-FOUR_QUESTION-"].update("This should make it play.")
        for question in questions.items:
            if was_last_awnser_correct==True:
                iterate=iterate+1
            else:
                pass
    elif event == "Score":
        window["-FOUR_QUESTION-"].update("This should show your score.")
    elif event == "leave":
        window["-FOUR_QUESTION-"].update("this should make you leave.")

##    correct_anwsers = 0
##    wrong_awnsers = 0

    while playing == True:
        pass
