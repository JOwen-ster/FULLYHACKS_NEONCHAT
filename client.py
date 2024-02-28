import tkinter as tk
from threading import Thread
import socket
import sys
import datetime

col = '#00004d'
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

class BluetoothGUI:
    def __init__(self, master, client):
        self.master = master
        master.title("NeonChat - Chatter")
        master.iconphoto(True, tk.PhotoImage(file = r"images/favicon.ico"))
        master.geometry('600x500')
        master.config(bg=col)

        self.client = client

        self.label = tk.Label(master, text="Enter text to send:", bg=col, fg='white')
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send via Bluetooth", command=self.send_data, bg=col, fg='lightblue')
        self.send_button.pack(padx=10, pady=10)

        self.connect_button = tk.Button(master, text="Connect to Host", command=self.connect_to_server, bg=col, fg='magenta')
        self.connect_button.pack(padx=10, pady=10)

        self.received_data_label = tk.Label(master, text="", bg=col, fg='white')
        self.received_data_label.pack(padx=10, pady=10)
    def connect_to_server(self):
        # Move connection logic to a separate thread
        connection_thread = Thread(target=self.client.connect)
        connection_thread.start()



    def send_data(self):
        if self.client.connected:
            data_to_send = self.entry.get()
            self.client.send_data(data_to_send)
            current_text_lines = self.received_data_label.cget("text").split('\n')
            last_10_lines = current_text_lines[:10]
            new_text = "\n".join(last_10_lines)
            self.received_data_label.config(text=(f"YOU[{datetime.datetime.now().strftime('%I:%M %p')}]: " + str(data_to_send) + "\n" + new_text))

    def update_received_data(self, data):
        current_text_lines = self.received_data_label.cget("text").split('\n')
        last_10_lines = current_text_lines[:10]
        new_text = "\n".join(last_10_lines)
        self.received_data_label.config(text=(f"HOST[{datetime.datetime.now().strftime('%I:%M %p')}]: " + str(data) + "\n" + new_text))




def main():
    # Replace '00:00:00:00:00:00' with the Bluetooth address of the server device
    server_bluetooth_address = sys.argv[1]
    server_port = 4

    server = BluetoothClient(server_bluetooth_address, server_port, None)  # Pass None for now

    root = tk.Tk()
    app = BluetoothGUI(root, server)
    server.gui = app  # Assign the GUI instance to the client
    root.mainloop()


if __name__ == "__main__":
    main()
