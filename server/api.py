from flask import Flask, jsonify, request
from sqlite3 import connect
from regras_negocio import processar_dados
import json
app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():

    connection = connect('simulador.db')
    cursor = connection.cursor()

    data = request.get_json()

    # consulta ao banco para saber se o id ja existe na tabela
    cursor.execute("select * from leituras where id = ?", (data['id'],))
    result = cursor.fetchone()

    # primeiro verifico se o id ja existe no banco
    # se existir, retorno uma mensagem dizendo que os dados ja existem
    if result:
        connection.close()
        return jsonify({'message': 'Data already exists'}), 200
    
    # se nao existr, processa os dados e insere no banco de dados, depois fecha a conexao
    else:
        data_process = processar_dados(data)
        cursor.execute("insert into leituras (id, sensor_id, temperatura, status_logico, timestamp) values (?, ?, ?, ?, ?)",
                       (data['id'], data['sensor_id'], data['temperatura'], data_process['status_logico'], data['timestamp']))
        connection.commit()
        connection.close()

        # escrever os dados em um arquivo json
        with open('data.json', 'a') as f:
            # transformo de dicionario para json e escrevo no arquivo
            linha_json = json.dumps(data_process)
            f.write(linha_json + '\n')
        return jsonify({'message': 'Data inserted successfully', 'status': data_process['status_logico']}), 201

