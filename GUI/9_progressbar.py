import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10 ms 마다 움직임
# progressbar.pack()
#
#
# def btn_cmd():
#    progressbar.stop()
#
#
# btn = Button(root, text="Click", command=btn_cmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btn_cmd():
   for i in range(1, 101):
      time.sleep(0.01)
      p_var2.set(i)
      progressbar2.update() # ui update
      print(p_var2.get())


btn = Button(root, text="Start", command=btn_cmd)
btn.pack()

root.mainloop()
