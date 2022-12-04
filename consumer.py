from kafka import KafkaConsumer
from json import loads
import json
import pandas as pd

consumer = KafkaConsumer("test", bootstrap_servers="localhost:9092", 
                            auto_offset_reset="earliest", enable_auto_commit=True,
                             group_id="my-group", 
                             value_deserializer=lambda x: loads(x.decode("utf-8")))

for message in consumer:
    message = message.value
    print(message)
    with open("data_daily.txt","a") as f:
        f.write(str(message)+"\n")