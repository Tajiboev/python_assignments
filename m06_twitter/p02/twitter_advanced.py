"""
Your task today is to complete the functions below, which does some sort of simple information retrieval
from a stream of tweets stored in a file
# More info about the Twitter API at: https://dev.twitter.com/overview/api
"""

import json
from matplotlib import pyplot as plt


def most_followed_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user with most followers,
     the name of the user, and the user's number of followers
     (if the most followed user has tweeted more than once, the oldest tweet should be selected)
    :param output_file:
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
    most_followed_user_tweet = ''
    most_followers = 0

    for tweet in tweet_list:
        if 'user' in tweet:
            if tweet['user']["followers_count"] > most_followers:
                most_followed_user_tweet = tweet['text']
                most_followers = tweet['user']["followers_count"]
    print(most_followed_user_tweet)
    return most_followed_user_tweet


# extract tweet that hs been retweeted the most

def most_status_changes_user_tweet(output_file):
    """
    This function should print on console and return the tweet in output_file tweeted by the user that has tweeted
    the most since joining twitter.
     the name of the user, and the user's number of followers
     (if the most followed user has tweeted more than once, the oldest tweet should be selected)

    :param output_file:
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
    most_tweeted_users_tweet = ''
    most_changes = 0

    for tweet in tweet_list:
        if 'user' in tweet:
            if tweet['user']["statuses_count"] > most_changes:
                most_tweeted_users_tweet = tweet['text']
                most_changes = tweet['user']["statuses_count"]
    print(most_tweeted_users_tweet, f'{most_changes} statuses')
    return most_tweeted_users_tweet

# evaluate the lexical complexity of your twitter "corpus" using the metrics defined before
# tag and analyse tweets

def find_tweets_by_keyword(output_file, keyword_list):
    """
   This functions returns the tweets in outout_file that match one or more of the keywords in keyword_list
   It's up to you to define an appropriate datastore structure returned by this function

    :param output_file: a file containing tracked tweet(s)
    :param keyword_list: a list of keywords to search tweets
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
    
    matching_tweets = []

    for tweet in tweet_list:
        text = tweet['text']
        is_match = False
        for i in keyword_list:
            if i in text:
                is_match = True
                break
        if is_match:
            matching_tweets.append(text)

    print(matching_tweets)        
    return matching_tweets


def plot_tweets_by_attribute(output_file, attribute):
    """
    This functions plots a histogram of number of tweets per "attribute" in output_file.
    For instance, if attribute = "language", then it plots a histogram showing the number of tweets per language found;
    if attribute "location" it plots the number of tweets per different user location

    :param output_file:
    :param attribute: a categorical attribute meaningful for a tweet
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
    
    attributes = []

    for tweet in tweet_list:
        attributes.append(tweet[attribute])

    plt.style.use('fivethirtyeight')
    plt.hist(attributes)

    plt.title(f'Plot by {attribute}')
    plt.xlabel(attribute)
    plt.xlabel('Total')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':

    """ UNCOMMENT and COMPLETE AS REQUIRED"""

    # most_followed_user_tweet("test_tweet.json")               # Note the path to the file: .. is used to go up one level in the directory structure

    # most_status_changes_user_tweet("test_tweet.json")

    # find_tweets_by_keyword('test_tweet.json', ['Zelensky', 'Erdogan'])

    plot_tweets_by_attribute('test_tweet.json', 'lang')

