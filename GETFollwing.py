print('V-20220822-2025 GET Following')

import json
import time
from getGMTDateTime import getGMT0DateTime

UserIdAcc = '1559187330828836864' #Emiton
UserNameAcc = 'emiton' #Emiton

### Authenticate
from authentTW import authentTW
client = authentTW()

def GetFollowing():
    global client
  
    #print(response)
        
    print('------------------------------')


    fd= open('src/following.json','r')
    followingDATAS = json.load(fd)
    foundNewFollowings=0
    
    following=client.get_users_following(id=UserIdAcc, max_results=1000)

    
    for users in following.data:

        print(users.id)

        

        followerdata={}
        followerdata['user_id']=users.id
        followerdata['AddingDateTime']=getGMT0DateTime(2,0)
        followerdata['UnfollowDateTime']=getGMT0DateTime(2,+120)
        followerdata['Unfollowed']=0

        
                            
        foundNewFollowings=foundNewFollowings+1
        followingDATAS['followings'].append(followerdata)
        
                         
    
    if foundNewFollowings>=1:
        with open('src/following.json', 'w') as json_file:
            json.dump(followingDATAS, json_file, indent=4,  sort_keys=True, separators=(',',':'))
            fd.close()


GetFollowing()

        


