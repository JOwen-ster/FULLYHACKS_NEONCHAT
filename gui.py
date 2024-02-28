import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import subprocess
from tkinter import simpledialog
from PIL import Image, ImageTk
import server
import client
import socket

root = tk.Tk()
root.iconphoto(True, tk.PhotoImage(file = r"images/favicon.ico"))

root.geometry('500x500')
root.title('Neon Chat')
root.config(bg='black')

image = Image.open("images/neonchattitle492x96.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack(padx=20, pady=20)

ipa = tk.Label(root, text = "Enter Address:", bg='black', fg='white')
ipa.pack(padx=10, pady=10)
textbox = tk.Text(root, height=1, font=('Arial', 12))
textbox.pack(padx=170, pady=10)

def runClient():
    maca = textbox.get('1.0', tk.END).strip()
    # try:
    #     testsocket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    #     testsocket.bind((maca, 4))
    #     testsocket.close()
    root.destroy()
    subprocess.run(['python', 'client.py', maca])
    # except:
    #     messagebox.showerror("Error", "Invalid MAC Address")
    #     testsocket.close()
    #     return


def runServer():
    maca = textbox.get('1.0', tk.END).strip()
    try:
        testsocket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        testsocket.bind((maca, 4))
        testsocket.close()
        root.destroy()
        subprocess.run(['python', 'server.py', maca])
    except:
        messagebox.showerror("Error", "Invalid MAC Address")
        testsocket.close()
        return

imgHost = tk.PhotoImage(file = r"images/neonbuttonhost200x68.png")
tk.Button(root, image = imgHost, command=runServer).pack(side=tk.LEFT, padx=30)
imgJoin = tk.PhotoImage(file = r"images/neonbuttonjoin200x68.png")
tk.Button(root, image = imgJoin, command=runClient).pack(side=tk.RIGHT, padx=30)

root.mainloop()
#end