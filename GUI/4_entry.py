from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")

txt = Text(root, width=20, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=20)
e.pack()
e.insert(0, "One line")


def btncmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
