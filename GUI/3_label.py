from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")
label1 = Label(root, text="안녕")
label1.pack()

photo = PhotoImage(file="images/check_green.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="Hello")

    global photo2
    photo2 = PhotoImage(file="images/check_red.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
