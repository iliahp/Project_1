import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

product_list = []


def items():
    item = {
        "product": product.get(),
        "price": price.get(),
        "count": count.get(),
    }

    product_list.append(item)
    msg.showinfo("save", f"Sell Item {item} saved")
    refresh_table()
    product.set("")
    price.set("")
    count.set("")


def refresh_table():
    # Clear Table
    for items in table.get_children():
        table.delete(items)

    for item in product_list:
        table.insert("", tkinter.END, values=tuple(item.values()))


win = tkinter.Tk()
win.title('Mobile')
win.geometry('550x350')
win.resizable(False, False)

tkinter.Label(win, text="product").place(x=30, y=30)
product = tkinter.StringVar()
tkinter.Entry(win, textvariable=product, width=23).place(x=90, y=30)

tkinter.Label(win, text="price").place(x=30, y=120)
price = tkinter.IntVar()
tkinter.Entry(win, textvariable=price, width=23).place(x=90, y=120)

tkinter.Label(win, text="count").place(x=30, y=75)
count = tkinter.IntVar()
tkinter.Entry(win, textvariable=count, width=23).place(x=90, y=75)

tkinter.Label(win, text="all sm").place(x=30, y=160)
all_sm = tkinter.IntVar()
tkinter.Entry(win, textvariable=all_sm, width=23,state="readonly").place(x=90, y=160)

table = ttk.Treeview(win, columns=(1, 2, 3), height=12, show="headings")
table.heading(1, text="product")
table.heading(2, text="price")
table.heading(3, text="count")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.place(x=260, y=20)

tkinter.Button(win, text="in", width=30, height=2, command=items).place(x=30, y=190)
tkinter.Button(win, text="out", width=30, height=2, command=items).place(x=30, y=240)

refresh_table()

win.mainloop()
