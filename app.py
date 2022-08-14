import database

MENU_MESSAGE = """
 -- Currency App--
What would you like to do?

1) See all currency
2) Add a new currency
3) Delete a currency
4) Find a currency by name
5) Find a currency by type
6) Find a currency by price
7) Exit.

Your selection: """

def menu():
    connection = database.connect()
    database.create_table(connection)

    while(user_input := input(MENU_MESSAGE)) != "7":

        if user_input == "1":
            prompt_show_all_currencies(connection)
            
        elif user_input == "2":
            prompt_add_new_currency(connection)
            
        elif user_input == "3":
            prompt_delete_a_currency(connection)
            
        elif user_input == "4":
            prompt_find_currency_by_name(connection)
            
        elif user_input == "5":
            prompt_find_currency_by_type(connection)
            
        elif user_input == "6":
            prompt_find_currency_by_price(connection)
           
        else:
            print("Invalid input")

def prompt_show_all_currencies(connection):
    currencies = database.get_all_currency(connection)

    for currency in currencies:
        print(currency)

def prompt_add_new_currency(connection):
    name = input("Enter currency name: ")
    type = input("Enter the currency type: ")
    circulatingSupply = input("Enter the current circulation supply for this currency: ")
    price = input("Enter the current price per dollar: ")
    database.add_crypto(connection, name, type, circulatingSupply, price)

def prompt_delete_a_currency(connection):
    name = input("Enter the currency you would like to delete: ")
    database.delete_currency_by_name(connection, name)

def prompt_find_currency_by_name(connection):
    name = input("Enter the name of the currency you are looking for: ")
    currencies = database.get_currency_by_name(connection, name)

    for currency in currencies:
        print(currency)

def prompt_find_currency_by_type(connection):
    type = input("Enter the type of the currency you are looking for: ")
    currencies = database.get_currency_by_type(connection, type)

    for currency in currencies:
        print(currency)

def prompt_find_currency_by_price(connection):
    price = input("Enter the price of the currency you are looking for: ")
    currencies = database.get_currency_by_price(connection, price)

    for currency in currencies:
        print(currency)

menu()
