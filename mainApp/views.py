"""
Gryphon Web Crawler
Built with ❤
"""

from django.shortcuts import render
import time


def index(request):
    return render(request, "homepage.html")
    
def initialize():
    """
    Sets all of the variables for crawling,
    and as a result can be used for effectively resetting the crawler.
    """
    # Declare global variables
    global VERSION, START_TIME, START_TIME_LONG
    #global TODO_FILE, DONE_FILE, ERR_LOG_FILE
    global RESPECT_ROBOTS
    global TODO, DONE, THREAD_COUNT

    url_queue = []
    # Getting Arguments
    VERSION = '0.0.1'


def get_time():
    return time.strftime('%H:%M:%S')

def get_full_time():
    return time. strftime('%H:%M:%S, %A %b %Y')