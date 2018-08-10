Balance = input("Please enter your current balance : $")
withdrawal = input("Please enter the amount you want to withdraw : $")
new_balance = Balance-withdrawal

if new_balance < 0:
    print "Withdrawal Denied"
elif new_balance < 10:
    print "Your balance is : $", new_balance
    print "Your balance below $10"
else:
    print "Your new balance is : $",new_balance


raw_input("Press Enter to escape")
