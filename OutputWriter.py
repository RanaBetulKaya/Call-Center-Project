from confluent_kafka import Producer
import json

class OutputWriter:
    def __init__(self, topic="transcribe_data", bootstrap_servers="kafka:9092"):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.topic = topic

    def write_output(self, key, value):
        try:
            message = {"key": key, "value": value}
            self.producer.produce(self.topic, key=key, value=json.dumps(value))
            self.producer.flush()
            print(f"Message sent to Kafka topic '{self.topic}': {message}")
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")
