# Call-Center-Project

<h1>Adımlar</h1>

<h4> 1.Adım </h4>
<p> Groq API Key alarak .env dosyasına eklenmeli </p>

<h4> 2.Adım </h4>
<p> requirements.txt dosyasındaki gereklilikleri indir. </p>

<h4> 3.Adım </h4>
<p> ffmpeg modülünü system-wide olarak install et. </p>

<h4> 4.Adım </h4>
<p> docker compose up --build -d ile kafkayı ayağa kaldır </p>

<h4> 5.Adım </h4>
<p> python Main.py ile projeyi başlat </p>

<h2> Pipeline Architecture </h2>
<p align="center">
  <img src="pipeline/pipeline.png" width="450" title="hover text">
</p>

<h2> NOT </h2>
<p> Audio2Text.py dosyasında zaten belirttim. Whisperx modelini cpu da çalıştırmak biraz uzun dürüyor. Sisteme göre değişiklik yapılabilir </p>
