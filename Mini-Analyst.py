logs = [
    {"ip": "10.0.0.1", "status": "fail", "porta": 22, "usuario": "admin"},
    {"ip": "10.0.0.1", "status": "fail", "porta": 22, "usuario": "joao"},
    {"ip": "10.0.0.1", "status": "fail", "porta": 80, "usuario": "maria"},
    {"ip": "10.0.0.1", "status": "ok", "porta": 443, "usuario": "admin"},
    {"ip": "10.0.0.2", "status": "fail", "porta": 22, "usuario": "ana"},
    {"ip": "10.0.0.2", "status": "ok", "porta": 22, "usuario": "ana"},
    {"ip": "10.0.0.3", "status": "ok", "porta": 21, "usuario": "carlos"},
]

portscan = {}
bruteforce = {}
users = {}

for log in logs:

    ip = log["ip"]
    status = log["status"]
    porta = log["porta"]
    usuario = log["usuario"]

    
    if status == "fail":
        bruteforce[ip] = bruteforce.get(ip, 0) + 1
    else:
        bruteforce[ip] = 0


    for ip, quantidade in bruteforce.items():
        if quantidade >= 3:
            print(f"🚨 Possível brute force: {ip}")

    portscan.setdefault(ip, set()).add(porta)


    users.setdefault(ip, set()).add(usuario)
    

for ip, portas in portscan.items():
    if len(portas) >= 3:
        print(f"⚠️ Possível port scan: {ip}")

for ip, usuarios in users.items():
    if len(usuarios) >= 3:
        print(f"⚠️ Possível enumeração de usuários: {ip}")