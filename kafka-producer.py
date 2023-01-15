from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random

print('Kafka Producer sendo inciado...')

#Data fake
dataFake = Faker()

#Log Producer
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#AWS config
#servers = "msk_broker_1:9096,msk_broker_2:9096"
# producer = Producer({
#     'bootstrap.servers':servers,
#     'security.protocol': 'SASL',
#     'sasl_plain_username': 'the_username',
#     'sasl_plain_password': 'the_password',
#     'sasl_mechanism': 'SCRAM-SHA-512'
# })

#Docker config
servers = "localhost:9092"
producer = Producer({
    'bootstrap.servers':servers})

#Callback messages
def posted(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Mensagem produzida no topico {} com o valor {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

#Create data messages
def main():
    for i in range(5):
        data={
           'id': dataFake.random_int(min=20000, max=100000),
           'nome':dataFake.name(),
           'endereco':dataFake.street_address() + ' | ' + dataFake.city() + ' | ' + dataFake.country_code(),
           'plataforma': random.choice(['celular', 'notebook', 'Tablet']),
           'data': str(dataFake.date_time_this_month())    
           }
        
        #Push data topic
        producer.poll(1)
        producer.produce('usuario-topico', json.dumps(data).encode('utf-8'),callback=posted)
        producer.flush()
        
if __name__ == '__main__':
    main()
