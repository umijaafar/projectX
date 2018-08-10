Name = raw_input("Please enter your name : ")
GSalary = input("Amount of your gross salary : RM")
KPI_index = input("Please insert your KPI index : ")

if KPI_index >= 0 :
    if KPI_index > 60 :
        if KPI_index > 80 :
            percent = 0.5
        else :
            percent = 0.2
    else :
        percent = 0.1
    Bonus = percent * GSalary
    print "Dear Mr/Mrs", Name,",your bonus is : RM ", Bonus
else :
    print "Invalid index"

raw_input("Press Enter to escape")
