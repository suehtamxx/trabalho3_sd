from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from server.regras_negocio import processar_dados
import json
from database.db_manager import engine, Leituras


app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    session = Session(engine)
    data = request.get_json()

    try:
        # consulta ao banco para saber se o id ja existe na tabela
        result = session.query(Leituras).filter_by(id=data['id']).first()

        # primeiro verifico se o id ja existe no banco
        # se existir, retorno uma mensagem dizendo que os dados ja existem
        if result:
            return jsonify({'message': 'Data already exists', 'status': result.status_logico}), 200
        
        # se nao existr, processa os dados e insere no banco de dados, depois fecha a conexao
        else:
            data_process = processar_dados(data)
            
            nova_leitura = Leituras(
                id=data['id'],
                sensor_id=data['sensor_id'],
                temperatura=data['temperatura'],
                status_logico=data_process['status_logico'],
                timestamp=data['timestamp']
            )
            session.add(nova_leitura)
            session.commit()

            # escrever os dados em um arquivo json
            with open('log_sensores.json', 'a') as f:
                # transformo de dicionario para json e escrevo no arquivo
                linha_json = json.dumps(data_process)
                f.write(linha_json + '\n')

            return jsonify({'message': 'Data inserted successfully', 'status': data_process['status_logico']}), 201
    except Exception as e:
        # se der algum erro no banco, damos um rollback para desfazer quaisquer operaçoes pendentes
        session.rollback()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    
    finally:
        session.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
