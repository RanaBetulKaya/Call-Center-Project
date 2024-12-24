import json
 
# Örnek Kafka verisi

 
# JSON verisini parse etme
def dialog_format(kafka_data):
    # Yeni formatta veri yapısı oluşturma
    dialogs = {
        kafka_data["key"]: {}  # Burada dialogs, bir sözlük olarak başlatılıyor
    }
    print(dialogs)
    
    # Detayları işleme
    for entry in kafka_data["detay"]:
        speaker = "SPEAKER_00" if entry["speaker"] == "Speaker_00" else "SPEAKER_01"
        sentence = entry["sentence"]
        sentiment = int(entry["sentiment"])
    
        # Anahtar değer çiftini ekleyin
        dialogs[kafka_data["key"]][f"{speaker}: {sentence}"] = sentiment
    
    # Sonuç
    print(dialogs)
    return dialogs