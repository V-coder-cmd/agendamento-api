from flask import Flask, request, jsonify
import models
from database import criar_tabela
from database import conectar
from email_service import enviar_confirmacao, enviar_cancelamento, enviar_atualizacao


app = Flask(__name__)

criar_tabela()

agendamentos = []

@app.route("/agendar", methods = ["POST"])
def agendar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")
    data = dados.get("data")
    horario = dados.get("horario")

    if not all([nome, email, data, horario]):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    agendameto = {
        "nome": nome,
        "email": email,
        "data": data,
        "horario": horario
    }

    agendamentos.append(agendameto)
    
    enviar_confirmacao(nome, email, data, horario)
    models.criar_agendamento(nome, email, data, horario)

    return jsonify({"status": "Agendamento criado e e-mail enviado com sucesso"}), 201


@app.route("/agendamentos/<int:id>", methods = ["DELETE"])
def deletar_agendamento(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, email, data, horario FROM agendamentos WHERE id = ?", (id,))
    agendamento = cursor.fetchone()

    if not agendamento:
        conexao.close()
        return {"erro": "Agendamento não encontrado"}, 400
    
    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

    enviar_cancelamento(
        agendamento["nome"],
        agendamento["email"],
        agendamento["data"],
        agendamento["horario"]
    )

    return {"status": "Agendamento removido com sucesso"}, 200


@app.route("/agendamentos", methods = ["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM agendamentos")
    registros = cursor.fetchall()

    conexao.close()

    agendamentos = [dict(registro) for registro in registros]
    return jsonify(agendamentos)


@app.route("/agendamentos/<int:id>", methods = ["PUT"])
def atualizar_agendamento(id):
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, email, data, horario FROM agendamentos WHERE id = ?", (id,))
    agendamento = cursor.fetchone()

    if not agendamento:
        conexao.close()
        return {"erro":"Agendamento não encontrado"}, 404


    dados = request.get_json(force=True)

    if not dados or "data" not in dados or "horario" not in dados:
        return jsonify({"erro": "Data e horário são obrigatórios"}), 400

    cursor.execute(
        "UPDATE agendamentos SET data = ?, horario = ? WHERE id = ?",
        (dados["data"], dados["horario"], id)
    )
    conexao.commit()

    try:

        enviar_atualizacao(
            agendamento["nome"],
            agendamento["email"],
            dados["data"],
            dados["horario"]
        )
    except Exception as e:
        print ("Erro ao enviar e-mail: ", e)

    return {
            "status": "Agendamento atualizado e e-mail enviado com sucesso",
            "antes":{
                "data": agendamento["data"],
                "horario": agendamento["horario"]
            },
            "depois":{
                "data": dados["data"],
                "horario": dados["horario"]
            }
            
    }, 200

if __name__ == "__main__":
    app.run(debug=True)