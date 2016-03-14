#! /usr/bin/python3
# import notify2
import os
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('XAUTHORITY', '/home/user/.Xauthority')
os.environ.setdefault('DISPLAY', ':0.0')

if not 'DISPLAY' in os.environ:
    os.environ['DISPLAY'] = ':0'



# os.system("notify-send 'RELAX' 'abhi nai aaya'")


url = "http://ggsipuresults.nic.in/ipu/results/resultsmain.htm"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'html.parser')



# notify2.init('app_name')
# print(soup.get_text())

if(soup.get_text().__contains__("Result ( Dec. 2015) of B.Tech. (CSE)")):
    os.system("notify-send 'SHIT' 'aa gaya result'")
    # n = notify2.Notification("BC",
    #                      "aa gaya result",
    #                      "notification-message-im"   # Icon name
    #                     )

elif(soup.get_text().__contains__("Result (Dec. 2015) of B.Tech. (CSE)")):
    os.system("notify-send 'SHIT' 'aa gaya result'")
    # n = notify2.Notification("BC",
    #                      "aa gaya result",
    #                      "notification-message-im"   # Icon name
    #                     )
else:
    os.system("notify-send 'RELAX' 'abhi nai aaya'")
    # n = notify2.Notification("Relax",
    #                      "abhi nai aaya",
    #                      "notification-message-im"   # Icon name
    #                     )




# n.show()
# print(notify2.get_server_info())