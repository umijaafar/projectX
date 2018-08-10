from bluetooth import *
import bluetooth

nearby_devices = bluetooth.discover_devices(flush_cache=True)
for i in nearby_devices:
    bt = bluetooth.lookup_name(i)
    if bt == "Z0001":
        bdaddr = i
server_socket=BluetoothSocket( RFCOMM )

server_socket.bind(("",2))
server_socket.listen(1)

client_socket, address = server_socket.accept()
#if bdaddr in address:
    #print "From Z0001..."

data = client_socket.recv(1024)

if data != None:

    file = open("Location.txt", "w")
    file.write(data)
    file.close()
    print "received"
else:
    print "No data"
client_socket.close()
server_socket.close()
