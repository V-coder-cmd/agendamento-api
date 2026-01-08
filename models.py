from database import conectar

def criar_agendamento(nome, email, data, horario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO agendamentos (nome, email, data, horario)
        VALUES(?, ?, ?, ?)
    """, (nome, email, data, horario))

    conexao.commit()
    conexao.close()

def listar_agendamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM agendamentos")
    resultados = cursor.fetchall()

    conexao.close()
    return resultados
