import schedule
import time


def job():
    print("I'm working...")


schedule.every(1).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("17:12").do(job)
schedule.every().minute.at(":17").do(job)


def run():
    while True:
        schedule.run_pending()
        time.sleep(0.1)
