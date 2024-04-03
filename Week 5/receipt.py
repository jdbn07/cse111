import csv
from datetime import datetime



PRODUCTS_NUMBER_INDEX= 0
PRODUCTS_NAME_INDEX=1
PRODUCTS_PRICE_INDEX =2

def main():    
    try:
        products = read_products("products.csv")
        #print(products)
        for key,value in products.items():
            print(key,value)
        
        print("---------------------------------------------------")
     
        company = " Inkom Emporium ".upper()
        print(company.center(50, ":"))
        print("Welcome to my store. We are at your service!")
        print()

        item=0
        subtotal=0
        total=0
        with open("request.csv","rt") as csv_file:
            reader_request = csv.reader(csv_file)
            next(reader_request)

            print("Purchase details: ")
            print("===================================")
            print("{:<15} {:<10} {}".format("Product","Quantity","Price"))
                #read the content in request file one line at a time
            for row in reader_request:
                
                number = row[0]        
                quantity = int(row[1])
                value= products[number]
                name=value[0]
                price=float(value[1])
                print(f"{name:<15} | {quantity:<8} | ${price} ")
               
                item+=quantity
                subtotal+= quantity*price
                sales_tax = subtotal*0.06
                total = round(subtotal + sales_tax,2)
             
            print("===================================")
            
            print(f"\nNumber of Items: {item}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total}")
            

        print()
        print("Thank you for you purchase. ")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A, %B %d - %I:%M:%S %p %Y}")
        
             
    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        
    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        
    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
           
    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")
  

def read_products(file_products):
    products= {}
    
    #open the csv file for reading
    with open(file_products,"rt") as csv_file:
        #it create a reader object
        reader_products = csv.reader(csv_file)
        #skip the first line
        next(reader_products)
        #read one line at time
        for row in reader_products:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row[0]
            products[key]=[row[1],float(row[2])]
    return products


if __name__ == "__main__":
    main()