from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동선택
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()


def btn_cmd():
   print(chkvar.get())


btn = Button(root, text="클릭", command=btn_cmd)
btn.pack()

root.mainloop()
