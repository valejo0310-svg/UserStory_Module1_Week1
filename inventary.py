# Welcome message for the sales register
print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")

# Creation of a list to store the sales
sales = []

# Starting message
print("-----Register a New Sale -----".center(60))

# Loop to keep asking for the inputs if the user doesn't enter the right values
values = True
while values:
#Try and except to control the possible mistakes made by the user
    try:
#Asking for the data necesary to make the purchase
        product = input("\nIntroduce the product to purchase: ")
        price = float(input("Introduce the price: "))
        quantity = int(input("Introduce how many products are being purchased: "))
    except ValueError:
        
        print("Please use the correct values")
        continue  # Used to keep the loop going if the values are wrong

   #Dictionary made to stroe all the data entered by the client
    sell = {
        "product": product,
        "price": price,
        "quantity": quantity
    }
#Adding the values of the dictionary  to the list
    sales.append(sell)
#Variable created to calculate the total cost of everything 
#Initially zero so it can be redefinied later on
    total_cost = 0
#loop made to take values from the values and the dictionary to make the final cost
    for sell in sales:
        total_cost += sell["price"] * sell["quantity"]

    # Final message to show the purchase
    print("=" * 60)
    print("TOTAL PURCHASE".center(60))
    print("=" * 60)
#For loop used to show all the data and the total
    for sell in sales:
        print("Product:", sell["product"])
        print("Quantity sold:", sell["quantity"])
    print(f"Your total is: {total_cost}")
    exit ()
