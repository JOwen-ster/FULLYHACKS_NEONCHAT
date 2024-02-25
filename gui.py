import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import client
import subprocess
from tkinter import simpledialog
from PIL import Image, ImageTk
import server

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
    root.destroy()
    subprocess.run(['python', 'client.py', maca])

def runServer():
    maca = textbox.get('1.0', tk.END).strip()
    root.destroy()
    subprocess.run(['python', 'server.py', maca])

imgHost = tk.PhotoImage(file = r"images/neonbuttonhost200x68.png")
tk.Button(root, image = imgHost, command=runServer).pack(side=tk.LEFT, padx=30)
imgJoin = tk.PhotoImage(file = r"images/neonbuttonjoin200x68.png")
tk.Button(root, image = imgJoin, command=runClient).pack(side=tk.RIGHT, padx=30)

# def enter(event):
#     # prints to check key
#     # print(event.state)
#     # print(event.keysym)
#     if event.keysym == "Return":
#         if event.state == 9:
#            msg.delete(tk.END) 
#         elif event.state == 8:
#             get_text()

# def stopText(event):
#     if event:
#         msg.delete(tk.END)

# msg = scrolledtext.ScrolledText(root, height=6, font=('Arial', 12))
# msg.bind("<KeyPress>", stopText)
# msg.pack(padx=10, pady=10)
# textbox = tk.Text(root, height=1, font=('Arial', 12))
# textbox.pack(padx=10, pady=10)
# textbox.bind("<KeyPress>", enter)


# def get_text():
#     new = textbox.get('1.0', tk.END).strip()
#     if not new:
#         return
#     msg.insert(tk.INSERT, new + "\n")
#     textbox.delete(1.0, tk.END)
#     client.send(new.encode("utf-8"))

root.mainloop()