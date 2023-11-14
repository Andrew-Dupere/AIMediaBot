import secrets
import tweepy

def postFunc(content):

    consumer_key = secrets.consumer_key
    consumer_secret = secrets.consumer_secret
    access_token = secrets.access_token
    access_token_secret = secrets.access_token_secret

    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    #https://docs.tweepy.org/en/stable/client.html#manage-tweets
    response = client.create_tweet(
        text=content
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")




