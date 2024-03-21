import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

port = 1000
for portx in range(1, 100):
    try:
        s.connect(('gmail.com', port))
        r = s.recv(1024)
        if 'Congratulations' in r.decode('utf-8'):
            print('[!] Hidden Service Found: %s ~ %s' % (port, r.decode('utf-8')))
            s.close()
            break
        else:
            print('%s ~ %s' % (port, r.decode('utf-8')))
            s.close()
    
    except socket.error as e:
        print('%s ~ %s' % (port, e))
    
    port += 1000
