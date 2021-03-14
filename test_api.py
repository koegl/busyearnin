import os
import json
# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af


# THIS SCRIPT CREATES A JSON FILE WITH TWEETS IN A PREDEFINED SEARCH SPACE AND LOAD IT INTO A LIST OF DICTS

# set search parameters
max_results = 500000
since = "2021-01-01"
until = "2021-03-13"
account = "elonmusk"

# set save path
save_file = "musk_tweets.json"

# execute the twitter search through a shell command
# jsonl makes it save to a json file (otherwise you get links)
# progress prints progress updates in the terminal
# max-result is the maximum amount of results
# twitter search ios what is entered in the twitter search field

command = "snscrape --jsonl --progress --max-results {} --since {} twitter-search " \
          "\"from:{} until:{}\" > {}".format(max_results, since, account, until, save_file)

os.system(command)

# load saved tweets into a list (one element per tweet)
with open('musk_tweets.json', 'r') as myfile:
    contents = myfile.readlines()
    myfile.close()

# transform list into dict and create a list of dicts
tweets = []

for i in range(len(contents)):
    tweets.append(json.loads(contents[i]))

# reverse their order so they are from oldest to newest
tweets.reverse()

print(len(tweets))
