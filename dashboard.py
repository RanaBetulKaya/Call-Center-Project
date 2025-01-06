import json, time
import streamlit as st
import plotly.graph_objects as go
from PredictConsumer import read_messages
 
def wrap_text(text, max_length):
    words = text.split()
    wrapped_text = ""
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > max_length:
            wrapped_text += line.strip() + "<br>"
            line = word + " "
        else:
            line += word + " "
    wrapped_text += line.strip()
    return wrapped_text
 
def app(message,key):
   
    data = message['detay']# Seçilen diyaloga ait verileri alır.
    print(data)
    # Diyalog verilerini işleme
    # print(message)
    # print(type(message))
    timestamps = list(range(len(data)))  # Her cümleye bir zaman damgası atıyor  # Konuşmacıyı belirle
    values = list(item["sentiment"] for item in data)
    print(values)
    sentences = list(item["sentence"] for item in data)
    print(sentences)
    y_values = [1 if item["speaker"] == "SPEAKER_01" else -1 for item in data] # Konuşmacıya göre y ekseni değerini belirliyor
    print(y_values)
    colors = ["green" if value > '0' else "red" for value in values]  # Değerlere göre çubuk renklerini belirliyor
    print(colors)
 
    hovertext = [
    f"{wrap_text(sentences[i], 50)}"
    for i in range(len(sentences))
    ]
    # Grafik oluşturma
    fig = go.Figure()  # Yeni bir grafik objesi oluşturuyor
 
    # Çubuklar için verileri ekleme
    for i in range(len(sentences)):
        fig.add_trace(go.Bar(
            x=[timestamps[i]],  # x ekseni değerleri
            y=[y_values[i]],  # y ekseni değerleri
            marker_color=colors[i],  # Çubuk rengi.
            hovertext=hovertext[i],
            width=0.5  # Çubuk genişliği.
        ))
 
    # Grafik boyutlandırma ve eksen ayarları
    num_timestamps = len(timestamps)  # Zaman damgası sayısını alıyor.
    width = 1000 # Grafik genişliğini hesap.
 
    fig.update_layout(
        title=f"Dosya {message['key']} - Konu: {message['konu']} - Genel Duygu: {message['duygu']}",  # Grafik başlığı.
        xaxis_title="Zaman",  # x ekseni başlığı.
        yaxis_title="SPEAKER_00 (-)<-------->SPEAKER_01 (+)",  # y ekseni başlığı.
        xaxis=dict(tickvals=timestamps),  # x ekseni değerlerini ayarlıyor
        yaxis=dict(
            tickvals=[-1, 0, 1],  # y ekseni aralıklarını ayarlıyor
            ticktext=["<b>-1 (SPEAKER_00)<b>", "0", "<b>1 (SPEAKER_01)<b>"]  # y ekseni metinlerini belirliyor
        ),
        showlegend=False,  
        bargap=0.5,  # Çubuklar arası boşluk
        width=width,  # Grafik genişliği.
        height=600  # Grafik yüksekliği.
    )
 
    st.plotly_chart(fig,key)  # Grafik nesnesini Streamlit'te görüntülüyor.
    
 
#confluent kafkadan gelen veriler streamlite gönderiliyor
st.title("Çağrı Analizi")
key = 0

for message in read_messages():
    print(message)
    print(type(message))
    time.sleep(5)
    app(message,key)
    key = key+1


 
 