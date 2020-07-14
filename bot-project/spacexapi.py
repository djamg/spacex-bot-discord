import requests
import json
import datetime
import random


previous = requests.get('https://api.spacexdata.com/v4/launches/latest')
previous_dict = previous.json()
response = requests.get('https://api.spacexdata.com/v4/launches/next')
response_dict = response.json()
launch_time = response_dict['date_utc']
gif_headers = {'api_key': 'UhaP5FUKjYe5ExMyQXpeOvXAGCtE1m43',
               'tag': 'spacex, nasa, isro, spaceshuttle, blueorigin, astronaut'}
gif_url = 'http://api.giphy.com/v1/gifs/random'


def next_launch():
    return("The next SpaceX Launch is scheduled on " +
           response_dict['date_utc'] + '\n' + '\n' + response_dict['details'])


def previous_launch():
    return("The previous SpaceX Launch was on " +
           previous_dict['date_utc'] + '\n' + '\n' + previous_dict['details'])


def launch():
    return("Spacex")


def image():
    image = previous_dict['links']['flickr']['original']
    random_sel = random.randint(0, len(image)-1)
    return(image[random_sel])
    # print(random_sel)


def launch_image():
    launch_image_list = ['https://media.giphy.com/media/l41JXjfuTR3NLKrwQ/giphy.gif',
                         'https://media.giphy.com/media/3oEhn501TH1S2NZATS/giphy.gif',
                         'https://media.giphy.com/media/3o6Ztc4jOYa24WDhq8/giphy.gif',
                         'https://media.giphy.com/media/f5ju9E432hCYFF9vnK/giphy.gif']
    return(random.choice(launch_image_list))


def random_gif():
    gif_response = requests.get(gif_url, gif_headers)
    gif_dict = gif_response.json()
    return(gif_dict['data']['images']['downsized']['url'])


random_gif()
