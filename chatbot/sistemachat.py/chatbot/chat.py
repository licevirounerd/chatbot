import nem as pc 
nome_maquina = "chat"
pc.saudacoes_GUI(nome_maquina)
while True:
    texto = pc.receber_textos()
    resposta = pc.buscar_respostas("Cliente: " +texto+"\n")
    if pc.exibir_msg_GUI(texto, resposta, nome_maquina) == "fim":
        break