# Autor: https://www.instagram.com/jhonn.souzaa/
# GitHub: https://github.com/Jhonatann001

import socket

# ANSI Cores
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Dicionário de portas e serviços conhecidos
SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt",
    # Adicione mais portas e serviços conforme necessário
}

def display_portscan():
    # Texto estilizado
    portscan_art = """


    🚪  🔍  🔒   🔑   🛠️    🚨   🚪    🔍   🛠️         
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |  P  |  O  |  R  |  T  |  S  |  C  |  A  |  N  |
    +-----+-----+-----+-----+-----+-----+-----+-----+
    
    Autor 👨‍💻
    https://github.com/Jhonatann001               
    https://www.instagram.com/jhonn.souzaa/       
    
                                   
    """
    print(f'{RED}{portscan_art}{RESET}')

# Executa a função para exibir o desenho
display_portscan()

LHOST = input('Digite o endereço IP ex: 192.168.0.1: ')
start_port = int(input('Digite a porta inicial (padrão: 1): ') or 1)
end_port = int(input('Digite a porta final (padrão: 1024): ') or 1024)

print(f'{GREEN}Buscando portas abertas de {start_port} a {end_port}...{RESET}')

# Lista para armazenar os resultados
results = []

for PORT in range(start_port, end_port + 1):  # Intervalo de portas personalizado
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Timeout para evitar espera longa
    result = s.connect_ex((LHOST, PORT))
    if result == 0:
        service = SERVICES.get(PORT, "Serviço desconhecido")  # Obtém o serviço da porta
        message = f'{PORT} OPEN / ABERTA - {service}'
        print(f'{GREEN}{message}{RESET}')  # Exibe a porta e o serviço no terminal
        results.append(message)  # Adiciona o resultado à lista
    else:
        message = f'{PORT} CLOSED / FECHADA'
        print(f'{RED}{message}{RESET}')
        results.append(message)  # Adiciona o resultado à lista
    s.close()

# Salva os resultados em um arquivo
with open('resultados.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')

print(f'{GREEN}Resultados salvos em "resultados.txt"{RESET}')