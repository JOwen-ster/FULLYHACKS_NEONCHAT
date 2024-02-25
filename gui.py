import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import server
import client

root = tk.Tk()



root.geometry('500x500')
root.title('Neon Chat')

label = tk.Label(root, text="NEON CHAT", font=('Arial', 24))
label.pack(padx=20, pady=20)

def enter(event):
    # prints to check key
    # print(event.state)
    # print(event.keysym)
    if event.keysym == "Return":
        if event.state == 9:
           msg.delete(tk.END) 
        elif event.state == 8:
            get_text()

def stopText(event):
    if event:
        msg.delete(tk.END)

msg = scrolledtext.ScrolledText(root, height=6, font=('Arial', 12))
msg.bind("<KeyPress>", stopText)
msg.pack(padx=10, pady=10)
textbox = tk.Text(root, height=1, font=('Arial', 12))
textbox.pack(padx=10, pady=10)
textbox.bind("<KeyPress>", enter)


def get_text():
    new = textbox.get('1.0', tk.END).strip()
    if not new:
        return
    msg.insert(tk.INSERT, new + "\n")
    textbox.delete(1.0, tk.END)
    client.send(new.encode("utf-8"))

photo = tk.PhotoImage(file = r"images/neonbutton100x34.png")
tk.Button(root, image = photo, command=get_text).pack(side=tk.TOP)


tk.Button(root, text="host", command=server.run_server).pack(side=tk.TOP)
tk.Button(root, text="join", command=client.run_client).pack(side=tk.TOP)

root.mainloop()