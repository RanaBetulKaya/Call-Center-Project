from confluent_kafka import Producer
import json
 
class LLMtoProducer:
    def __init__(self, topic="topics", bootstrap_servers="localhost:9092"):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.topic = topic
 
    # Topic' e mesajı produce eden fonksiyon
    def produce_message(self, data):
        try:
            # Kafka'ya mesaj gönder
            self.producer.produce(self.topic,value=(json.dumps(data)).encode("utf-8"))
            self.producer.flush()
            # print(f"Message sent to Kafka topic '{self.topic}': {data}")
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")
           