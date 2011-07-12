from pprint import pprint

from infopython import session
from infopython import agenda
from infopython.isources import webpages

session.set(compete_key = "",
            twitter_key = "",
            twitter_secret = "",
            twitter_user_key = "",
            twitter_user_secret = "",
            klout_api_key = "")

# ISources            
google = webpages.WebPage("google.com")
yahoo = webpages.WebPage("yahoo.com")

# Saca cosos
aud = lambda w: w.get_info("compete")["metrics"]["uv_count"]
imp = lambda w: w.get_info("pagerank")["pagerank"]

ag = agenda.AgendaSetting(itype=webpages.WebPage,
                          inf_sources=[google, yahoo],
                          audience_valuator=aud,
                          impact_valuator=imp)

ag.rank()

for i in ag:
    print i.id, "%s + %s = %s" % (i.audience, i.impact, i.value)
    







