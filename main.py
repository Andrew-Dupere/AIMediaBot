import secrets
import WorkingTextTweet
import yahooScraper
import gptprompt


mediaHeadlines = yahooScraper.yahoo()
role = 'sarcastic comedian'

tweet = gptprompt.gptCompletions(role,f'Here is a list of headlines {mediaHeadlines}, pick one list item and make a hilarious twitter post about the headline') 

WorkingTextTweet.postFunc(tweet)

