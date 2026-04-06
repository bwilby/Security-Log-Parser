#LogParser.py


failed_logins = {}
fails = 0
with open("auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            username = parts[8]
            ip = parts[10]
            fails +=1
            if ip not in failed_logins:
                failed_logins[ip] = {"count": 0, "usernames": []}
            
            failed_logins[ip]["count"] += 1
            failed_logins[ip]["usernames"].append(username)

print("=== Failed Login Report ===")
for ip, data in failed_logins.items():
    print(f"IP: {ip} | Attempts: {data['count']} | Usernames tried: {set(data['usernames'])}")

print ("\n=== Brute Force Alerts ===")
for ip, data in failed_logins.items():
    if data["count"] > 2:
        print(f"ALERT: Possible brute force from {ip} - {data['count']} attempts")

print("Total Failed login attempts:", fails)