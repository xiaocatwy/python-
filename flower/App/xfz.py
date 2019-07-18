from kafka import KafkaConsumer
consumer=KafkaConsumer('world',group_id='consumer-20171017',bootstrap_servers=['127.0.0.1:9092'])
for msg in consumer:
    recv = "%s:%d:%d:value=%s" %(msg.topic,msg.partition,msg.offset,msg.value)
    print(recv)