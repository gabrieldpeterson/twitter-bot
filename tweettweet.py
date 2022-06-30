import tweepy

key_text = 'key.txt'
keys = []

with open(key_text) as f:
    keys = f.read().splitlines()

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]
bearer_token = keys[4]

client = tweepy.Client(
    bearer_token, consumer_key, consumer_secret, access_token, access_token_secret
)

# public_tweets = client.get_home_timeline()
# for tweet in public_tweets.data:
#     print(tweet.text)

user = client.get_me()
print(user.data.name)