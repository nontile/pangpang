import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")


def info():
    msgbox.showinfo("alarm", "Reservation was completed normally")


def warn():
    msgbox.showwarning("warn", "These seats were sold out")


def error():
    msgbox.showerror("error", "A Payment Exception has occurred")


def okcancel():
    msgbox.askokcancel("ok / cancel", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")


def retrycancel():
    msgbox.askretrycancel("retry / cancel", "temporary error! Do you try again?")


def yesno():
    msgbox.askyesno("Yes / No", "yes or no?")


def yesnocancel():
    res = msgbox.askyesnocancel("yes / no / cancel", "What's your choice?")
    # 네 : 저장 후 종료
    # 아니요 : 자장하지 않고 종료
    # 취소 : 프로그램종료취소(현재 화면에서 계속 작업)
    print("응답: ", res)  # True, False, None -> 1, 0, rest
    if res == 1:
        print("Yes")
    elif res == 0:
        print("No")
    else:
        print("Cancel")


Button(root, command=info, text="alarm").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="ok cancel").pack()
Button(root, command=retrycancel, text="ok cancel").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()

root.mainloop()
