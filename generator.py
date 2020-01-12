import string
import random

"""function to generate random string"""
"""consisting of letters and digits"""
def generate_random_token(stringLength=30):
	__gen_token = string.ascii_lowercase

	return ''.join(random.choice(__gen_token) for i in range(stringLength))

print(generate_random_token(30))

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString() )
print ("Random String is ", randomString(10) )
print ("Random String is ", randomString(10) )