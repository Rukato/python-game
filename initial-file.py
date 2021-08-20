import  time
import requests
import sys

def main():
    # Maybe move this to the beginning 
    api_url_cat = "https://quotes.rest/qod/categories?language=en&detailed=false"
    response = requests.get(api_url_cat)

    #add error managment for the api calls
    if response.status_code == 200:
        list_of_cats = response.json()['contents']['categories']
    else:
        print("Quote service not available at the moment...sounds familiar, yeah but at least we're honest about it ;-p")
        sys.exit()

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

    # move to separete function
    print(get_message(chosen_cat, list_of_cats))

    print("Now take that in and breath, just breath")

def get_message(category, list_of_cats):
    message = ''
    author = ''

    if category in list_of_cats:    
        quote_response = requests.get("https://quotes.rest/qod?category={}&language=en".format(category.lower()))
        if quote_response.status_code == 200:
            message = quote_response.json()['contents']['quotes'][0]['quote']
            author = quote_response.json()['contents']['quotes'][0]['author']
        else: 
            print("Sorry kids, my advice guru has left to find themselves, but just remember to breath and watch the movie The Prom")
            sys.exit()
            
    else:
        message = "You choosed a non option...good on you! Now you get a tsk tsk from the programer, but at least your a free thinker"
        author = "Unknow Dev"

    return message + ' by ' + author

if __name__ == "__main__":
    main()