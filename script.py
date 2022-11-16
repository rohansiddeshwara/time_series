import requests
import schedule


url="http://127.0.0.1:8000/"

def get_daily(url):
    r=requests.get(url)
    data=r.json()
    with open("data_daily.txt","a") as f:
        f.write(str(data)+"\n")

def get_weekly(url):
    r=requests.get(url)
    data=r.json()
    with open("data_weekly.txt","a") as f:
        f.write(str(data)+"\n")

if __name__=="__main__":
    scheduler1 = schedule.Scheduler()
    scheduler1.every().day.at("09:00").do(get_daily,url)
    scheduler1.every().day.at("17:00").do(get_daily,url)
    while True:
        schedule.run_pending()
