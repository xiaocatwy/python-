from kafka import KafkaProducer
# 创建生产者
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(3) :
    producer.send('bigdata01',b'Hello kafka')
producer.close()