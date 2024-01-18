import sqlite3, os

os.system('cls')

conexao = sqlite3.connect('agenda.db')
print(conexao)
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS agenda (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT)')