import os
import ray
from AudioProcessor import AudioProcessor
from OutputWriter import OutputWriter
from KafkaConsumerReader import KafkaConsumerReader
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
    # Dosya dizini değiştirilmeli
    audio_directory = "/app/data"
    
    # Dizindeki tüm .wav dosyalarını al
    audio_files = get_audio_files(audio_directory)

    # Eğer dizinde ses dosyası yoksa bir mesaj yazdır
    if not audio_files:
        print("Ses dosyası bulunamadı.")
        return

    futures = [process_audio_file.remote(audio_file) for audio_file in audio_files]
        
    while len(futures):
        done_id, futures = ray.wait(futures)
        # file_name, transcription = os.path.basename(ray.get(done_id[0])), ray.get(done_id[0])
        # output_writer.write_output(file_name, transcription)
        outputWriter = OutputWriter()
        outputWriter.write_output(ray.get(done_id[0])[0], ray.get(done_id[0])[1])

    
    
if __name__ == "__main__":
    main()
