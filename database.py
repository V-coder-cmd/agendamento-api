import sqlite3

def conectar():
    conexao = sqlite3.connect("agendamentos.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            data TEXTE NOT NULL,
            horario TEXT NOT NULL
            )
        """)
    conexao.commit()
    conexao.close()