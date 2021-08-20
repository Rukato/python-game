import  time
import requests

def main():
    print("Hi!")
    time.sleep(1)
    print("I know life can be hard and frustating...")
    time.sleep(1)
    print("Mostly hard")
    time.sleep(1)
    print("But you're not alone!")
    time.sleep(1)
    print("Let me give you a bit of good advice")
    time.sleep(1)
    print("But first...")
    time.sleep(2)
    name = input("What's your name?  ")
    print("Hi " + name + "!")

    api_url_cat = "https://quotes.rest/qod/categories?language=en&detailed=false"
    response = requests.get(api_url_cat)
    print(response.json()['contents'])
    
    for category in response.json()['contents']['categories']:
        print(category)

if __name__ == "__main__":
    main()