import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("300x240")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese").pack()
Button(frame_burger, text="chicken").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="coke").pack()
Button(frame_drink, text="juice").pack()

root.mainloop()
