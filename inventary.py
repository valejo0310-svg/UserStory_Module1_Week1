print("""
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!             
╚════════════════════════════════════════════════════════════╝
""")

sales = []


print("-----Register a New Sale -----".center(60))


values = True
while values:

    try:

        product = input("\nIntroduce the product to purchase: ")
        price = float(input("Introduce the price: "))
        quantity = int(input("Introduce how many products are being purchased: "))
    except ValueError:
        
        print("Please use the correct values")
        continue  
