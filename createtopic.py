#Creates a topic in the server to publish messages

SERVER = 'localhost:9092'

from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers= SERVER, client_id='test')
topic_list = []
topic = input("Insert the topic name:")
topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
print("Topic", topic, "created")
admin_client.create_topics(new_topics=topic_list, validate_only=False)
