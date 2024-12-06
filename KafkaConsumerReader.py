from confluent_kafka import Consumer
import json
import time

class KafkaConsumerReader:
    def __init__(self, topic="transcribe_data", bootstrap_servers="kafka:9092", group_id="group1"):
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })
        self.topic = topic
        self.consumer.subscribe([self.topic])

    def read_messages(self):
        print(f"Listening to Kafka topic '{self.topic}'...")
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue
                message = json.loads(msg.value())
                print(f"Received message: {message}")
        except KeyboardInterrupt:
            print("Stopped by user")

def main():
    time.sleep(10) 
    print("Consumer tanımlanıyor")
    consumer = KafkaConsumerReader()
    print("Fonk çağırılıyor")
    consumer.read_messages()
    
if __name__ =="__main__":
    print("ife girdi")
    main()