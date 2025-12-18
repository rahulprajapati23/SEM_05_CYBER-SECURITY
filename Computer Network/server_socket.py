import socket
import datetime

# RAHUL_PRAJAPATI_23162171020
print("----------------------------------")
print("      Starting server...")
print("----------------------------------")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8000))
s.listen(3)

print("Server is listening on port 8000...")
conn, addr = s.accept()
print("Connected to:", addr)

# RAHUL_PRAJAPATI_23162171020
while True:
    client_msg = conn.recv(1024).decode()

    if client_msg.lower() == "quit":
        print("Server: Connection terminated by client.")
        break

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Client [{current_time}]: {client_msg}")

    server_msg = input("Server (Enter message): ")
    conn.send(server_msg.encode())

    if server_msg.lower() == "quit":
        print("Server: Connection terminated by server.")
        break

# RAHUL_PRAJAPATI_23162171020
conn.close()
s.close()
print("Server closed.")