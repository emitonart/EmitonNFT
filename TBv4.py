print('V-20220822-2025 TBv4')


import tweepy
import time
import random

from daydrop import run24d
from getGMTDateTime import getGMT0DateTime

from FollowerHandler import FollowingHandler
from FollowerHandler import UnFollowingHandler


### Authenticate
from authentTW import authentTW

client = authentTW()



# datetime object containing current date and time

dt_string = getGMT0DateTime(2,-1)
dt_stringE = getGMT0DateTime(2,0)
print("date and time START= " + dt_string + " ||| date and time END= " + dt_stringE)


###
#Timeloop Handler
###


#Docs and Vars for Handler
welcomes = open('src/welcome.txt','r').read().splitlines()

nftdrop = open('src/NFTDrop.txt','r').read().splitlines()

#Timeloop Handler Function
def runTw ():
    #counter for s in 24h
    time24=62000
    cycles24=0
    
    while True:
        

        print('---1h init---')
        randWel = round(random.uniform(0, 23))
        randND = round(random.uniform(0, 31))
        print(str(randWel) +' '+ str(randND) +' '+getGMT0DateTime(2,0))
        print(str(welcomes[randWel])+' '+str(nftdrop[randND]))
        
        #create tweet
        client.create_tweet(text=str(welcomes[randWel])+' '+str(nftdrop[randND]))

        timeAdd = 3000+random.uniform(0, 1200)
        time24 = time24 + timeAdd

        #Call Following Checks for add end delete
        UnFollowingHandler()
        FollowingHandler()

        print(str(time24)+' Sec| '+str(cycles24)+' cycles')
        if time24 >= 62000:
            time.sleep(30+random.uniform(0, 30))
            print('---time24 init---')
            #create 24h tweet
            run24d()

            
            time24=0
            cycles24=cycles24+1

        time.sleep(timeAdd)


if __name__ == "__main__":
    runTw()