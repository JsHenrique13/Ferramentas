import os
email = 'teste@assesi.com'

def vpath(email):
    base = r'C:/Temp'
    try:
        lista = os.listdir(base)
        print('pasta existe')
    except:
        os.mkdir(r'C:/Temp')
        print('pasta criada, pois nao existia')
    
    nome = email.split('@')
    pasta_backup = nome[1]
    
    if pasta_backup in lista:
        print("arquivo já existe na base")
    else:
        os.mkdir(f"{base}/{pasta_backup}")
        print("arquivo nao existe na base, criado agora!")

    final_dir = f"{base}/{pasta_backup}"
    return final_dir
path = vpath(email)
print(path)