import secrets
import WorkingTextTweet
import yahooScraper
import gptprompt
import newsAPI
import time


# mediaHeadlines = yahooScraper.yahoo()
stockObject = newsAPI.dataPull()



role = 'Financial Analayst/Journalist writing cynical but funny tweets about the market'


#tweet = gptprompt.gptCompletions(role, f'Here is a list of headlines {mediaHeadlines}, pick one list item and make a hilarious twitter post about the headline') 


for item in stockObject:

    tweet = gptprompt.gptCompletions(role, f'write an a twitter post about this: f{item},keep the character limit below 280')

    WorkingTextTweet.postFunc(tweet.strip('"'))
    
    time.sleep(180)
    print(f'tweet about {item} sent')
    

