import os
import ray
from AudioProcessor import AudioProcessor
from OutputWriter import OutputWriter

def get_audio_files(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist. Skipping audio file processing.")
        return []
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.wav')]

def main():
    audio_directory = "/Users/cansuoksel/Downloads/Call-Center-Project/data"
    audio_files = get_audio_files(audio_directory)
    if not audio_files:
        print("No audio files found. Exiting.")
        return

    ray.init()

    futures = []
    processor = AudioProcessor()
    output_writer = OutputWriter()

    for audio_file in audio_files:
        futures.append(ray.remote(processor.transcribe).remote(audio_file))

    while len(futures):
        done_id, futures = ray.wait(futures)
        file_name, transcription = os.path.basename(ray.get(done_id[0])), ray.get(done_id[0])
        output_writer.write_output(file_name, transcription)

if __name__ == "__main__":
    main()
