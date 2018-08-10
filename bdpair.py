import bluetooth

#--Pair HC-05 with PC first

target_name = "Z0001"
target_address = None

nearby_devices = bluetooth.discover_devices()
print nearby_devices

for bdaddr in nearby_devices:
    print bluetooth.lookup_name( bdaddr )
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    print "Trying connection"
    #######################################
    i=0 # ---- your port range starts here
    maxPort = 3 # ---- your port range ends here
    err = True
    #while err == True and i <= maxPort:
     #   print "Checking Port ",i
    port = 3
    #try:
    sock.connect((target_address, port))
    err = False
    #except Exception,e:
            ## print the exception if you like
            #i += 1
    #if i > maxPort:
        #print "Port detection Failed."
        #exit(0)
    #######################################

    print "Trying sending"
    sock.send("scr.txt")
    print "Finished sending"
    print sock.recv()
    print "Finished receiving"
    sock.close()
else:
    print "could not find target bluetooth device nearby"
