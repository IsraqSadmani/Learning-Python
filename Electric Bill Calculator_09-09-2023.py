'''Write a program in python to calculate and print the electricity bill of a given
customer. The customer ID, name and unit consumed by the user should be captured
from the keyboard to display the total amount to be paid to the customer.

NB-1: Unit-Bill rate Range: =100 unit @1.00, >100-500 unit @2.00, >500-700 unit @5.00,
>700 unit @10.00

NB-2: If bill exceeds TK 400 then a surcharge of 15% will be charged and the minimum
bill should be of TK 100'''

#Input Customer ID, Name, Unit Consumed

c_id = input("Enter Customer IDNO.: ") #Input customer IDNO
c_name = input("Enter Customer Name: ") #Input customer name
unit = float (input("Total Electricity Consumed: ")) #Input electricity consumed

#Bill Flooring

floor_1 = 100
floor_2 = 400
floor_3 = 200
floor_4 = (unit - 700)

#Bill_Calculation

if unit > 700:
    floor_1 = 100
    floor_2 = 400
    floor_3 = 200
    floor_4 = (unit - 700)
elif unit > 500:
    floor_1 = 100
    floor_2 = 400
    floor_3 = (unit - 500)
    floor_4 = 0
elif unit > 100:
    floor_1 = 100
    floor_2 = (unit - 100)
    floor_3 = 0
    floor_4 = 0
else:
    floor_1 = unit
    floor_2 = 0
    floor_3 = 0
    floor_4 = 0

bill = (floor_1 * 1.00 + floor_2 * 2.00 + floor_3 * 5.00 + floor_4 * 10.00)

#Surcharge Calculation
sur_rate = 0.15

if bill > 400:
    sur_rate = 0.15
else:
    sur_rate = 0.00

surcharge = (bill * sur_rate)
net_bill = (bill + surcharge)

#Minimum Bill Condition

if bill < 100:
    net_bill = 100.00

#Bill Printing

print("Customer IDNO:", c_id,
      "\nCustomer Name:", c_name,
      "\nUnit Consumed:", unit,
      "\nActual Bill Amount:", bill,
      "\nSurcharge Amount:", surcharge,
      "\nNet Amount Payable:", net_bill)
