import socket
import threading


def receive_messages(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"\nMessage: {data.decode('utf-8')}")
    except OSError as e:
        pass
    finally:
        client.close()

# Client setup
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("f0:57:a6:fc:f2:14", 4))

# Start a thread to handle incoming messages
receive_thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
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