import os

os.system('cls')
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector não instalado!')
else:
    print('MySql Connector instalado e pronto!')