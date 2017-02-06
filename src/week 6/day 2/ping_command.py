import os

targetIP = '172.24.1.25'
response = os.system("ping -c 2 " + targetIP)

#and then check the response...
if response == 0:
    print(targetIP, 'is up!')
else:
    print(targetIP, 'is down!')

