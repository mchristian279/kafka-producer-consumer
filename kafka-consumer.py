from kafka import KafkaConsumer
from json import loads
import random

#Generate ID Consumer-Group
id = random.randint(1,1000)

#Name Consumer-Group Kafka
consumer_group = ('consumer-group-name-'+str(id))

print('Kafka Starting...')

topic = 'topic-name'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers='server:port,server:port,
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='./cacert.pem',
    ssl_certfile='./certificate.pem',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=consumer_group
)
# Read data from kafka
for message in consumer:
    print(message)
