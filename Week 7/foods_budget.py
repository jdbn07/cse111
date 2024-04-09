from datetime import datetime
import csv

Welcome = """
Welcome to Foods Budget!! 
This is a calculator that will help you plan and adjust your foods 
budget finances on a monthly basis. According on website toweinsurance.com,
"Budgeting creates a spending plan for your money and can help ensure there is 
always enough money to pay for food, bills, and other expenses... Budgeting 
can sound like a chore, but you may be surprised how powerful controlling 
your money will feel and how much stress is removed from your life." So we
have create this tool to organize your consumes better.
Your healthy finances are importants for your personal health! """
print(Welcome)
print()

def main():

    name_user = input("Name: ").capitalize()
    last_name = input("Last name: ").capitalize()
    budget = float(input("What is your estimated budget?: "))
    print(f"Hello {name_user}, your estimated budget is {budget}")

    option = show_menu()
    while option != 4:
        try:
            if option == 1:
                prod_name = input("Insert product: ").capitalize()
                w= input("weight(e.g. 500 gr): ")
                q= int(input("Quantity of product(e.g. 2: "))
                price = float(input("Price per unit: "))

                store_data(prod_name,w,q,price)
                show_menu()
            if option == 2:
                get_remove_item()
            if option == 3:
                compute_amount()
            if option == 4:
                get_exit()

        except TypeError as type_err:
            print(type_err)
        except Exception as excep:
            print(excep)

    
    print()
    print("Thank you for use our service. ")
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%A, %B %d - %I:%M:%S %p %Y}")

def show_menu():
    print("""
        ----------------------------
        1. Enter product
        2. remove item
        3. show amount
        4. exit
        ----------------------------
        """)
    
    try:
        option = int(input("Choose one option and enter the information: "))

    except ValueError as val_err:
        print(f"Error: {val_err}")
        print("You entered text that is not an integer. Please")
        print("run the program again and enter an integer.")
    return option
    
def get_exit():
    print("exit")
    print("Thanks to visit us")

def compute_amount(price,q):
    total_price=0
    comp_quant= price*q
    total_price=total_price+comp_quant
    return total_price

def read_list(filename):
    try:
        #open the csv file for reading
        with open(filename,"rt") as csv_file:
            #it create a reader object
            reader_products = csv.reader(csv_file)
            #skip the first line
            next(reader_products)
            #read one line at time

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")

    return reader_products

def print_list(prod_list):
    #print the list of products that the client will budget
    for groceries in prod_list:
        return groceries
    
def extract_product_file(products):
    for row in products:
                
        name = row[0]        
        quantity = int(row[1])
        value= products[name]
        name=value[0]
        price=float(value[1])
        print(f"{name:<15} | {quantity:<8} | ${price} ")


def store_data(prod,w,q,pric):
    #Here I store the user information in a csv file:
    file_stored = open('data_base.csv',"w")
    file_stored.write()

   
    return file_stored

def get_remove_item(total,amount,list_p):

    if total > amount:
        print("Oh, oh! passed your budget")
        option = int(input("Choose an option: 1.remove items / 2.extend the list(e.g.1): "))

        if option == 1:
            list_p.pop()

        if option == 2:
            amount_new = float(input("Insert your new budget: "))

    return amount_new
        

# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()