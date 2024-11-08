from chatbot import nem

nome = input("quem é você?")
while True:
    texto = nem.receber_textos
    resposta =  nem.buscar_respostas(nome, texto)
    if nem.exibir_msg(resposta, nome) == "Sai daqui":
        break 