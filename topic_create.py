from kafka import KafkaAdminClient, NewTopic

# Set the following variables as appropriate
bootstrap_servers = ['localhost:9092']
topic_name = 'my-topic'
num_partitions = 3
replication_factor = 1

# Create the KafkaAdminClient object
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Create the NewTopic object
topic = NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

# Call the create_topics method to create the topic
admin_client.create_topics(new_topics=[topic])

# Close the KafkaAdminClient
admin_client.close()
