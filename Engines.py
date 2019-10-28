import sys
sys.path.append("C:/Users/adity/Desktop/confidential")

from global_constants import *

from NewsEngine import *
from SocialEngine import *

twitterEngine = TwitterEngine(
    TWITTER_CONSUMER_KEY=TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET=TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN=TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET=TWITTER_ACCESS_TOKEN_SECRET)

newsEngine = NewsEngine(pageSize=1, NEWS_API_KEY=NEWS_API_KEY)