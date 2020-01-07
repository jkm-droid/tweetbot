#vainbot/bots/rconfig.py
import tweepy
import logging
from os import environ

logger = logging.getLogger()

def create_api():
	#declaring the required keys and tokens
	API_KEY = "luovbsfjIwtPQDpmmHiWbPzFB"
	API_SECRET_KEY = "X7ywyWZvQrQW6ksCjoicDY1H7LLl7PozUIxqkY9p3ca8KEBf24"
	ACCESS_TOKEN = "3356774219-Xmu4eAQiJUVipT6tBGkMiE8HDCOTjneVb5dBRnI"
	ACCESS_SECRET_TOKEN = "0UJPZn5zkrz466pZm4aRxukjPc0QTEJOOqDHREUceV3ft"

	#Authenticating to twitter account
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

	#creating API object
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	try:
		api.verify_credentials()
		username = api.me()
	except Exception as e:
		logger.error("Error creating API", exc_info=true)
		raise e

	logger.info("API created")
	logger.info(username.name)

	return api
