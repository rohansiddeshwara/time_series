from kafka import KafkaConsumer
from json import loads
import json
import pandas as pd
import ast
import pymongo
from pymongo import MongoClient

# Set the following variables as appropriate
bootstrap_servers = ['localhost:9092']
topic_name = 'my-topic'

# Connect to MongoDB Atlas

client = pymongo.MongoClient("mongodb+srv://rohansiddeshwara:dhY6Y4jS87h0UEhA2R7CHK9H545qvxM1D02pF5ifr1R2sPpXpGmqFbgSVBl6CrXW@test.npowlfj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection = db["INFY"]

# Create the KafkaConsumer object
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Continuously poll for new messages and insert them into MongoDB
for message in consumer:
    # Parse the message
    price_data = message.value.decode('utf-8')
    price_data = json.loads(price_data)
    # Insert the data into MongoDB
    collection.insert_one(price_data)

# Close the KafkaConsumer
consumer.close()
