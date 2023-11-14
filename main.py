import secrets
import WorkingTextTweet
import yahooScraper
import gptprompt


mediaHeadlines = yahooScraper.yahoo()
role = 'you are a soviet era comediam writing twitter posts and you do not talk about Trump, or people that are sick or dying'

tweet = gptprompt.gptCompletions(role,f'Here is a list of headlines from the news {mediaHeadlines}, pick one list item as a topic and make a funny comment about it as a twitter post') 

WorkingTextTweet.postFunc(tweet)

