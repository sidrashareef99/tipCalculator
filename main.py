input("What is your name? ")
subtotal = float(input("How much was your meal? "))

print("Subtotal:",subtotal)

percent_tip = float(input("What percent tip would you like to give? "))
decimal_tip = float(percent_tip /100)
tip_amount = float(format(subtotal * decimal_tip, ".2f"))

print("Your tip amount:",tip_amount)

sales_tax = (float(format((subtotal*.07),".2f")))

print("Sales tax amount:", sales_tax)

total_cost=float(format((subtotal+sales_tax+tip_amount),".2f"))

print("Your total cost is: ", total_cost)