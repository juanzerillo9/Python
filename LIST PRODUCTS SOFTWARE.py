"""

This is a program to add and List products in a memory.
It's only a prototype to practice with desktop environment!


"""

from tkinter import *
from tkinter import ttk

# VENTANA

ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)


# DISPLAYS

def home():
    #Setting display
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=145,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    #Listar productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text=" ---------- ").grid()

    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values=(product[1]))
    #Hidden another display
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()
    return True

def add():

    #Header

    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=125,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Form Camps
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
        )

    #Hidden another display
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    return True



def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=217,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    
    
    #Hidden another display
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    return True


def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


# App variables
products = []

name_data = StringVar()
price_data = StringVar()

#Define Displays HOME
home_label = Label(ventana, text="Products List")
#products_box = Frame(ventana, width=250)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Product', anchor=W)
products_box.heading("#1", text='Price', anchor=W)

#Define Displays ADD
add_label = Label(ventana, text="Add a Product")

#Form camp
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Name: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Price: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Description: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text=("Add"), command=add_products)


#Define Displays INFO
info_label = Label(ventana, text="Info")
data_label = Label(ventana, text="Created By JZ9 - 2022")

# LOAD HOME IN PROGRAM
home()

# MENU

menu_superior = Menu(ventana)

menu_superior.add_command(label="Home", command=home)
menu_superior.add_command(label="Add", command=add)
menu_superior.add_command(label="Info", command=info)
menu_superior.add_command(label="Quit", command=ventana.quit)


#Cargar menu
ventana.config(menu=menu_superior)

#CARGAR VENTANA
ventana.mainloop()
