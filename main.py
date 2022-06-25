
total_price = float(input("How much is the bill in total?"))
num_of_people = float(input("How many of you need to pay?"))
percent_of_tip = float(input("according to the services of waitors/waitress, \nwhat percentage of tip do you want to offer?"))
payable = (1+percent_of_tip/100)* total_price/num_of_people
print(payable)

