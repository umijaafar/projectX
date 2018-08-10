#import bluetooth

#nearby_devices = bluetooth.discover_devices(lookup_names = True,flush_cache = True,duration = 10)
#print nearby_devices
#paired = bluetooth.pair_devices ()





    
list = []
check = []
n = 0
id = "WD"
baca = open("scr.txt","r")

list = [line.rstrip("\n") for line in baca]
for i in list:

    n = n + 1
    if id in i:
        if i not in check:
            check.append(i)
            print i
            print list[n]


baca.close()

