from tkinter import Tk, Label, Button, Listbox, END
from simulador import gerar_e_enviar_leitura

def acionar_envio():
    sucesso, temp_sorteada, status_recebido, id_leitura = gerar_e_enviar_leitura()
    
    label_temp_valor.config(text=f"{temp_sorteada} °C")
    label_status_valor.config(text=status_recebido)
    
    if status_recebido == 'Normal':
        label_status_valor.config(fg="green")
    elif status_recebido == 'Alerta':
        label_status_valor.config(fg="orange")
    elif status_recebido == 'Critico' or status_recebido == 'Erro de Conexão':
        label_status_valor.config(fg="red")
    
    texto_historico = f"Temp: {temp_sorteada}°C | Status: {status_recebido} | ID: {id_leitura[:8]}..."
    listbox_historico.insert(END, texto_historico)



janela = Tk()
janela.title("Simulador de Sensor Cliente")
janela.geometry("450x450")

Label(janela, text="Temperatura Enviada:", font=("Arial", 12)).pack(pady=(20, 0))
label_temp_valor = Label(janela, text="-- °C", font=("Arial", 24, "bold"))
label_temp_valor.pack()

Label(janela, text="Status Retornado pelo Servidor:", font=("Arial", 12)).pack(pady=(10, 0))
label_status_valor = Label(janela, text="--", font=("Arial", 16, "bold"))
label_status_valor.pack()

botao_enviar = Button(janela, text="Gerar e Enviar Leitura", font=("Arial", 12), command=acionar_envio)
botao_enviar.pack(pady=20)

Label(janela, text="Histórico Local de Envios:", font=("Arial", 10)).pack()
listbox_historico = Listbox(janela, width=55, height=10)
listbox_historico.pack(pady=5)

janela.mainloop()