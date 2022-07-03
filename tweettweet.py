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

# Get list of tweets on my home screen
# public_tweets = client.get_home_timeline()
# for tweet in public_tweets.data:
#     print(tweet.text)

# Print info on myself
# user = client.get_me()
# print(user.data.name)

# Get a list of my followers and follow them back
# user = client.get_me()
# print(user.data.id) # my user id
# for follower in client.get_users_followers(id=user.data.id).data:
#     print(follower)
#     client.follow_user(target_user_id=follower.id)

# Search tweets
query = 'python'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.data)
