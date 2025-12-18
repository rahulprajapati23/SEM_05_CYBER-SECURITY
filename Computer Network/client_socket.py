import socket
import datetime

# RAHUL_PRAJAPATI_23162171020
print("----------------------------------")
print("      Starting client...")
print("----------------------------------")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8000))

print("Connected to server. You can start communication...")

# RAHUL_PRAJAPATI_23162171020
while True:
    client_msg = input("Client (Enter Message): ")
    s.send(client_msg.encode())

    if client_msg.lower() == "quit":
        print("Client: Connection closed.")
        break

    server_msg = s.recv(1024).decode()

    if server_msg.lower() == "quit":
        print("Client: Server is not able to respond, please try again later.")
        break

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Server [{current_time}]: {server_msg}")

    if server_msg.lower() == "quit":
        print("Client: Connection terminated by server.")
        break

# RAHUL_PRAJAPATI_23162171020
s.close()
print("Connection closed.")