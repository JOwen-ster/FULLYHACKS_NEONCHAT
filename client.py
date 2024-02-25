import tkinter as tk
from threading import Thread
import socket
import subprocess

class BluetoothClient:
    def __init__(self, host, port, gui):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.gui = gui
        self.connected = False
        

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")
            self.connected = True
            self.receive_data()
        except Exception as e:
            print(f"Connection error: {e}")
            self.connected = False

    def send_data(self, data):
        try:
            self.client_socket.send(data.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")

    def receive_data(self):
        while self.connected:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.gui.update_received_data(data.decode('utf-8'))
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
    
    def is_socket_connected(self):
        try:
            peer_address = self.client_socket.getpeername()
        except socket.error:
            self.connected = False
            self.client_socket.close()

class BluetoothGUI:
    def __init__(self, master, client):
        self.master = master
        master.title("Bluetooth Tkinter GUI")
        master.geometry('400x300')
        master.config(bg='black')

        self.client = client

        self.label = tk.Label(master, text="Enter text to send:")
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send via Bluetooth", command=self.send_data)
        self.send_button.pack(padx=10, pady=10)

        self.received_data_label = tk.Label(master, text="Received data will appear here:")
        self.received_data_label.pack(padx=10, pady=10)

        self.connect_button = tk.Button(master, text="Connect to Server", command=self.connect_to_server)
        self.connect_button.pack(padx=10, pady=10)

    def connect_to_server(self):
        # Move connection logic to a separate thread
        connection_thread = Thread(target=self.client.connect)
        connection_thread.start()
        dc = Thread(target=self.is_socket_connected)
        dc.start()



    def send_data(self):
        if self.client.connected:
            data_to_send = self.entry.get()
            self.client.send_data(data_to_send)

    def update_received_data(self, data):
        self.received_data_label.config(text=f"Received data: {data}")

# def ask(root):
#     result = None
#     asklabel = tk.Label(root, text="Enter host MAC Address:")
#     asklabel.pack()

#     askentry = tk.Entry(root)
#     askentry.pack()

#     def send_address():
#         result = askentry.get()
#     asksend = tk.Button(root, text="Send via Bluetooth", command=send_address)
#     asksend.pack()
#     return result


def main(ask='00:00:00:00:00:00'):
    # Replace '00:00:00:00:00:00' with the Bluetooth address of the server device
    server_bluetooth_address = '5c:fb:3a:53:e8:3e'
    server_port = 4

    server = BluetoothClient(server_bluetooth_address, server_port, None)  # Pass None for now

    root = tk.Tk()
    app = BluetoothGUI(root, server)
    server.gui = app  # Assign the GUI instance to the client
    root.mainloop()


if __name__ == "__main__":
    main()
