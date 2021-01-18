"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""


from datetime import datetime
from google.cloud import texttospeech
from flask import Response

import os
try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r".\cloud_key.json"
except:
    print("Please put or VERIFY the config file in config_key.json")


def speak(input_text, language, input_pitch, input_speed, voice_name):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text = input_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    voice = texttospeech.VoiceSelectionParams(
        language_code = str(language),
        name = str(voice_name),
    )
    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=int(input_pitch),
        speaking_rate=float(input_speed),
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("temp.mp3", "wb") as out:
    # Write the response to the output file.
        out.write(response.audio_content)
        # print('File Created')