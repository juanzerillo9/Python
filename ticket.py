import mysql.connector

#Conexion a base de datos

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ticket"
)

cursor = database.cursor(buffered=True)


def add_product():

    np = input("Add your product: ")
    npp = input("Add product price: ")
    value = [
        (np, npp)
    ]
    cursor.executemany("INSERT INTO products VALUES(null, %s, %s)", value)

    return main()


def seeBD():
    cursor.execute("SELECT * FROM products")
    # SACAR DATOS, tambien puede utilizarse fectchone para sacar el primer dato
    result = cursor.fetchall()
    print("-----TUS productos-----")
    for prd in result:
        print(prd)
    return main()

def order_product():
    id = input("Insert product ID: ")
    quant = int(input("Ingrese la cantidad de el producto: "))
    value = [
        (id)
    ]
    cursor.execute("SELECT * FROM products WHERE id = %s", value)
    # SACAR DATOS, tambien puede utilizarse fectchone para sacar el primer dato
    result = cursor.fetchall()
    cart = ()
    for p in result:
        cart = (p[1], p[2], quant)

    return pedido(cart)

def pedido(cart):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart(
        product varchar(40) not null,
        price float(10, 2) not null,
        quant int(5) not null
    )
    """)
    value = [
        (cart[0], cart[1], cart[2])
    ]

    cursor.executemany("INSERT INTO cart VALUES(%s, %s, %s)", value)
    
    return order()

def cart():
    cursor.execute("SELECT * FROM cart")
    result = cursor.fetchall()
    print("-----YOUR CART-----")
    for prd in result:
        print(prd)
    return order()

def order():
    print("""
    
    START A ORDER:

    PRESS 1 FOR ADD A PRODUCT
    PRESS 2 TO PRINT THE ORDER
    PRESS 3 TO SEE YOUR CART
    PRESS 4 TO CANCEL
    
    """)

    opt = input("OPTION: ")

    if opt == '1':
        return order_product()
    try:
        if opt == '2':
            return print_order()
    except:
        print("There are no items")
    if opt == '3':
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cart(
        product varchar(40) not null,
        price float(10, 2) not null,
        quant int(5) not null
        )
        """)
        return cart()
    if opt == '4':
        cursor.execute("DROP TABLE cart")
        print(cursor.rowcount, "Borrados!!")
        main()
    else:
        print("Error")\

    return main()


def print_order():
    cursor.execute("SELECT * FROM cart")
    result = cursor.fetchall()
    print("YOUR TICKET".center(40,"*"))
    print()
    total = 0

    for prd in result:
        print(f'{prd[0]}'.ljust(30,"."), end="")
        print(f'{(prd[1]*float(prd[2]))}'.rjust(10, "."))
        print() 
        total += float(prd[1]*prd[2])

    #print(f'{prd[0]} ........ {int(prd[1])*prd[2]}'.center())
    print('-'*40)
    print()
    print('TOTAL'.ljust(30,"."), end="")
    print(str(total).rjust(10, "."))
    print()
    print('*'*40)
    return order()

def main():
    print("""
    
    Welcome to the TICKETET

    PRESS 1 FOR ADD A PRODUCT
    PRESS 2 FOR SHOW YOUR PRODUCTS
    PRESS 3 TO TAKE A ORDER
    PRESS 4 TO EXIT
    """)

    option = input("Select an option: ")
    if option == '1':
        add_product()
    if option == '2':
        seeBD()
    if option == '3':
        order()
    if option == '4':
        exit()
    
main()

#GUARDAR CAMBIOS
database.commit()