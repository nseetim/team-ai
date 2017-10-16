import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = input("Enter the Project name: ")
HOMEPAGE = input("Enter the url to the HomePage\n (Make sure you start with https:// or http://): ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = int(input("Enter the number of threads \n(this is OS specific as well as hardware specific"
                              "so ensure you know what your doing)"))

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
