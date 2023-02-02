import PySimpleGUI as sg
import os, imaplib

sg.theme('DarkTeal9')


def backup(server, email, senha, dest ):
        
    try:
        os.mkdir(f'{dest}/Inbox')
    except: pass

    EMAIL_FOLDER = "Inbox"
    IMAP_SERVER = server
    EMAIL_ACCOUNT = email
    PASSWORD = senha
    OUTPUT_DIRECTORY = f'{dest}/Inbox'
    
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print ("Processing mailbox: ", EMAIL_FOLDER)
        
        rv, data = M.search(None, "ALL")
        if rv != 'OK':
            print ("No messages found!")
            return

        for num in data[0].split():
            rv, data = M.fetch(num, '(RFC822)')
            if rv != 'OK':
                print ("ERROR getting message", num)
                return
            print ("Writing message ", num)

            f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
            f.write(data[0][1])
            f.close()
        M.close()
    else:
        print ("ERROR: Unable to open mailbox ", rv)
    M.logout()


    



def vpath(email):
    base = r'C:/Temp'
    try:
        lista = os.listdir(base)
        #   print('pasta existe')
    except:
        os.mkdir(r'C:/Temp')
        #   print('pasta criada, pois nao existia')
    
    nome = email.split('@')
    pasta_backup = nome[1]
    
    if pasta_backup in lista:
        pass
        #   print("arquivo já existe na base")
    else:
        os.mkdir(f"{base}/{pasta_backup}")
        #   print("arquivo nao existe na base, criado agora!")

    final_dir = f"{base}/{pasta_backup}"
    return final_dir


def novalinha(contador):
    row = [
        sg.pin(
            sg.Column([
                [
                    sg.Input(size=(30,1), key=("EMAIL", contador)),      
                ]
            ],
            key = ("LINHA", contador)
            )
        )
    ]
    return row[:]

layout = [
    [sg.Text("Servidor"),sg.Input("", size=(20,1), pad=(0,0), justification="c", key="BACKUPSERVER")],
    [sg.Text("Emails", size=(30,1), pad=(0,0), justification="c")],
    
    [sg.Column([],key='LISTA')],
    
    [sg.Button("+", border_width=1, pad=(0,0), size=(4,1),focus=False,
    button_color=(sg.theme_text_color(), sg.theme_background_color()), key=("ADD"), ), sg.Button('Arquivar Emails', border_width=1, button_color=(sg.theme_text_color(), sg.theme_background_color()))],
    
    
]
window = sg.Window("Download Emails", layout, use_default_focus=False, element_justification="C", text_justification="c", resizable=True,transparent_color=True, font='Courier 10 bold')

contador = 0

while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, "EXIT"):
        print(senha, contador)
        break
    if event == "ADD" and contador < 17:
        window.extend_layout(window["LISTA"], [novalinha(contador)])
        contador+=1
    if event == 'Arquivar Emails':
        #   acessar os emails dos inputs => values[('EMAIL',0)]
        senha = sg.PopupGetText('Senha:', title='Password', password_char='*')
        for c in range(0, contador):
            vpath(values[('EMAIL',c)])
    if event == "ADD" and contador == 17:
        sg.PopupNoTitlebar("Limite maximo de arquivamento simultaneo atingido, após a conclusão destes será possivel adicionar outros Emails. ", font='Helvetica 10 italic bold')
        

window.close()