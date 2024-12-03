import whisperx

class AudioProcessor:
    def __init__(self, model_name="base"):
        self.model = whisperx.load_model(model_name)

    def transcribe(self, audio_path):
        try:
            result = self.model.transcribe(audio_path)
            transcription = result.get("text", "")
            return transcription
        except Exception as e:
            print(f"Error during transcription: {e}")
            return None
