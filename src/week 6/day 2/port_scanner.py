from socket import *
targetIP = '172.24.1.25'

for i in range(8000, 9000):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print ('Port %d: OPEN' % (i,))
            print(s.recv(result))
        s.close()