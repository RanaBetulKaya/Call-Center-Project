import os
from langchain_groq import ChatGroq
from prompts import prompt
from dotenv import load_dotenv
from pathlib import Path
from LLMtoProducer import LLMtoProducer
from PredictConsumer import PredictConsumer
import json
 
 
# Prediction yapan LLM fonksiyonu
def llm_service(message):
    load_dotenv(Path(".env")) # Groq API Key .env dosyasından yükleniyor.
    llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )  
    # full_prompt, prompt dosyasındaki kurallara ve örneklere göre topic' ten
    # alınan message ile birleştirilmiş halidir.
    full_prompt = f"{prompt}\nÖrnek: {message}\nYanıt:"
   
    # langchain kullanıldığı için .invoke ile modele prompt veriliyor.
    result = llm.invoke(full_prompt)
    
    content = result.content  # content'e bu şekilde erişim sağlayabilirsiniz.
    # print(content)
    consumer = PredictConsumer()
    consumer.start()
    try:
    # Markdown işaretlerini temizle, yeni satır karakterlerini kaldır
        content = content.replace('```json\n', '').replace('```', '').strip()  # Markdown işaretlerini kaldır
        content = content.replace("\n", "").strip()  # Satır sonu karakterlerini kaldır
        json_object = json.loads(content)
        
        producer = LLMtoProducer()
        producer.produce_message(json_object)

    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        print(f"Invalid Content: {repr(content)}")  # İçeriği detaylı görmek için
    