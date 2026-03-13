import json

logs = None

with open("logs.json") as file:
    logs = json.load(file)


def analisar_logs(logs):
    try:

        alerta = []
        bruteforce = {}
        portscan = {}
        usuarios = {}

        for x in logs:
            ip = x["ip"]
            status = x["status"]
            porta = x["porta"]
            user = x["usuario"]


            if status == "fail":
                bruteforce[ip] = bruteforce.get(ip, 0) + 1
            else:
                bruteforce[ip] = 0


            portscan.setdefault(ip, set()).add(porta)


            usuarios.setdefault(ip, set()).add(user)


        for ip, quantidade in bruteforce.items():
            if quantidade >= 3:
                alerta.append(f"Possível BruteForce: {ip}")


        for ip, portas in portscan.items():
            if len(portas) >= 3:
                alerta.append(f"Possível PortScan: {ip}")


        for ip, users in usuarios.items():
            if len(users) >= 3:
                alerta.append(f"Possível Enumeração de Usuários: {ip}")


        with open("Alertas.txt", "a") as file:
            for x in alerta:
                print(x)
                file.write(x + "\n")

    except ValueError:
        print("Erro ao processar logs")


analisar_logs(logs)