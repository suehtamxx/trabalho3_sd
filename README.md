# Sistema Cliente/Servidor em Três Camadas (Sensor de Temperatura)

**Curso:** Sistemas de Informação - Universidade Federal do Piauí (UFPI)  

## Objetivo
Este projeto implementa um sistema cliente/servidor em três camadas capaz de enviar, processar e armazenar dados de sensores de temperatura de forma organizada e resiliente. O foco principal é demonstrar a comunicação HTTP, a transparência de distribuição e a garantia de idempotência nas requisições.

## Arquitetura do Sistema

O projeto foi dividido em três camadas lógicas e físicas:

1. **Cliente (Simulador Tkinter):** - Interface gráfica desenvolvida em Tkinter.
   - Gera dados simulados de temperatura (-10°C a 40°C).
   - Envia a leitura via HTTP (POST) para o servidor em formato JSON.
   - Gera um UUID único por requisição para garantir a idempotência.
   - Exibe em tempo real o status retornado pelo servidor e o histórico de envios.

2. **Servidor (Regras de Negócio e API):**
   - API construída com Flask.
   - **Filtro de Idempotência:** Verifica se o UUID recebido já existe no banco de dados para evitar duplicidade em caso de reenvio por falhas de rede.
   - **Processamento Lógico:** Avalia a temperatura recebida e classifica o status como Normal, Alerta (>10°C) ou Crítico (>15°C).
   - Salva um log das requisições em um arquivo `.json` no disco.

3. **Banco de Dados:**
   - Utiliza SQLite com mapeamento objeto-relacional (ORM) via SQLAlchemy.
   - Armazena os metadados na tabela `leituras` (id, sensor_id, temperatura, status_logico, timestamp).

## Instruções de Execução

O sistema foi desenhado para rodar em computadores distintos, mas pode ser executado localmente para testes.

### Pré-requisitos
Certifique-se de ter o Python 3 instalado. Instale as dependências do projeto executando o comando abaixo na raiz do repositório:
```bash
pip install -r requirements.txt
```
## Para rodar o sistema em duas máquinas ou mais, uma máquina vai executar o comando do banco de dados e em seguida o comando do servidor. A outra máquina precisa rodar apenas o comando do cliente (e o servidor precisa estar no ar).

## Banco de Dados
Primeiro é preciso inicializar o Banco de Dados. Execute este comando abaixo:
```bash
python3 database/db_manager.py
```

## Servidor
O próximo passo é inciar o Servidor para receber as requisições. Execute este comando abaixo:
```bash
python3 -m server.api
```

## Cliente
O último passo é iniciar o Cliente. Execute este comando abaixo:
```bash
python3 client/app.py
```
Clique em "Gerar e Enviar Leitura" para enviar uma requisição para o servidor.apa

