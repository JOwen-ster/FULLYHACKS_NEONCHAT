import socket
import threading

# Server setup
def run_server():
    def handle_client(client):
        try:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                print(f"msg from {contacts[addr]}: {data.decode('utf-8')}")
        except OSError as e:
            pass
        finally:
            client.close()
    
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server.bind(("f0:57:a6:fc:f2:14", 4))
    server.listen(1)

    print("Waiting for a connection...")

    # Accept a client connection
    client, addr = server.accept()
    contacts = {}
    contacts[addr] = "owen"
    print(f"Accepted connection from {contacts[addr]}")

    # Start a thread to handle incoming messages
    receive_thread = threading.Thread(target=handle_client, args=(client,), daemon=True)
    receive_thread.start()

    try:
        while True:
            # Main thread for sending messages
            message = input()
            client.send(message.encode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        client.close()
        server.close()