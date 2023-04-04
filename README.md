# Speech recognition vietnamese
## Description 
This is a Python program for inference the wav2vec2-base-vietnamese-250h model. The model is used for the speech recognition task, specifically vietnamese speech

## Requirements 
- Python 3.9

## Installation 
Run the following command to install library and to download model weight

`pip install -r requirements.txt`

to download the model file run the following command

`wget -P ./Wav2Vec2_VI_model https://huggingface.co/nguyenvulebinh/wav2vec2-base-vietnamese-250h/resolve/main/pytorch_model.bin`

## Usage
You can run the inference with the `infer.py` file. 

## Credits
This repo uses the wav2vec2-base-vietnamese-250h model developed by nguyenvulebinh from VietAI, coupled with the Hugging Face Transformers library, which is an open-source library for NLP models.