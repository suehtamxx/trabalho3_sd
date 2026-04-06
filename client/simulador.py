import requests
import uuid
import random
import datetime

def gerar_e_enviar_leitura():

    temp_sorteada = random.randint(-10, 40)
    id_leitura = str(uuid.uuid4())
    
    dados_simulados = {
        'id': id_leitura,
        'sensor_id': f'Sensor_{random.randint(1, 10)}',
        'temperatura': temp_sorteada,
        'timestamp': datetime.datetime.now().isoformat()
    }

    try:
        resposta = requests.post('http://localhost:5000/api/data', json=dados_simulados)
        dados_resposta = resposta.json()

        status_recebido = dados_resposta.get('status', 'Desconhecido')
        return True, temp_sorteada, status_recebido, id_leitura
        
    except requests.exceptions.RequestException:
        return False, temp_sorteada, "Erro de Conexão", id_leitura