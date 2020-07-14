import requests
import json
import datetime
import random


previous = requests.get('https://api.spacexdata.com/v4/launches/latest')
previous_dict = previous.json()
response = requests.get('https://api.spacexdata.com/v4/launches/next')
response_dict = response.json()
launch_time = response_dict['date_utc']


def next_launch():
    return("The next SpaceX Launch is scheduled on " +
           response_dict['date_utc'] + '\n' + '\n' + response_dict['details'])


def previous_launch():
    return("The previous SpaceX Launch was on " +
           previous_dict['date_utc'] + '\n' + '\n' + previous_dict['details'])


def launch():
    return("Spacex goes brrrrrrrrrrrrr!")


def image():
    image = previous_dict['links']['flickr']['original']
    random_sel = random.randint(0, len(image)-1)
    return(image[random_sel])
    # print(random_sel)


image()
