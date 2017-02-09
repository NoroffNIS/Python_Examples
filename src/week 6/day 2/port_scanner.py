from socket import *
targetIP = '172.24.1.23'

for port in range(8000, 9000):
    try:
        print("[+] Attempting to connect to ",targetIP,":" , str(port))
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, port))
        print('Result:',result)

        if(result == 0) :
            print ('Port %d: OPEN' % (port,))
        else:
            print('Port %d: CLOSED' % (port,))

        s.close()
    except:
        pass





