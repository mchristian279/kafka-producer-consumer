from kafka import KafkaProducer
from faker import Faker
import json
import logging
import random

print('Kafka producer starting...')

# Topic Name
topic = 'topic-name'

# Instance Fake Data Lib
dataFake = Faker()

# Log Producer File
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='produtor.log',
    filemode='w'
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Connection Kafka Brokers
producer = KafkaProducer(
    bootstrap_servers='server:port,server:port',
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='./cacert.pem',
    ssl_certfile='./certificate.pem',
    # ssl_keyfile='key.pem'
)


# Callback Success
def send_success(record_metadata):
    print('topic:', record_metadata.topic)
    print('partition:', record_metadata.partition)
    print('offset:', record_metadata.offset)


# Callback Error
def send_error(excp):
    log.error('ERROR', exc_info=excp)


# Create Data Messages
def main():
    for i in range(3):
        # Generate Fake Data
        data = {
            'id': dataFake.random_int(min=20000, max=100000),
            'name': dataFake.name(),
            'address': dataFake.street_address() + ' | ' + dataFake.city() + ' | ' + dataFake.country_code(),
            'platform': random.choice(['celular', 'notebook', 'Tablet']),
            'date': str(dataFake.date_time_this_month())
        }
        # Push Data in Topic
        producer.send(topic, json.dumps(data).encode("utf-8")).add_callback(send_success).add_errback(send_error)
        producer.flush()
        logger.info(producer)
        print(json.dumps(data))


if __name__ == '__main__':
    main()
