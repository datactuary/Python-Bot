from itertools import count
import tweepy
import config

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

########## Reading Tweets ##########
#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user.name} said {tweet.text}")

########## Twittear ##########
#api.update_status("Hamilton")

########## Information ##########
#user = api.get_user(screen_name='datactuary')
#print("User details:")
#print(user.name)
#print(user.description)
#print(user.location)
#print('')

#print("Last 20 Followers:")
#for follower in user.followers():
#    print(follower.name)

########## Follows Someone ##########
#api.create_friendship(screen_name="realpython")

########## Tweets Liker ##########
timeline = api.home_timeline(count=1)
tweet = timeline[0]
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
print(f"Liking tweet of {tweet.user.name}: {tweet.text}")
api.create_favorite(tweet.id)

########## Tweets Searcher ##########
#for tweet in api.search_tweets(q="iPhone", lang="es", count=2):
#    print("User: " f"{tweet.user.screen_name}")
#    print("Name: " f"{tweet.user.name}")
#    print("Tweet: " f"{tweet.text}")
#    print("")

########## Trends ##########
#trends_result = api.get_place_trends(1) #1 means World-wide
#for trend in trends_result[0]["trends"]:
#    print(trend["name"])
