def processar_dados(dados):
    if dados['temperatura'] >= 15:
        dados['status_logico'] = 'Critico'
    elif dados['temperatura'] >= 10:
        dados['status_logico'] = 'Alerta'
    elif dados['temperatura'] >= -10 and dados['temperatura'] < 10:
        dados['status_logico'] = 'Normal'
    else:
        dados['status_logico'] = 'Invalido'
    return dados