import socket # Biblioteca para conexões de rede

def scan_ports(ip, ports):
    print(f"Iniciando varredura no IP: {ip}\n")
    for port in ports:
        # Cria um objeto de socket (familia IPv4, protocolo TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Tempo máximo de espera (0.5 segundos)

        # Tenta conectar na porta. Retorna 0 se tiver sucesso.
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Porta {port}: ABERTA")
        else:
            print(f"[-] Porta {port}: FECHADA")

        s.close() # FEcha a conexão

# Configuracão de teste
alvo = "127.0.0.1" # Testa na propria maquina (localhost)
portas_para_testar = [21, 22, 80, 443, 3306]

scan_ports(alvo, portas_para_testar)