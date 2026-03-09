import FreeSimpleGUI as sg
layout = [ 
[sg.Button("Play Quiz", font=("calibri",25, "bold"))],
[sg.Text("", key="-OUTPUT-")],
[sg.Button("See how many questions you have left", font=("calibri",20, "bold"))],
[sg.Text("", key="-OUTPUT-")],
[sg.Button("leave", font=("calibri",2, "bold"))],
[sg.Text("", key="-OUTPUT-")]
] 
window = sg.Window("Quiz", layout)
running=True
playing = False
while running == True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Click Me!":
        # Update the text when button is clicked
        window["-OUTPUT-"].update("Button was clicked!")

##    correct_anwsers = 0
##    wrong_awnsers = 0
##    layout = [ 
##    [sg.text("Question Text", font=("calibri",20, "white", "bold"))],
##    [sg.text("Anwser 1 Text", font=("calibri",20,"#8742FA"))],
##    [sg.text("Anwser 2 Text", font=("calibri",20,"#FA4259"))],
##    [sg.text("Anwser 3 Text", font=("calibri",20,"#B5FA42"))],
##    [sg.text("Anwser 4 Text", font=("calibri",20,"#42FAE3"))]
##    ] 
    while playing == True:
        pass
