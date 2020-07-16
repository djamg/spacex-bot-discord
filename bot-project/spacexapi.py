import requests
import json
import datetime
import random


gif_headers = {'api_key': 'UhaP5FUKjYe5ExMyQXpeOvXAGCtE1m43',
               'tag': 'spacex, nasa, isro, spaceshuttle, blueorigin, astronaut'}
gif_url = 'http://api.giphy.com/v1/gifs/random'
nasa_live = 'https://www.youtube.com/watch?v=21X5lGlDOfg'


def next_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/next')
    response_dict = response.json()
    launch_time = response_dict['date_utc']
    return("The next SpaceX Launch is scheduled on " +
           response_dict['date_utc'] + '\n' + '\n' + response_dict['details'])


def previous_launch():
    previous = requests.get('https://api.spacexdata.com/v4/launches/latest')
    previous_dict = previous.json()
    return("The previous SpaceX Launch was on " +
           previous_dict['date_utc'] + '\n' + '\n' + previous_dict['details'])


def launch():
    return("Spacex")


def image():
    previous = requests.get('https://api.spacexdata.com/v4/launches/latest')
    previous_dict = previous.json()
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


def isro():
    isro_image_list = ['https://www.isro.gov.in/sites/default/files/galleries/GSLV-F10%20/%20GISAT-1%20Gallery/logu6770.jpg',
                       'https://www.isro.gov.in/sites/default/files/galleries/GSLV-F10%20/%20GISAT-1%20Gallery/avp4964copy1.jpg',
                       'https://www.isro.gov.in/sites/default/files/galleries/GSLV-F10%20/%20GISAT-1%20Gallery/avp4741copy.jpg',
                       'https://www.isro.gov.in/sites/default/files/galleries/%E0%A4%9C%E0%A5%80.%E0%A4%8F%E0%A4%B8.%E0%A4%8F%E0%A4%B2.%E0%A4%B5%E0%A5%80.-%E0%A4%8F%E0%A4%AB10/%E0%A4%9C%E0%A5%80.%E0%A4%86%E0%A4%88.%E0%A4%B8%E0%A5%88%E0%A4%9F-1%20%E0%A4%A6%E0%A5%80%E0%A4%B0%E0%A5%8D%E0%A4%98%E0%A4%BE/007.jpg',
                       'https://yehaindia.com/wp-content/uploads/2019/09/isro.jpg',
                       'https://api.baliyans.com/apis/media/images/b7813c56-3b62-4542-a111-26dd6382ac8a_chandrayaan-2-7.jpg',
                       ]
    return(random.choice(isro_image_list))
