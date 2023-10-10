import sqlite3

def validarLogin(usuario: str,senha: str):
    login_validation = False
    with sqlite3.Connection(r'assets\bancoDaora.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(f'select * from usuarios where usuario = "{usuario}" and senha = "{senha}"')
        consulta = cursor.fetchall()
        if len(consulta) == 1:
            login_validation = True
        cursor.close()
        return login_validation