from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf

# load model and processor
processor = WhisperProcessor.from_pretrained("./Whisper_base_model")
model = WhisperForConditionalGeneration.from_pretrained("./Whisper_base_model")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="vietnamese", task="transcribe")

# read wav file to array
sound_arr,sampling_rate = sf.read("./test.wav")

input_features = processor(sound_arr, sampling_rate=sampling_rate, return_tensors="pt").input_features

# generate token ids from model
predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)

# decode token ids to text
transcription = processor.batch_decode(predicted_ids)
print(transcription)