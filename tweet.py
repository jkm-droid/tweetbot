#tweetbot/tweet.py

import tweepy
import logging
import time
import random
from config import create_api

#logging logic
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

"""read keywords randomly from a file"""
"""return a single random keyword"""
def get_random_keyword():
	lines = open('keywords.txt').read().splitlines()
	keyword = random.choice(lines)

	return keyword

"""get random subjects from a file"""
"""return the random subject"""
def get_random_subject():
	lines = open('subjects.txt').read().splitlines()
	subject = random.choice(lines)

	return subject

"""function to get random headings from a file"""
"""and return a random heading"""
def get_random_heading():
	lines = open('headings.txt').read().splitlines()
	heading = random.choice(lines)

	return heading

"""function for sending the tweet"""
def send_tweet(api):
	logger.info("Tweeting...")
	#get the generated keyword
	my_keyword = get_random_keyword()

	#get the generated subject
	my_subject = get_random_subject()

	#get the generated heading
	my_heading = get_random_heading()

	#embed the keyword in the tweet message
	my_tweet = f"{my_heading}.I guarantee quality work and timely delivery if assigned\n #essaypay\n#essayhelp \n#{my_keyword}\n#assignments\n#homeworkpay\n#homeworkhelp\n#homeworkslave\n#{my_subject}\n#assignmenthelp\n#homework\n#assignment\nKindly DM @Josh_the_writer"
	#send the tweet message
	api.update_status(status=my_tweet)

	logger.info("Tweet sent successfully")

	logger.info("sleeping...")

	#setting interval between tweets
	time.sleep(60)

"""function for creating the API"""
"""And sending the tweet"""
def main():
	api = create_api()

	while True:
		send_tweet(api)
		
if __name__ == "__main__":
	main()