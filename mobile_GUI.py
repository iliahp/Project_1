import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg


def sell_item():
    item = {
        "brand": brand.get(),
        "model": model.get(),
        "color": color.get(),
        "glass": glass.get(),
        "memory": memory.get()
    }
    msg.showinfo("save", f"Sell Item {item} saved")


win = tkinter.Tk()
win.title('Mobile')
win.geometry('300x500')
win.resizable(False, False)

tkinter.Label(win, text="brand").place(x=30, y=50)
brand = tkinter.StringVar()
ttk.Combobox(win, textvariable=brand, values=["apple", "samsung", "nokia"], state="readonly").place(x=90, y=50)

tkinter.Label(win, text="model").place(x=30, y=100)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model, width=23).place(x=90, y=100)

tkinter.Label(win, text="color").place(x=30, y=150)
color = tkinter.StringVar()
ttk.Combobox(win, textvariable=color, values=["white", "black", "red", "blue"], state="readonly").place(x=90, y=150)

tkinter.Label(win, text="option").place(x=30, y=200)
glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="Glass", variable=glass).place(x=90, y=190)
memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="memory", variable=memory).place(x=90, y=210)

tkinter.Button(win, text="sell", width=20, command=sell_item).place(x=90, y=250)

win.mainloop()
