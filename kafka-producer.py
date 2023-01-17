from kafka import KafkaProducer
from faker import Faker
import json
import logging
import random

print('Kafka produtor starting...')

#Topic
topic = 'topic-name'

#Instance Fake Data Lib
dataFake = Faker()

#Log Producer File
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='producer.log',
    filemode='w'
    )
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Conection Kafka Brokers
producer = KafkaProducer(
    bootstrap_servers='server:port,server:port',
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='./cacert.pem',
    ssl_certfile='./certificate.pem'
    )

#Callback Sucess
def send_success(record_metadata):
    print('topic:', record_metadata.topic)
    print('partition:', record_metadata.partition)
    print('offiset:', record_metadata.offset)

#Callback Error
def send_error(excp):
    log.error('I am an errback', exc_info=excp)

#Create Data Messages
def main():
    for i in range(100):
        #Generate Data Fake
        data = {
            'id': dataFake.random_int(min=20000, max=100000),
            'name': dataFake.name(),
            'address': dataFake.street_address() + ' | ' + dataFake.city() + ' | ' + dataFake.country_code(),
            'platform': random.choice(['celular', 'notebook', 'Tablet']),
            'date': str(dataFake.date_time_this_month())
        }
        # Push Data in Topic
        inputMessage = producer.send(topic, json.dumps(data).encode("utf-8")).add_callback(send_success).add_errback(send_error)
        producer.flush()
        inputMessage
        logger.info(inputMessage)
        print(json.dumps(data))
if __name__ == '__main__':
    main()
