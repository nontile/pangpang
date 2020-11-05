from tkinter import *

root = Tk()
root.title("나도")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버트2222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버트3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버트4444444444444411")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="images/check_green.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btn7_cmd():
    print("버튼이 클릭 되었습니다.")


btn7 = Button(root, text="동작하는버튼", command=btn7_cmd)
btn7.pack()

root.mainloop()
