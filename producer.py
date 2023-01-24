import requests
import schedule
from kafka import KafkaProducer
import json

# Set the following variables as appropriate
bootstrap_servers = ['localhost:9092']
topic_name = 'my-topic'

# Create the KafkaProducer object
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

url="http://127.0.0.1:8000/"

def get_daily(url):
    r = requests.get(url)
    data=r.json()
    json_str=json.dumps(data)
    # Send the data to the Kafka topic
    producer.send(topic_name, str(json_str).encode('utf-8'))
    print(data)
    with open("data_daily.txt","a") as f:
        f.write(str(data)+"\n")

def get_weekly(url):
    r=requests.get(url)
    data=r.json()
    with open("data_weekly.txt","a") as f:
        f.write(str(data)+"\n")

if __name__=="__main__":
    # scheduler1 = schedule.Scheduler()
    schedule.every(10).seconds.do(get_daily,url)
    # scheduler1.every().day.at("10:00").do(get_daily,url)
    # scheduler1.every().day.at("17:00").do(get_daily,url)
    while True:
        schedule.run_pending()
