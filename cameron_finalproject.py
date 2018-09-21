#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:34:09 2018

@author: sarahcameron
"""
#import tweepy and datetime 
import tweepy
from tweepy import OAuthHandler 
import datetime


#twitter account dev info
consumer_key = 'scNrMjbb7Ki4AomckG2wo2MGy'
consumer_secret = 'UuXOUoBbORJ1QzDUKT66HFirva6W30bA0LdAfp3wosScBNCpda'
access_token = '1020103281123766272-WSBzbsAJBnmAKSmjIoLYq2A6AjAlRQ'
access_secret = 'RKv2deMZXix15lOggd8y8dxFDeN01U4y1xYkP6Umvoe2h'


#try to access Twitter API
def twitterAccess(key,secret,token,secret2):
 
    auth = OAuthHandler(key,secret)
    auth.set_access_token(token,secret2)
    
    try:
        api = tweepy.API(auth)
        print('api successful')
        
    except Exception as error:
        print(error,'wait a few minutes before trying to run the program. rate limit exceeded')
             
    return api

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
twitterAccess(consumer_key,consumer_secret,access_token,access_secret)    


num_words=[]
name=[]

#crime words to search for in tweets
word=['police','crime','jail','danger','arrest','shooting','road','traffic','death','penalty','fire','ambulance'
      'emergency','roads','traffic','cops','guns','news','warned','caution','injuries','firehouses','collision','collided',
      'accident','theft','robbery','stabbing']
len_word=len(word)


#initialize tweet, keyword and date dictionaries
tweet_dictionary={}
#{'user':'tweet'}
keyword_dictionary={}
#{user:keyword}
date_dictionary={}
#{user:date}

#loop through 200 tweets from the Twitter homepage. split() each tweet to loop through keywords
for status in tweepy.Cursor(api.home_timeline).items(200):
   alltweets=status.text
   data=[status.user.screen_name , status.text, status.created_at]
   username=data[0]
   tweet=data[1]
   date=str(data[2])
   date=date.split()
   date=date[0]
   tweet_split=tweet.split()
   tweet_len=len(tweet_split)

#loop through keywords and identify tweets that contain those keywords. Tweets containing keywords stored in tweet_dictionary
# tweets containing keywords stored in keword_dictionary and tweets that contained keywords dates are stored in date_dictionary
   for i in range(len_word):
       if word[i] in tweet_split:
           user=username
           name.append(user)
           tweet='_'.join(tweet_split)
         
           if user not in tweet_dictionary.keys():
               tweet_dictionary[user] = [tweet]
               keyword_dictionary[user]=[word[i]]
               date_dictionary[user]=[date]
           else:
              tweet_dictionary[user].append(tweet)
              keyword_dictionary[user].append(word[i])
              date_dictionary[user].append(date)

       else: 
           count=0
           user=0
 
 #get current date/time to compare to date/time of tweets        
now=datetime.datetime.now()
now=str(now)
now=now.split()
now=now[0]
   
#loop through dictionaries and print results. Result will show username and how many tweets were made from that user containing a keyword           
for key,value in keyword_dictionary.items():
    tweet_count=len(tweet_dictionary[key])
    date=set(date_dictionary[key])
    date=''.join(date)
    if date==now:
        time='today'
    else:
        time=('on',date)
    value=set(value)     
    if len(value)==1 and tweet_count==1:
        print(key,'tweeted containing the word',', '.join(value),tweet_count,'time',time)
        print("\n")
    elif len(value)>1 and tweet_count==1:
        print(key,'tweeted containing the words',', '.join(value),tweet_count,'time',time)
        print("\n")
    elif len(value)==1 and tweet_count>1:
        print(key,'tweeted containing the word',', '.join(value),tweet_count,'times',time)
        print("\n")
    elif len(value)>1 and tweet_count>1:
        print(key,'tweeted containing the words',', '.join(value),tweet_count,'times',time)
        print("\n")
 
    
# from results, the user can specify which username's tweet they want to display based on the above results.    
print()
print('find specific tweet:')    
    
user1=str(input('enter a username:    '))
keyword1=str(input('enter the matching keyword based on previous output:   '))
while user1 not in keyword_dictionary:
    user1=str(input('enter a valid username'))
    continue 
else:  

    class specificTweet:
        tweet_dictionary=tweet_dictionary
        def __init__(self,user,keyword):
            self.__user=user
            self.keyword= keyword
        
        def __repr__(self):
            str_user=str(self.__user)
            str_keyword=str(self.keyword)
            return 'user: ' + str_user + '  keyword: '+ str_keyword
    
        def __getDictionary(self,user):
            a=tweet_dictionary[user]
            return a
        
        
        def getTweet(self):
            a=self.__getDictionary(self.__user)      
            for i in range(0,len(a)+1):
                if self.keyword in a[i]:
                    return a[i]
                i+= 1   
 
    
                
tweet=specificTweet(user1,keyword1)  
answer=tweet.getTweet()  
print()
print('the tweet from username', user1,'containing the keyword', keyword1, 'is')
print()
print(answer)
        

# the username, keyword the user selected and the resulting tweet will be stored in a .txt file            
file1 = open("current_crime.txt","w")
text=('the tweet from username ' + user1 + ' containing the keyword ' + keyword1 + ' is:   ' + answer) 
file1.write(text)    
file1.close() 
        
        

   
   







