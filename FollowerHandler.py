print('V-20220822-2025 FollowerHandler')

import json
import time
from getGMTDateTime import getGMT0DateTime

UserIdAcc = '1559187330828836864' #Emiton
UserNameAcc = 'emiton' #Emiton

### Authenticate
from authentTW import authentTW
client = authentTW()

def FollowingHandler():
    print('------------FollowingHandler----------------')
    global client


    response=client.get_users_tweets(UserIdAcc,max_results=48)
    
    #print(response)

    fd= open('src/following.json','r')
    followingDATAS = json.load(fd)
    fd.close()
    foundNewFollowings=0

    qtext="@EmitonNFT"
    response=client.search_recent_tweets(query=qtext,start_time=getGMT0DateTime(2,-12), max_results=100, tweet_fields=['id','author_id','text','created_at','in_reply_to_user_id'])
    followers=client.get_users_followers(id=UserIdAcc, max_results=1000)
    following=client.get_users_following(id=UserIdAcc, max_results=1000)

    
    for tweet in response.data:

        if foundNewFollowings >=13: #limit 50/15min  ->400/Tag sind 13.8/h bei 3000fq
            break

        print(tweet.id,tweet.author_id,tweet.text, tweet.created_at, tweet.in_reply_to_user_id)

        if str(tweet.author_id) not in str(followers.data): #is not follower
                   
            if str(tweet.author_id) not in str(following.data): #i'm not following
 
                    if str(tweet.author_id) not in str(followingDATAS['followings']):  #i never followed

                        #follow -> write in list for later checked unfollow

                        client.follow_user(tweet.author_id)

                        followerdata={}
                        followerdata['user_id']=tweet.author_id
                        followerdata['AddingDateTime']=getGMT0DateTime(2,0)
                        followerdata['UnfollowDateTime']=getGMT0DateTime(2,+120)
                        followerdata['Unfollowed']=0
  
                        foundNewFollowings=foundNewFollowings+1
                        followingDATAS['followings'].append(followerdata)
                        time.sleep(1)
                         
    
    if foundNewFollowings>=1:
        print('->NEW FOLLOWINGS:'+ str(foundNewFollowings))
        with open('src/following.json', 'w') as json_file:
            json.dump(followingDATAS, json_file, indent=4,  sort_keys=True, separators=(',',':'))
            fd.close()


def UnFollowingHandler():
    print('------------UNfollowingHandler')
    fd= open('src/following.json','r')
    followingDATAS = json.load(fd)
    fd.close()

    unfollowingscount=0

    for following in followingDATAS['followings']:

        if unfollowingscount>=17: #500 per day 3000s/24h ->17.3max
            break

        #print(str(int(following['UnfollowDateTime'].replace('-','').replace(':','').replace('T',''))))
        #print(str(int(getGMT0DateTime(2,0).replace('-','').replace(':','').replace('T',''))))
        if int(following['UnfollowDateTime'].replace('-','').replace(':','').replace('T','')) <= \
            int(getGMT0DateTime(2,0).replace('-','').replace(':','').replace('T','')) and\
            following['Unfollowed']==0:

            print('UNFOLLOW: '+ str(following['user_id']))
            client.unfollow_user(following['user_id'])
            unfollowingscount=unfollowingscount+1

            following['Unfollowed']=1
            time.sleep(1)

            #Data of ExFollingsRemains for further checks 

    #write Changes to file
    if unfollowingscount>=1:
        print('->UNFOLLOWINGS Count: '+ str(unfollowingscount))
        with open('src/following.json', 'w') as json_file:
            json.dump(followingDATAS, json_file, indent=4,  sort_keys=True, separators=(',',':'))
            fd.close()


        


