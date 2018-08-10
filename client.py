from bluetooth import *
import bluetooth

nearby_devices = bluetooth.discover_devices(flush_cache=True)
for i in nearby_devices:
    bt = bluetooth.lookup_name(i)
    print i
    print bt
    if bt == "Z0001":
        bdaddr = i
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect((bdaddr, 3))

client_socket.send(scr.txt)

print "Finished"

client_socket.close()
