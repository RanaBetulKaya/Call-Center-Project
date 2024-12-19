import ray
from Audio2Text import Audio2Text
from ProducerWriter import ProducerWriter
from ConsumerReader import ConsumerReader
import time
import os
 
# Dizindeki .wav dosyaları almak için kullanılan fonksiyon. 
def get_audio_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.wav')]
 
# Her bir ses dosyasını speakerlara ayırarak text' e dönüştürme işlemini yapacak fonksiyon.
# Ray ile paralelleştirme sağlanıyor. 
@ray.remote
def process_audio_file(audio_file):
    print(f"Running on node: {ray.util.get_node_ip_address()}")
    processor = Audio2Text(audio_file)
    processor.load_models()
    return processor.process_audio()
 
def main():
    ray.init() # ray başlatılıyor.
    
    audio_directory = "data" # ses dosyaları dizini
    audio_files = get_audio_files(audio_directory)
 
    if not audio_files:
        print("Ses dosyası bulunamadı.") # Eğer ses dosyası yoksa direkt çıkıyor
        return
 
    # Consumer nesnesi oluşturuluyor ve başlatılıyor
    consumer = ConsumerReader()
    consumer.start() 
 
    # ray ile işlenen ses dosyalarından dönen text sonuç için .remote ile futuresa aktarılıyor.
    futures = [process_audio_file.remote(audio_file) for audio_file in audio_files]
    
    # ray.wait toolu ile sürekli herhangi bir dosya için işlemin bitip bitmediğini kontrol ediyor
    # Böylece bütün dosyaların bitmesini beklemeden topice yollanabiliyor.
    while len(futures): 
        done_id, futures = ray.wait(futures)
        # Producer nesnesi oluşturuluyor ve message produce ediliyor
        outputWriter = ProducerWriter() 
        outputWriter.produce_message(ray.get(done_id[0])[0], ray.get(done_id[0])[1])
 
if __name__ == "__main__":
    main()