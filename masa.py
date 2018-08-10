import bluetooth
import serial
import datetime
import time

while (1):

    nearby_devices = bluetooth.discover_devices(flush_cache=True)
    idw = []
    count = 0
    while count < 10000:
        idw.append(count)
        count = count+1
    else:
        for i in nearby_devices:
            bt = bluetooth.lookup_name(i)
            print (str(bt))
            for num in idw:
                if bt == "WD{0:04d}".format(idw[num]):
        
                    time = datetime.datetime.now()
                    x = '1'
    
                    if x == '1':
                        file = open("scr.txt","a")
                        file.write(str(bt) + "\n")
                        file.write(str(time) + "\n")
                        file.close()
                        print ("Connected")
            #else:
                #print ("not connected")


