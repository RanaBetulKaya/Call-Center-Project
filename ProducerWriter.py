from confluent_kafka import Producer
import json

class ProducerWriter:
    def __init__(self, topic="transcribe_data", bootstrap_servers="localhost:9092"):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.topic = topic

    # Topic' e mesajı produce eden fonksiyon
    def produce_message(self, key, data):
        try: 
            diarized_message = diarized_message_dialog_format(data)
            print(f"Diarized message:\n{diarized_message}")

            # Kafka'ya mesaj gönder
            message = {"key": key, "value": diarized_message}
            self.producer.produce(self.topic, key=key, value=json.dumps(message))
            self.producer.flush()
            
            print(f"Message sent to Kafka topic '{self.topic}': {message}")
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")

# Diarize edilip text' e dönüştürülen mesajı, diyalog formatına getiren fonksiyon.
# Diyalog formatındaki text diarized_message arrayine ekleniyor.
def diarized_message_dialog_format(data):
    diarized_string = []
    for segment in data["segments"]:
        speaker = segment["speaker"]
        text = segment["text"]
        diarized_string.append(f"- {speaker}: {text}\n")
    diarized_message = ''.join(diarized_string)
    return diarized_message