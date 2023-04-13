from flask import Flask, request
import soundfile as sf
import io
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# load model and processor
processor = WhisperProcessor.from_pretrained("./Whisper_base_model")
model = WhisperForConditionalGeneration.from_pretrained("./Whisper_base_model")
forced_decoder_ids = processor.get_decoder_prompt_ids(language="vietnamese", task="transcribe")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def whisper_predict():
    file = request.data
    # read wav file to array
    sound_arr, sampling_rate = sf.read(io.BytesIO(file))
    input_features = processor(sound_arr, sampling_rate=sampling_rate, return_tensors="pt").input_features

    # generate token ids from model
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)

    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    # transcription = str(sampling_rate)
    return transcription[0]

if __name__ == '__main__':
    app.run(port=5000)