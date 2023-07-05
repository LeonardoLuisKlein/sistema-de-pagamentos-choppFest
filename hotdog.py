import socket
from datetime import datetime

# Configurações do servidor: IP e Porta
server_ip = 'INSIRA O IP DO SERVIDOR'
server_port = 12345

# Variável para acompanhar o valor total de vendas
valor_total_vendas = 0.0
preco_produto = 8

# Dicionário de códigos de cupom e seus descontos
cupons = {
    "c10": 0.1,  # Desconto de 10%
    "c20": 0.2,  # Desconto de 20%
    # Adicione mais códigos de cupom, se necessário
}

# Criação do socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Vinculação do endereço IP e porta ao socket
    server_socket.bind((server_ip, server_port))

    # Aguardando por conexões
    server_socket.listen(1)
    print("Servidor do hotdog pronto para receber conexões.")

    while True:
        # Aguardando por uma conexão
        # Quando recebe a conexão pega as informações do cliente
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com: ", client_address)
        # Recebimento do valor da transação, valor do produto e código de cupom do cliente
        valores = client_socket.recv(1024).decode().split(",")
        saldo = float(valores[0])
        codigo_cupom = valores[1]
        print("Valor da transação recebido: ", preco_produto)

        # Processamento da transação (simulado)
        if saldo >= preco_produto:
            novo_saldo = saldo - preco_produto
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Verifica se há código de cupom e aplica o desconto correspondente
            if codigo_cupom in cupons:
                desconto = cupons[codigo_cupom]
                valor_desconto = preco_produto * desconto
                preco_produto -= valor_desconto
                resposta = f"Data e Hora: {data_hora}\nNovo saldo: R${novo_saldo}\nValor do produto: R${preco_produto}\nDesconto aplicado: R${valor_desconto}"
            else:
                resposta = f"Data e Hora: {data_hora}\nNovo saldo: R${novo_saldo}\nValor do produto: R${preco_produto}"
                
            # Atualiza o valor total de vendas
            valor_total_vendas += preco_produto
        else:
            resposta = "Pagamento negado: valor do produto é inferior ao valor da transação."

        print(resposta)
        # Envio da resposta ao cliente
        client_socket.send(resposta.encode())

        client_socket.close()
        print("Conexão encerrada com: ", client_address)
        print("Valor total de vendas: ", valor_total_vendas)
finally:
    server_socket.close()