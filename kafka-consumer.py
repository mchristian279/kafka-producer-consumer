from kafka import KafkaConsumer
from json import loads

print('Kafka consumer starting...')

topic = 'topic-name'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers='server:port,server:port',
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='./cacert.pem',
    ssl_certfile='./certificate.pem',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group-id-name'
    )
# Read data from kafka
for message in consumer:
 print (message)

