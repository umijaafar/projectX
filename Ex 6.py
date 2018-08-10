sales = input("Please Insert your sales : RM ")

if sales <= 2000:
    commission_rate = 0.02
elif sales <= 4000:
    commission_rate = 0.04
elif sales <= 6000:
    commission_rate = 0.07
else:
    commission_rate = 0.1

commission = commission_rate*sales

print "Your commission rate is : ",commission_rate

print "Your commission earned is : ",commission

raw_input("Press Enter to escape")
