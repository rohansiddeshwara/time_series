from kafka import KafkaConsumer
from json import loads
import json
import pandas as pd
import ast
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Set the following variables as appropriate
bootstrap_servers = ['localhost:9092']
topic_name = 'my-topic'

# Create the KafkaConsumer object
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# # Read messages from the Kafka topic
# for message in consumer:
#     with open("data_daily_consumer.txt","a+") as f:
#         test=message.value.decode('utf-8') 
#         f.write(test['lastPrice'])

# #
# fig, ax = plt.subplots()
# prices = [0.,]
# fig.canvas.draw()
# Continuously poll for new messages and update the chart
# for message in consumer:
#     # Parse the message and add the price to the list
#     price_data = message.value.decode('utf-8')
#     price_data=json.loads(price_data)
#     price = price_data['lastPrice']
#     prices.append(price)
    
#     # Update the chart with the new data
#     # ax.plot(prices)
#     # fig.canvas.draw()
#     print(prices)

# Set up the matplotlib chart
fig, ax = plt.subplots()
prices = []

# Define the update function for the animation
def update(num):
    # Poll for new messages and update the chart
    for message in consumer:
        # Parse the message and add the price to the list
        price_data = message.value.decode('utf-8')
        price_data = json.loads(price_data)
        price = price_data['lastPrice']
        prices.append(price)
        
        # Update the chart with the new data
        ax.plot(prices)
        break

# Set up the FuncAnimation object
ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()

# Close the KafkaConsumer
consumer.close()



    