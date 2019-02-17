import socket

hosts = ['www.uc.edu','www.google.com','www.reddit.com']
print('working from host: %s' % socket.fqdn())
for h in hosts:
    print (h + ': ' + socket.gethostbyname(h))

