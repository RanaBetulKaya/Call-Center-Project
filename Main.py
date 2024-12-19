import ray
from AudioProcessor import AudioProcessor
from ProducerWriter import ProducerWriter
from ConsumerReader import ConsumerReader
import time
import os
 
def get_audio_files(directory):
    print("buradayım")
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.wav')]
 
@ray.remote
def process_audio_file(audio_file):
    print(f"Running on node: {ray.util.get_node_ip_address()}")
    processor = AudioProcessor(audio_file)
    processor.load_models()
    return processor.process_audio()
 
def main():
    ray.init()
    print(ray.nodes())
    audio_directory = "/app/data_audio"
   
    audio_files = get_audio_files(audio_directory)
 
    if not audio_files:
        print("Ses dosyası bulunamadı.")
        return
 
    consumer = ConsumerReader()
    consumer.start()
 
    futures = [process_audio_file.remote(audio_file) for audio_file in audio_files]
    while len(futures):
        done_id, futures = ray.wait(futures)
        outputWriter = ProducerWriter()
        outputWriter.produce_message(ray.get(done_id[0])[0], ray.get(done_id[0])[1])
 
if __name__ == "__main__":
    main()