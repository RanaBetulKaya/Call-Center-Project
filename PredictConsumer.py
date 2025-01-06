from confluent_kafka import Consumer, KafkaException, KafkaError
import json
 
 
conf = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'grup3',                
    'auto.offset.reset': 'earliest'        
}
 
# Kafka Consumer oluşturma
consumer = Consumer(conf)
 
# Mesajları almak istediğiniz Kafka topic ismi
topic = 'topics'
 
consumer.subscribe([topic])
 
def read_messages():
    try:
        while True:
            msg = consumer.poll(timeout=5.0)
           
            if msg is None:
                continue  
           
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                   
                    print(f"End of partition {msg.partition} reached {msg.offset}")
                else:
                    raise KafkaException(msg.error())
            else:
                message = json.loads(msg.value().decode('utf-8'))
                yield message  
               
    except KeyboardInterrupt:
        print("Consumer stopped")
 
    finally:
        consumer.close()  