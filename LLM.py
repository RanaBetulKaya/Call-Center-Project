import os
from langchain_groq import ChatGroq
from prompts import prompt
from dotenv import load_dotenv
from pathlib import Path

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
    
    # Modelin ürettiği tahmin terminale yazdırılıyor.
    print(result)

    