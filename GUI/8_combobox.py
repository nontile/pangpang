import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")

values = [str(i) + "일" for i in range(1, 32)]  # 1 - 31
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)  # 0번째 인데스 선택
readonly_combobox.pack()


def btn_cmd():
   print(combobox.get())
   print(readonly_combobox.get())


btn = Button(root, text="Click", command=btn_cmd)
btn.pack()

root.mainloop()
