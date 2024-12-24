import threading
from confluent_kafka import Consumer
import json

class PredictConsumer:
    def __init__(self, topic="topics", bootstrap_servers="localhost:9092", group_id="group1"):
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
                message = msg.value().decode('utf-8')
                json_data = json.loads(message) 
                print(f"Received message")
                detay_count = len(json_data["detay"])
                print(detay_count)
                for item in json_data["detay"]:  # Direkt olarak item üzerinde iterasyon yapıyoruz
                    print("Konuşmacı:", item["speaker"])
                    print("Cümle: ", item["sentence"])
                    print("Duygu: ", item["sentiment"])
                # print(json_data)
                
        except KeyboardInterrupt:
            print("Stopped by user")
 
    def start(self):
        consumer_thread = threading.Thread(target=self.read_messages)
        consumer_thread.daemon = True  
        consumer_thread.start()
