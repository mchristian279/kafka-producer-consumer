<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" />

### To run the applications start here

### prerequisites
```text
- python3
- Kafka topic created
```
#### create python virtual environment to run
```sh
virtualenv virtual-environment-name
source ./virtual-environment-name/bin/activate
```
#### Install library dependencies
```sh
pip3 install -r requirements.txt
```
#### With the topic created in Kafka, point in the following variable to specify the desired topic
```python
# topic name
topic = 'topic-name'
```
#### specify the desired quantity of produced messages, in the "for i range(3)" of the "main" function. In this case range(3) will be the messages produced
```python
# Create data messages
def main():
      for i in range (3):
          # Generate Fake Data
          data = {
              'id': dataFake.random_int(min=20000, max=100000),
              'name': dataFake.name(),
              'address': dataFake.street_address() + ' | ' + dataFake.city() + ' | ' + dataFake.country_code(),
              'platform': random.choice(['phone', 'laptop', 'Tablet']),
              'date': str(dataFake.date_time_this_month())
          }
```
#### Start the producer
```sh
python3 kafka-producer.py
```
#### You can check the producer's execution log through the log file that will be generated
```text
producer.log
```
#### Start the consumer
```sh
python3 kafka-consumer.py
```

### If necessary, convert kafka.client.truststore.jks to cacert.pem and certificate.pem for Kafka authentication

# kafka-producer-consumer
### Convert kafka.client.truststore.jks to cacert.pem and certificate.pem

### 1 - export the cacert from the kafka.client.truststore.jks file
```bash
keytool -list -rfc -keystore kafka.client.truststore.jks -storepass pass-kafka.client.truststore | awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/ {print $0}' > cacert.pem
```
### 2 - List kafka.client.truststore.jks to query the "Alias name" to generate the certificate.pem
```bash
keytool -list -rfc -keystore client.truststore.jks
```
### 3 - Use the "Alias name" listed above and then export the certificate certificate.pem
```bash
keytool -exportcert -alias root-users.pem -keystore kafka.client.truststore.jks \
        -rfc -file certificate.pem
```
