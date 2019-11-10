from publisher import publish_twitter_stream
from subscriber import receive_tweets


PROJECT_NAME = 'eventos-odsl'
PUBSUB_TOPIC_NAME = 'tweets'
SUBSCRIPTION_NAME = 'tweets-listener'


def main():
    publish_twitter_stream()
    receive_tweets(PROJECT_NAME, SUBSCRIPTION_NAME)


if __name__ == '__main__':
    main()
