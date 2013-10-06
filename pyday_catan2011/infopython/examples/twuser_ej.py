from pprint import pprint

from infopython import session
from infopython.isources import twitteruser

session.set(compete_key = "",
            twitter_key = "",
            twitter_secret = "",
            twitter_user_key = "",
            twitter_user_secret = "",
            klout_api_key = "")
            
yo = twitteruser.TwitterUser("leliel12")

print "ID> " + yo.id
print "Username> " + yo.username
print "Tweepy>"
pprint(yo.get_info("tweepy"))







