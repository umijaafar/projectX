print """
________________________
Welcome to My time table
^^^^^^^^^^^^^^^^^^^^^^^^
"""

tableNumber = input("Choose your number")

for number in range(9):
    number = number + 1
    total = number * tableNumber
    print number ,"x", tableNumber,"=", total
    
