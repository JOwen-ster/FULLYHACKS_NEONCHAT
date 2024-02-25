import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


root.geometry('500x500')
root.title('NeonTooth')

label = tk.Label(root, text="Test", font=('Arial', 24))
label.pack(padx=20, pady=20)

def enter(event):
    if event.state == 8 and event.keysym == "Return":
        hello()


textbox = tk.Text(root, height=3, font=('Arial', 12))
textbox.pack(padx=10, pady=10)
textbox.bind("<KeyPress>", enter)


def hello():
    new = textbox.get('1.0', tk.END).strip()
    msg = tk.Label(root, text=new, font=('Arial', 12))
    msg.pack(padx=10, pady=10)

photo = tk.PhotoImage(file = r"neonbutton100x34.png")
tk.Button(root, image = photo, command=hello).pack(side=tk.TOP)




root.mainloop()