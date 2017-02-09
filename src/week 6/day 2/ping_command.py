import os

targetIP = '172.24.1.25'
response = os.system("ping -n 2 " + targetIP)

print('Response:',response)
#and then check the response...
if response == 0:
    print(targetIP, 'is up!')
else:
    print(targetIP, 'is down!')

