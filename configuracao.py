import sqlite3, os

def con():
    os.system('cls')

    conexao = sqlite3.connect('agenda.db')
    if conexao == True:
        print('Conectado')
        
    cursor = conexao.cursor()

    return conexao

if __name__== '__main__':

    c = con()

