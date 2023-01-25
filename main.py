import schedule
import time
import requests

def schedule_a_tiktok():
    # schedule a tiktok
    pass

def schedule_a_ig_reel():
    # schedule an ig reel
    pass

def schedule_a_yt_short():
    # schedule a yt short
    pass

def test_schedule():
    schedule.every(5).seconds.do(lambda: print_test("Hello world"))
    schedule.every().day.at("00:08").do(lambda: test_job_that_executes_once("It's 12:08 am"))
    
def print_test(text):
    print(text)
    print()

def test_job_that_executes_once(arg):
    print(arg)
    return schedule.CancelJob

test_schedule()

while(True):
    schedule.run_pending()
    time.sleep(1)