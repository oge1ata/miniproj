import socket

# Define the hostname and port range
hostname = 'youtube.com'  # Change this to the target hostname
start_port = 1000
end_port = 60000

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)  # Set timeout to 2 seconds

# Iterate through the port range and attempt to connect
for port in range(start_port, end_port + 1):
    try:
        s.connect((hostname, port))
        print('%s ~ Port %d is open' % (port, port))
        # Do something with the open port
        s.close()  # Close the connection after use
    except socket.error as e:
        print('%s ~ %s' % (port, e))

# Close the socket after scanning all ports
s.close()
