from tkinter import *

root = Tk()
root.title("tkinter")
root.geometry("240x180")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btn_cmd():
    # Deletion
    # listbox.delete(0) # 맨앞 삭제
    # listbox.delete(END)

    # Counting
    print(listbox.size())

    print("1번째부터 3번째까지: ", listbox.get(0, 2))

    print("선택된 항목: ", listbox.curselection())


btn = Button(root, text="클릭", command=btn_cmd)
btn.pack()

root.mainloop()
