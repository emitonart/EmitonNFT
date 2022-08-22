print('V-20220822-2025 daydrop')

import json

import time
import random
from getGMTDateTime import getGMT0DateTime

welcomes = open('src/welcome.txt','r').read().splitlines()


f= open('src/24offers.json')
offers24 = json.load(f)

offernr = 2 #Change for other start in 24offers.json

from authentTW import authentTW
client = authentTW()


def run24d():

    global client
    global offernr
    global welcomes

    # datetime object containing current date and time

    dt_string = getGMT0DateTime(2,-1)
    dt_stringE = getGMT0DateTime(2,0)
    print("date and time START= " + dt_string + " ||| date and time END= " + dt_stringE)


    # init Tweetsearch
    querytext='"drop your nft" -is:retweet -@drop_your_nft_ -@drop_your_nft'
    response = client.search_recent_tweets(query=querytext, max_results=10, start_time=dt_string,  tweet_fields=['id','author_id','text','created_at'])
    print(response.meta['result_count'])
    print(response.data[0].id)

    #    time.sleep(0+random.uniform(0, 5))


    print('----------------------24h---------------------------')


    #create tweet handler 
    randWel = round(random.uniform(0, 23))
    tweet24 = (str(welcomes[randWel])+' '+'Check this! ' + str( offers24['art'][offernr]['titel']) +'\n\n'
    + '--- #nft #NFTCommmunity #NFTCollection #art #poesie #Philosophy' +'\n'
    + str( offers24['art'][offernr]['text'])  +'\n'
    + str( offers24['art'][offernr]['url']) +' via @opensea')

    print(tweet24)

    client.create_tweet(text=tweet24, in_reply_to_tweet_id=response.data[0].id)
    offernr = offernr + 1
    if offernr >= len(offers24['art'])-1:
        offernr=0

    time.sleep(30+random.uniform(0, 30))
    #create tweet handler
    randWel = round(random.uniform(0, 23))
    tweet24 = (str(welcomes[randWel])+' '+'Check this! ' + str( offers24['art'][offernr]['titel']) +'\n\n'
    + '--- #nft #NFTCommmunity #NFTCollection #art #poesie #Philosophy' +'\n'
    + str( offers24['art'][offernr]['text'])  +'\n'
    + str( offers24['art'][offernr]['url']) +' via @opensea')

    print(tweet24)
    client.create_tweet(text=tweet24)


    offernr = offernr + 1
    if offernr >= len(offers24['art'])-1:
        offernr=0
