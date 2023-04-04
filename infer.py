from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import soundfile as sf
import torch

# load model and tokenizer
processor = Wav2Vec2Processor.from_pretrained("./Wav2Vec2_VI_model")
model = Wav2Vec2ForCTC.from_pretrained("./Wav2Vec2_VI_model")

# read wav file to array
sound_arr,_ = sf.read("./test.wav")

# tokenize
input_values = processor(sound_arr, return_tensors="pt", padding="longest").input_values  # Batch size 1

# retrieve logits
logits = model(input_values).logits

# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)

print(transcription)