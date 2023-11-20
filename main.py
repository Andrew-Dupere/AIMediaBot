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

    tweet = gptprompt.gptClientCompletions('user', f'you are a cynical and funny financial analyst, write a less than 270 character twitter post about: {item}')

    WorkingTextTweet.postFunc(tweet.strip('"'))
    
    time.sleep(1800)
    
    

