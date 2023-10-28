from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
import os


def decrypt():
    password = code.get()

    if password == "2002":
        win2 = Toplevel(win)
        win2.title("decryption")
        win2.geometry("700x700")
        win2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(win2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(win2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=200, y=60, width=400, height=150)
        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "2002":
        messagebox.showerror("encryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "2002":
        win1 = Toplevel(win)
        win1.title("encryption")
        win1.geometry("700x700")
        win1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(win1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(win1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=200, y=60, width=400, height=150)
        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "2002":
        messagebox.showerror("encryption", "Invalid Password")


def main_screen():
    global win
    global code
    global text1
    win = Tk()
    win.geometry("1500x1500")
    win.title("message app")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    text1 = Text(font="Rpbote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=450, y=50, width=600, height=150)
    Label(text="Enter Secret key for encryption and decryption", fg="black", font=("calbri", 28)).place(x=380, y=230)

    code = StringVar()
    Entry(textvariable=code, width=50, bd=0, font="arial,25", show="*").place(x=470, y=350)

    Button(text="ENCRYPT", height="3", width="25", bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=470, y=450)

    Button(text="DECRYPT", height="3", width="25", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=840, y=450)

    Button(text="RESET", height="3", width="50", bg="#1089ff", fg="white", bd=0, command=reset).place(x=570, y=600)

    win.mainloop()


main_screen()
