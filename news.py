import requests 

#sports sources 
sports_sources = ['bbc-sport', 'bleacher-report', 'espn', 'espn-cric-info', 'four-four-two', 'fox-sports']
tech_sources = ['engadget', 'hacker-news', 'recode']
general_sources = ['google-news', 'abc_news', 'cbc-news', 'google-news-ca']
categories = ['business', 'entertainment', 'general', 'science', 'sports', 'technology']
"""
# Example for api request for top headlines in the us
https://newsapi.org/v2/top-headlines?country=us&apiKey=80e76045083d4f898a4e51b5502346ea

q: Keywords or a phrase to search for.
"""
def News(user):
    loopagain = True 
    while loopagain: 
        # Ask user to pick category for news
        print()
        print('Here are some news categories: ')
        for item in categories:
            print(item.upper())
        user_in = input('Please pick a category from the above choices to find news for: ')
        while user_in.lower() not in categories:
            user_in = input('Please pick a valid category from the above choices to find news for: ')

    
        api_key = '80e76045083d4f898a4e51b5502346ea'

        url = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'.format(user._count, user_in, api_key)
    
        response = requests.get(url)

        resp_json = response.json()
        articles = resp_json['articles']
        print()
        for i in range(5):
            title = articles[i]['title']
            desc = articles[i]['description']
            print(title)
            print(desc)
            print()
        inpu = input("Would you like to find news in another category? y/n: ")
        while inpu.lower().strip() != 'y' and inpu.lower().strip() != 'n':
                inpu = input('Please enter a valid response. y/n: ')
                if inpu.lower().strip() == 'y' or inpu.lower().strip() == 'n':
                    break
        if inpu.lower().strip() == 'y':
            loopagain = True
        else:
            loopagain = False 
    print()
    print("https://newsapi.org - Powered by News API")