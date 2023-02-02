import PySimpleGUI as sg

sg.theme('DarkTeal9')


def novalinha(contador):
    row = [
        sg.pin(
            sg.Colunm([
                [
                    sg.Button("X", border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key=("DEL", contador)),
                    sg.Input(size=(30,1), key=("EMAIL", contador)),
                ]
            ],
            key = ("LINHA", contador)
            )
        )
    ]
    return row[:]

layout = [
    [sg.Text("Emails", size=(30,1), pad=(0,0), justification="c")],
    
    [sg.Column([],key='LISTA')],
    
    [sg.Button("+", border_width=1, pad=(0,0), size=(4,1),focus=False , button_color=(sg.theme_text_color(), sg.theme_background_color()), key=("ADD")), sg.Button('Arquivar Emails', border_width=1, button_color=(sg.theme_text_color(), sg.theme_background_color()))],
    
    
]

window = sg.Window("Tela de download", layout, use_default_focus=False, element_padding=(2,0), element_justification="c", text_justification="c",  )

c = 0

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "EXIT"):
        break
    if event == "+":
        c += 1
        window.extend_layout(window['LISTA'], [novalinha(c)])
    print(event, values, c)
window.close()