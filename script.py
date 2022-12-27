import tweepy
from utils import print_err, load_config, save_config
from functions import count_down
from logger_tool import Logger

config = load_config()
#config = load_config(file="_config.json")

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_secret = config['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

'''
Username: _slightlyTechie
Access Token:
Access Token Secret:
'''

auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

if __name__ == '__main__':

    try:
        data = load_config('data.json')
        data, message = count_down(data)
        Logger.info(f"DATA: {data}")
        Logger.info("Message: ", message)
        if message:
            api.update_status(message)
        save_config(data, "data.json")
    except Exception as e:
        print_err(e)
