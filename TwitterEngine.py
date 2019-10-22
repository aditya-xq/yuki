import tweepy


class TwitterEngine:
    def __init__(self, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                 TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET):
        self.TWITTER_CONSUMER_KEY = TWITTER_CONSUMER_KEY
        self.TWITTER_CONSUMER_SECRET = TWITTER_CONSUMER_SECRET
        self.TWITTER_ACCESS_TOKEN = TWITTER_ACCESS_TOKEN
        self.TWITTER_ACCESS_TOKEN_SECRET = TWITTER_ACCESS_TOKEN_SECRET

        self.auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,
                                        TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN,
                                   TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def doTweet(self, tweet):
        self.api.update_status(status=tweet)
        return []

    def deleteLatestTweet(self):
        latestTweetId = self.api.user_timeline(count=1)[0].id_str
        self.api.destroy_status(latestTweetId)
        return []