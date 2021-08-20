import  time
import requests

def main():
    print("Hi!")
    time.sleep(1)
    print('\n')
    print("I know life can be hard and frustating...")
    time.sleep(1)
    print("Mostly hard")
    time.sleep(1)
    print("But you're not alone!")
    time.sleep(1)
    print("Let me give you a bit of good advice")
    print('\n')
    time.sleep(1)
    print("But first...")
    time.sleep(2)
    name = input("What's your name?  ")
    print("Hi " + name + "!")
    print('\n')

    api_url_cat = "https://quotes.rest/qod/categories?language=en&detailed=false"
    response = requests.get(api_url_cat)

    list_of_cats = response.json()['contents']['categories']

    print('Let\'s see what tickles your fancy')
    time.sleep(1)
    print('\n')
    print('Choose one of the following...')
    for category in list_of_cats:
        print(category.capitalize())
        time.sleep(0.5)
    
    chosen_cat = input("What do you choose?  ")

    print("Ok, just a second....(imagine Jeopardy song plaing, R.I.P. Alex)")
    time.sleep(1.5)

    message = ''
    author = ''

    if chosen_cat.upper() == "INSPIRE":
        quote_response = requests.get("https://quotes.rest/qod?category=inspire&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "MANAGEMENT":
        quote_response = requests.get("https://quotes.rest/qod?category=management&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "SPORTS":
        quote_response = requests.get("https://quotes.rest/qod?category=sports&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "LIFE":
        quote_response = requests.get("https://quotes.rest/qod?category=life&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "FUNNY":
        quote_response = requests.get("https://quotes.rest/qod?category=funny&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "LOVE":
        quote_response = requests.get("https://quotes.rest/qod?category=love&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "ART":
        quote_response = requests.get("https://quotes.rest/qod?category=art&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    elif chosen_cat.upper() == "STUDENTS":
        quote_response = requests.get("https://quotes.rest/qod?category=students&language=en")
        message = quote_response.json()['contents']['quotes'][0]['quote']
        author = quote_response.json()['contents']['quotes'][0]['author']
    else:
        message = "You choosed a non option...good on you! Now you get a tsk tsk from the programer, but atleast your a free thinker"
        author = "Unknow Dev"

    print(message + " by " + author)
    print("Now take that in and breath, just breath")

if __name__ == "__main__":
    main()