import threading
from confluent_kafka import Consumer
from LLM import llm_service
import json
 
class ConsumerReader:
    def __init__(self, topic="transcribe_data", bootstrap_servers="localhost:9092", group_id="group1"):
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
                print(f"Received message")
                
                # Okunan mesaj llm servisine yollanıyor.
                byte_key = msg.key()
                string_key = byte_key.decode('utf-8')
                print(type(string_key))
                llm_service(message, string_key)
                
        except KeyboardInterrupt:
            print("Stopped by user")
 
    def start(self):
        consumer_thread = threading.Thread(target=self.read_messages)
        consumer_thread.daemon = True  
        consumer_thread.start()