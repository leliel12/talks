from pprint import pprint

from infopython import session
from infopython.isources import twitteruser

session.set(compete_key = "5h88328y8wchp8gf8bgt4fx9",
            twitter_key = "X8yUKlPyHmfMRQpV2gXWg",
            twitter_secret = "71Q3lqNMlEEnSpa10ynmKTXiuQxB0Yg051vecVWzOPc",
            twitter_user_key = "57517417-V1F43HjYyad6HlaQqFpXrtAre3dbJPM9F56rcZI03",
            twitter_user_secret = "DOMLETmR9XSEbb45l8fc5OGDsInbusP0wJd18dVQk",
            klout_api_key = "d6zu25pnvf7ppz99925sg5xj")
            
yo = twitteruser.TwitterUser("leliel12")

print "ID> " + yo.id
print "Username> " + yo.username
print "Tweepy>"
pprint(yo.get_info("tweepy"))





