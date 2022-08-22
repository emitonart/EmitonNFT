print('V-20220822-2025 getGMTDateTime')

from datetime import datetime
from datetime import timedelta

def getGMT0DateTime(localGmt, addhour):

    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
  
    dt_string = datetime.today() + timedelta(hours= -localGmt +addhour)
    dt_string = dt_string.strftime("%Y-%m-%dT%H:%M:%S")+'-00:00'
        
    #print("date and time =", dt_string)
        


    return dt_string

