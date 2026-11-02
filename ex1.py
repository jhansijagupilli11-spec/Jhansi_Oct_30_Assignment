print("=====WELCOME TO JHANSI RESTAURANT =====")
name = input("Enter customer name: ")
print("1. Biryani - Rs.250")
print("2. Pizza - Rs.200")
print("3. Burger - Rs.120")
print("4. Fried Rice - Rs.150")
print("5. Sandwich - Rs.100")
food = input("Enter food choice: ")
if food == "biryani":
    price = 250
elif food == "pizza":
    price = 200
elif food == "burger":
    price = 120
elif food == "fried rice":
    price = 150
elif food == "sandwich":
    price = 100
else:
    price = 0
if price > 0:
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    if total >= 1000:
        discount = total * 0.10
    elif total >= 500:
        discount = total * 0.05
    else:
        discount = 0
    final_amount = total - discount
    option = input("Dine in or Take away: ")
    payment = input("Enter payment method: ")
    print("***** CUSTOMER BILL *****")
    print(f"Customer Name: {name}")
    print(f"Food Item: {food}")
    print(f"Price: Rs.{price}")
    print(f"Quantity: {quantity}")
    print(f"Total: Rs.{total}")
    print(f"Discount: Rs.{discount}")
    print(f"Final Amount: Rs.{final_amount}")
    print(f"Dining: {option}")
    print(f"Payment: {payment}")
else:
    print("Food item not available!")
print("THANK YOU! VISIT AGAIN!")