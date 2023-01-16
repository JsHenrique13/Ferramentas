import PySimpleGUI as sg
import qrcode
import os
# só funciona com o => pip install qrcode==6.1

layout = [
    [sg.Image(size=(300,300), key="IMG")],
    [sg.InputText(size=(30,1), key="LINK", justification="c")],
    [sg.Button("Gerar QR Code")],
]


window = sg.Window("Qr Code Generator", layout, element_justification="c")


def gera_qr(data):
    qr= qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    filename = "qr_code"+".png"
    path = os.path.join(os.getcwd(), filename)
    print(path)
    img.save(path)
    return path


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "Gerar QR Code":
        link = values["LINK"]
        QRimg = gera_qr(link)
        window["IMG"].update(filename = QRimg)


window.close()    