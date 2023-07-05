import socket

saldo = input("Digite o saldo: ")
seletor = input("Digite o produto. Opções: 1 = chopp R$ 10.00. 2 = cachorro quente R$ 8.00")

# Configurações do servidor: IP e Porta
if seletor == "1":
    print("Você escolheu o chopp")
    server_ip = 'SERVIDOR CHOPP'
elif seletor == "2":
    print("Você escolheu o cachorro quente")
    server_ip = 'SERVIDOR DOGÃO'
else:
    print("Opção inválida.")
    exit()

server_port = 12345

# Código de cupom (opcional)
cupom = input("Digite o código de cupom (ou deixe em branco): ")

# Valor da transação e valor do produto
valores = f"{saldo},{cupom}"

# Criação do socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectando ao servidor
    client_socket.connect((server_ip, server_port))
    print("Conectado ao servidor.")

    # Envio do valor da transação, valor do produto e código de cupom
    client_socket.send(valores.encode())

    # Recebimento da resposta do servidor
    resposta = client_socket.recv(1024).decode()
    print("Resposta do servidor: ", resposta)

finally:
    client_socket.close()
    print("Conexão encerrada.")