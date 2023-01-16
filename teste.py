import PySimpleGUI as sg


def novalinha(contador, numero_linha):
    row = [
        sg.pin(
            sg.Column([
                [
                    sg.Button("X", border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key=("DEL", contador)),
                    sg.Input(size=(25,1), key=("VALOR", contador)),
                    sg.Text(f'Linha {numero_linha}', key = ("LINHA_N", contador))
                ]
            ],
            key = ("LINHA", contador)
            )
        )
    ]
    return row[:]

layout = [
    [sg.Text("Gerenciador de Demandas")],
    [sg.Column([],key="PAINEL")],
    [sg.Text("Exit", enable_events=True, key="EXIT"),
    sg.Text("+", enable_events=True, key = "ADD_LINHA")]
]

window = sg.Window("Demandas da Web", layout, use_default_focus=False, font=15, element_justification="C", text_justification="c")

contador = 0
numero_linha = 1 

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "EXIT"):
        break
    if event == "ADD_LINHA":
        window.extend_layout(window["PAINEL"], [novalinha(contador, numero_linha)])
        contador+=1
        numero_linha+=1
    elif event[0] == "DEL":
        numero_linha-=1
        window[("LINHA", event[1])].update(visible=False) 
window.close()