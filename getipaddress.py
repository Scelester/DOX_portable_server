import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

ipaddress = s.getsockname()[0]

print("\n\nYour server will run in=>\n"+ipaddress+"\n\n")
print("===="*6)
