#tweetbot/tweet.py

import tweepy
import logging
import time
import random
from config import create_api
from datetime import datetime

#logging logic
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

"""read keywords randomly from a file"""
"""return a single random keyword"""
def get_random_keyword():
	open_file = open('keywords.txt').read().splitlines()
	keyword = random.choice(open_file)

	return keyword

"""get random subjects from a file"""
"""return the random subject"""
def get_random_subject():
	open_file = open('subjects.txt').read().splitlines()
	subject = random.choice(open_file)

	return subject

"""function to get random headings from a file"""
"""and return a random heading"""
def get_random_heading():
	open_file = open('headings.txt').read().splitlines()
	heading = random.choice(open_file		)

	return heading

"""function for sending the tweet"""
def send_tweet(api):
	logger.info("Tweeting...")
	#get the generated keyword
	my_keyword = get_random_keyword()

	#get the generated subject
	my_subject = get_random_subject()

	#get the generated headinga`1
	my_heading = get_random_heading()

	#embed the keyword in the tweet message
	my_tweet = "{my_heading} I guarantee quality work, original content and timely delivery.\n#essaypay\n#essayhelp \n#{my_keyword}\n#assignments\n#homeworkpay\n#homeworkhelp\n#homeworkslave\n#{my_subject}\n#assignmenthelp\n#homework\nKindly DM @Josh_the_writer".format(my_heading=my_heading, my_keyword=my_keyword,my_subject=my_subject)

	#send the tweet message
	logger.info("sending tweet...")
	
	api.update_status(status=my_tweet)

	logger.info("Tweet sent successfully")

	#save the tweets posted to a file
	logger.info("saving tweet...")

	current_data_time = datetime.now()
	date = current_data_time.strftime("%Y-%m-%d %H:%M")

	with open("logs.txt", 'a') as f:
		f.write(f"\nPosted on {date} \n\n")
		f.write(my_tweet)
		f.write("\n\n************************************************************************************\n")
		f.close()

	logger.info("Tweet saved successfully")

	logger.info("sleeping...")

	#setting interval between tweets
	time.sleep(600)

"""function for creating the API"""
"""And sending the tweet"""
def main():
	api = create_api()
	#send_tweet()
	while True:
		send_tweet(api)
		
if __name__ == "__main__":
	main()