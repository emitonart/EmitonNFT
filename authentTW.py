print('V-20220820-2231 autentTW')

import tweepy

def authentTW():

    all_keys = open('src/twitterkeys.env','r').read().splitlines()
    api_key = all_keys[0]
    api_key_secret = all_keys[1]
    access_token = all_keys[2]
    access_token_secret = all_keys[3]

    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    ret = tweepy.Client(consumer_key=all_keys[0],
    consumer_secret=all_keys[1],
    access_token=all_keys[2],
    access_token_secret=all_keys[3],
    bearer_token=all_keys[4]
    )
    return ret