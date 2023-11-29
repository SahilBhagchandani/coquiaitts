# Install all the requirements
# pip install TTS

# import all the modules that we will need to use
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import site
import torchaudio
import numpy as np

# Get the site packages location
location = site.getsitepackages()[0]

# Define the path to the models.json file
path = location + "/Lib/site-packages/TTS/.models.json"

# Create a ModelManager
model_manager = ModelManager(path)

# Download the TTS model and vocoder model
model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC_ph")
voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

# Initialize the Synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)

# def tts(text, pitch=0.0, speak_rate=1.0):
#     # Synthesize speech with adjusted parameters
#     outputs = synthesizer.tts(text, pitch=pitch, speak_rate=speak_rate)
#     return outputs

# def save_wav(outputs, out):
#     # Save the synthesized speech to a WAV file
#     wav_data = outputs['mel_outputs_postnet'].squeeze().detach().cpu().numpy()
#     torchaudio.save(out, torch.Tensor(wav_data), 22050)

