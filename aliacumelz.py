number=input("How many numbers:")
count=0
total_num=0
while number<>0:
    total_num=total_num+number
    number=number-1
    count=count+1
    print "x=", str(count)

average=total_num/count

print "the average is" , average
    
    
