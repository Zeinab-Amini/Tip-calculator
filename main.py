#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
#float is better for money instead of int
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100 
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
#not * tip (math for percentage)
each_person = total_bill / people
final_amount = "{:.2f}".format(each_person)
#add 0 if not needed for money

print(f"Each person has to pay ${final_amount}")