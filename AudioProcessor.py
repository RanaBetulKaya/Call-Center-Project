import whisperx
import os
import datetime
import torch
print(torch.backends.mps.is_available())

class AudioProcessor:
    def __init__(self, audio_file, device="cpu", batch_size=64, compute_type="int8"):
        self.audio_file = audio_file
        self.device = device
        self.batch_size = batch_size
        self.compute_type = compute_type
        self.model = None
        self.diarize_model = None

    def load_models(self):
        print("model yükleme başladı ", datetime.datetime.now())
        self.model = whisperx.load_model(
            "small",
            self.device, 
            compute_type=self.compute_type,
            
        )
        self.diarize_model = whisperx.DiarizationPipeline(
            use_auth_token="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",
            device=torch.device('cpu'),
            model_name="pyannote/speaker-diarization"
        )

    def process_audio(self):
        # transcribe 
        print("transcribe başladı ", datetime.datetime.now())
        audio = whisperx.load_audio(self.audio_file)
        result = self.model.transcribe(audio, batch_size=self.batch_size)
        print("transcribe bitti ", datetime.datetime.now())
        
        # alignment
        print("alignment başladı ", datetime.datetime.now())
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)
        print("alignment bitti ", datetime.datetime.now())
        # diarization
        print("diarization başladı ", datetime.datetime.now())
        diarize_segments = self.diarize_model(audio, min_speakers=2, max_speakers=2)
        audio_filename = os.path.splitext(os.path.basename(self.audio_file))[0]
        array = [audio_filename, whisperx.assign_word_speakers(diarize_segments, result)]
        print("diarization bitti ", datetime.datetime.now())
        return array