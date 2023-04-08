# Speech recognition vietnamese
## Description 
This is a Python repo for speech recognition vietnamese using `wav2vec2-base-vietnamese-250h` model and `whisper-base` model.

## Requirements 
- Python 3.9

## Installation 
Run the following command to install library 

`pip install -r requirements.txt`

to download the whisper-base model file run the following command

`wget -P ./Whisper_base_model https://huggingface.co/VtAIP/whisper-base/resolve/main/pytorch_model.bin`

and to download the wav2vec2-base-vietnamese-250h model file run the following command

`wget -P ./Wav2Vec2_VI_model https://huggingface.co/nguyenvulebinh/wav2vec2-base-vietnamese-250h/resolve/main/pytorch_model.bin`

## Usage
You can run the inference of the `wav2vec2-base-vietnamese-250h` model with the `infer_wav2vec.py` file and of the `whisper-base` model with the `infer_whisper.py` file. 

## Credits
This repo uses the wav2vec2-base-vietnamese-250h model developed by nguyenvulebinh from VietAI and the Whisper-nase model developed by OpenAI, coupled with the Hugging Face Transformers library, which is an open-source library for NLP models.