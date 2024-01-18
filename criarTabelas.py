from configuracao  import con
from sqlite3 import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXIST contatos ( nome VARCHAR(50), tel VARCHAR(10))
"""

tabela_emails = """
    CREATE TABLE IF NOT EXIST emails(
    dono VARCHAR(50)
    )
"""

with con() as c:
    try:
        cursor = c.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')