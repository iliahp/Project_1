import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

product_list = []


def sell_item():
    item = {
        "brand": brand.get(),
        "model": model.get(),
        "color": color.get(),
        "glass": glass.get(),
        "memory": memory.get()
    }
    product_list.append(item)
    msg.showinfo("save", f"Sell Item {item} saved")
    refresh_table()
    brand.set("")
    color.set("")
    model.set("")

def refresh_table():
    # Clear Table
    for items in table.get_children():
        table.delete(items)

    for item in product_list:
        table.insert("", tkinter.END, values=tuple(item.values()) )


win = tkinter.Tk()
win.title('Mobile')
win.geometry('550x350')
win.resizable(False, False)

tkinter.Label(win, text="brand").place(x=30, y=25)
brand = tkinter.StringVar()
ttk.Combobox(win, textvariable=brand, values=["apple", "samsung", "nokia"], state="readonly").place(x=90, y=25)

tkinter.Label(win, text="model").place(x=30, y=75)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model, width=23).place(x=90, y=75)

tkinter.Label(win, text="color").place(x=30, y=125)
color = tkinter.StringVar()
ttk.Combobox(win, textvariable=color, values=["white", "black", "red", "blue"], state="readonly").place(x=90, y=125)

table = ttk.Treeview(win, columns=(1, 2, 3), height=12, show="headings")
table.heading(1, text="brand")
table.heading(2, text="model")
table.heading(3, text="color")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.place(x=260, y=20)

tkinter.Label(win, text="option").place(x=30, y=175)
glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="Glass", variable=glass).place(x=90, y=165)
memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="memory", variable=memory).place(x=90, y=185)

tkinter.Button(win, text="sell", width=30,height=2, command=sell_item).place(x=30, y=225)

refresh_table()

win.mainloop()
