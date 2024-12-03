# Call-Center-Project

<h1>Steps</h1>

<h4>Install the Ray</h4>
<p> pip install -U "ray[default]" </p>

<h4>Install WhisperX</h4>
<p> Also you should install WhisperX. You can check this link: https://github.com/m-bain/whisperX </p>

<h4>Start the Ray Cluster</h4>
<p> ray start --head </p>

<h4>Submit the jobs to cluster</h4>
<p> ray job submit --working-dir . -- python Main.py  </p>
