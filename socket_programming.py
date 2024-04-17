# Socket Programming in Python
# ip = socket.gethostbyname('www.google.com')  #gethostbyname is for finding ip addresses

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET id for ipv4, SOCK_STREAM is for connection oriented TCP protocol
    print("Socket successfully created!")
except socket.error as err:
    print(f"Socket creation failed with error {err}")

port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:  # gaierror means there's a problem with the dns
    print("Error resolving the host")
    sys.exit()
s.connect((host_ip, port))
print(f'Socket has successfully connected to Github on port == {host_ip}')
