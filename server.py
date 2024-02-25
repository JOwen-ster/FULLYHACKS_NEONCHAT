import tkinter as tk
from threading import Thread
import socket
import sys

col = '#260033'
class BluetoothServer:
    def __init__(self, host, port, gui):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(3)
        self.gui = gui

    def start(self):
        print("Server listening for incoming connections...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            self.clients.append(client_socket)
            client_thread = Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Update GUI with received data
                self.gui.update_received_data(data.decode('utf-8'))
            except Exception as e:
                print(f"Error handling client: {e}")
                break

class BluetoothGUI:
    def __init__(self, master, server):
        self.master = master
        master.title("NeonChat - Hosted")
        master.iconphoto(True, tk.PhotoImage(file = r"images/favicon.ico"))
        master.geometry('400x300')
        master.config(bg=col)

        self.server = server

        self.label = tk.Label(master, text="Enter text to send:", bg=col, fg='white')
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send via Bluetooth", command=self.send_data, bg=col, fg='lightblue')
        self.send_button.pack(padx=10, pady=10)

        self.received_data_label = tk.Label(master, text="Received data will appear here:", bg=col, fg='white')
        self.received_data_label.pack(padx=10, pady=10)

        # self.connect_button = tk.Button(master, text="Stop Searching", command=self.connect_to_server, bg=col, fg='magenta')
        # self.connect_button.pack(padx=10, pady=10)

    def send_data(self):
        data_to_send = self.entry.get()
        for client in self.server.clients:
            try:
                client.send(data_to_send.encode('utf-8'))
            except Exception as e:
                print(f"Error sending data: {e}")

    def update_received_data(self, data):
        self.received_data_label.config(text=f"Received data: {data}")

if __name__ == "__main__":
    server_bluetooth_address = sys.argv[1]
    server = BluetoothServer(server_bluetooth_address, 4, None)  # Pass None for now

    server_thread = Thread(target=server.start)
    server_thread.start()

    root = tk.Tk()
    app = BluetoothGUI(root, server)
    server.gui = app  # Assign the GUI instance to the server
    root.mainloop()