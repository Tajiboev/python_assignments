"""
Your task is to implement some basic functions to track live tweets and inspect their content
To complete this task and test it, you MUST have created a twitter account and you should now
your credentials: access_token, access_token_secret, consumer_key, consumer_secret

More info about the Twitter API at: https://dev.twitter.com/overview/api
"""

from twitter_streaming import TweetToFileListener
from time import sleep

from tweepy import OAuthHandler
from tweepy import Stream

import json


def get_tweet_stream(output_file, twitter_credentials):
    """
    This function is given and returns a "stream" to listen to tweets and store them in output_file
    To understand how this function works, check it against the code of twitter_streaming in part00_preclass

    :param output_file: the file where the returned stream will store tweets
    :param twitter_credentials: a dicionary containing the credentials to aceess twitter (you should have created your own!_
    :return: a "stream" variable to track live tweets
    """
    access_token = twitter_credentials['access_token']
    access_token_secret = twitter_credentials['access_token_secret']
    consumer_key = twitter_credentials['consumer_key']
    consumer_secret = twitter_credentials['consumer_secret']

    l = TweetToFileListener()
    l.set_output_file(output_file)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    return stream


def listen_and_store_tweets(keywords, duration, output_file, twitter_credentials):
    """
    This function tracks live tweets on a given topic for a certain duration and stores them in a file

    :param keywords: a list of keywords to track
    :param duration: the time the tracking will stay alive, e.g., 10 seconds
    :param output_file: the file where tweets will be stored
    :param twitter_credentials: a dictionary with credentials to access twitter
    """
    newStream = get_tweet_stream(output_file, twitter_credentials)
    newStream.filter(track=keywords, is_async=True) 
    sleep(duration)
    newStream.disconnect()
    pass


def count_tweets(output_file):
    """
    This function counts the number of tweets stored in output_file
    :returns the number of tweets in output_file
    """
    tweets_file = open(output_file, "r")

    # a list where we will store the tweets parsed from output_file
    tweet_list = []

    # Each line in the output file is a different tweet
    # Note that tweets in output file are interleaved by empty lines (that is, lines containing only the "\n" char)
    # This is line must be skipped (see "if" statement within the for loop)
    for line in tweets_file:
        if line is not "\n":
            # using json, we can parse each line into a dictionary "tweet"
            tweet_dict = json.loads(line)
            # store the dictionary representing each tweet in the tweet_list list
            tweet_list.append(tweet_dict)

    # always remember to close file when you don't need it
    tweets_file.close()
    return tweet_list.__len__()



# display the text and user info of tweets mae by users with more than follow_num followers
def show_tweets_high_followed_users(output_file, follower_num):
    """
    This function should print on console the tweets in output_file that have been tweeted by users with
    more than follower_num followers

    :param output_file: the file where tweets are stored
    :param follower_num: the minimum number of followers required to display a tweet
    :return:
    """
    tweets_file = open(output_file, "r")

    # a list where we will store the tweets parsed from output_file
    tweet_list = []

    # Each line in the output file is a different tweet
    # Note that tweets in output file are interleaved by empty lines (that is, lines containing only the "\n" char)
    # This is line must be skipped (see "if" statement within the for loop)
    for line in tweets_file:
        if line is not "\n":
            # using json, we can parse each line into a dictionary "tweet"
            tweet_dict = json.loads(line)
            # store the dictionary representing each tweet in the tweet_list list
            tweet_list.append(tweet_dict)

    # always remember to close file when you don't need it
    tweets_file.close()

    for tweet in tweet_list:
        if 'user' in tweet:
            if tweet['user']["followers_count"] > follower_num:
                print('printing @ high_followed_users\n',tweet) 

    
    pass


def listen_and_store_tweets_lan(keywords, duration, lan, output_file, twitter_credentials):
    """
    This function tracks live tweets on a given topic
    and in given languages for a certain duration and stores them in a file

    :param keywords: a list of keywords to track
    :param duration: the time the tracking will stay alive, e.g., 10 seconds
    :param lan: a list of languages to track, e.g. ['en', 'es', 'it'] tracks only tweets in English and Spanish (Espanol) and Italian
    :param output_file: the file where tweets will be stored
    :param twitter_credentials: a dictionary with credentials to access twitter
    """
    newStream = get_tweet_stream(output_file, twitter_credentials)
    newStream.filter(track=keywords, languages=lan, is_async=True) 
    sleep(duration)
    newStream.disconnect()
    pass


def load_props(prop_file):
    access_token, access_token_secret , consumer_key, consumer_secret = "", "", "", ""
    with open(prop_file, "r") as f:
        for line in f:
            l = line.split("=")
            if l[0] == "ACCESS_TOKEN":
                access_token = l[1].strip()
            elif(l[0] == "ACCESS_TOKEN_SECRET"):
                access_token_secret = l[1].strip()
            elif (l[0] == "CONSUMER_KEY"):
                consumer_key = l[1].strip()
            elif (l[0] == "CONSUMER_SECRET"):
                consumer_secret = l[1].strip()
    return access_token, access_token_secret , consumer_key, consumer_secret

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    access_token, access_token_secret, consumer_key, consumer_secret = load_props("api.txt")

    tweet_cred = {'access_token': access_token, 'access_token_secret': access_token_secret,
                  'consumer_key': consumer_key, 'consumer_secret': consumer_secret}

    """ UNCOMMENT line by line to text your functions"""

    listen_and_store_tweets(['trump', 'clinton'],2, "test_tweet.json", tweet_cred)

    print(count_tweets("test_tweet.json"), '= number of tweets')

    listen_and_store_tweets_lan(['trump', 'clinton'], 2, ['en', 'es', 'ko'], "test_tweet.json", tweet_cred)

    show_tweets_high_followed_users("test_tweet.json",7)