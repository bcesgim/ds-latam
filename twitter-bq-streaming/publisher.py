import tweepy

import settings
from streamer import TweetStreamListener


def publish_twitter_stream():
    auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
    auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
    api = tweepy.API(auth)

    stream_listener = TweetStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=['datos'])


if __name__ == '__main__':
    publish_twitter_stream()
