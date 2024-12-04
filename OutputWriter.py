from confluent_kafka import Producer
import json

class OutputWriter:
    def __init__(self, topic="transcribe_data", bootstrap_servers="kafka:9092"):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.topic = topic

    def write_output(self, key, data):
        try:
            diarized_string = []
            for segment in data["segments"]:
                # print(f"Cümle: {segment['text']} (Konuşmacı: {segment['speaker']})")
                speaker = segment["speaker"]
                text = segment["text"]
                diarized_string.append(f"- {speaker}: {text}\n")
            diarized_message = ''.join(diarized_string)
            print(f"Diarized message:\n{diarized_message}")

            # Kafka'ya mesaj gönder
            message = {"key": key, "value": diarized_message}
            self.producer.produce(self.topic, key=key, value=json.dumps(message))
            self.producer.flush()
            
            print(f"Message sent to Kafka topic '{self.topic}': {message}")
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")
