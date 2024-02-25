import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

root = tk.Tk()


root.geometry('500x500')
root.title('NeonTooth')

label = tk.Label(root, text="Test", font=('Arial', 24))
label.pack(padx=20, pady=20)

def enter(event):
    # prints to check key
    # print(event.state)
    # print(event.keysym)
    if event.keysym == "Return":
        if event.state == 9:
           msg.delete(tk.END) 
        elif event.state == 8:
            hello()

def stopText(event):
    msg.delete(tk.LAST, tk.END)

msg = scrolledtext.ScrolledText(root, height=6, font=('Arial', 12))
msg.bind("<KeyPress>", stopText)
msg.pack(padx=10, pady=10)
textbox = tk.Text(root, height=1, font=('Arial', 12))
textbox.pack(padx=10, pady=10)
textbox.bind("<KeyPress>", enter)


def hello():
    new = textbox.get('1.0', tk.END).strip()
    msg.insert(tk.INSERT, new + "\n")
    textbox.delete(1.0, tk.END)

photo = tk.PhotoImage(file = r"images/neonbutton100x34.png")
tk.Button(root, image = photo, command=hello).pack(side=tk.TOP)




root.mainloop()