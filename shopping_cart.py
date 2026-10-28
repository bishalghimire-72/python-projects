cart = []
total = 0

while True:
    print("\n==== SHOPPING CART ====")
    print("1. Add item")
    print("2. view cart")
    print("3. remove item")
    print("4. show total")
    print("5. exit")

    choice = input("choose an option: ")

    if choice == "1":
        item = input("enter item name: ")
        price = float(input("enter item price: "))

        cart.append([item,price])
        total = total + price

        print(item, "added to cart.")

    elif choice == "2":
        if len (cart) == 0:
            print("your cart is empty.")
        else:
            print("\n your cart:")

            for item in cart:
                print(item[0], "-", item[1])

    elif choice == "3":
        item_to_remove = input("enter item name to remove:")

        found = False

        for item in cart:
            if item[0] == item_to_remove:
                cart.remove(item)
                total = total - item[1]
                print(item_to_remove,"removed from cart.")
                found = True
                break 

        if found == False:
          print ("items not found.") 

    elif choice == "4":
        print("total:",total)

    elif choice == "5":
        print("THANK YOU FOR SHOPPING")
        break

    else:
        print("invalid option.")         
