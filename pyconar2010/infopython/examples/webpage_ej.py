from pprint import pprint

from infopython import session
from infopython.isources import webpages

session.set(compete_key = "",
            twitter_key = "",
            twitter_secret = "",
            twitter_user_key = "",
            twitter_user_secret = "",
            klout_api_key = "")
            
google = webpages.WebPage("google.com")

print "ID> " + google.id
print "URL> " + google.url
print "HTML>\n" + google.html

print "Compete>"
pprint(google.get_info("compete"))





