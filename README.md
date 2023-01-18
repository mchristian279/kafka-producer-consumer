<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" />

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