payment = 100.00
insert = input("Please insert the amount you want to pay")
balance = insert-payment
while balance < 0:
    print abs(balance)
    insert = input("Please insert the amount you want to pay")
    balance = insert+balance

print balance
