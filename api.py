import os
from babel import Locale

try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r".\cloud_key.json"
except:
    print("Please put or VERIFY the config file in config_key.json")

    
"""Lists the available voices."""
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

# Performs the list voices request
voices = client.list_voices()




def list_voices():
    all_voices = []
    for voice in voices.voices:
        single_voice = []
        # Display the voice's name. Example: tpc-vocoded
        # print(f"Name: {voice.name}")
        single_voice.append(voice.name)

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            # print(f"Supported language: {language_code}")
            single_voice.append(language_code)

        ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        # print(f"SSML Voice Gender: {ssml_gender.name}")
        single_voice.append(ssml_gender)
        all_voices.append(single_voice)
    
    return all_voices

def all_languages():
    all_languages = []
    for voice in list_voices():
        if voice[1] not in all_languages:
            all_languages.append(voice[1])
    return all_languages

def list_voices_by_language_code_and_gender(language_code, gender):
    voices_by_language_code = []

    for voice in list_voices():
        # print(voice)
        if voice[1] == language_code and  "SsmlVoiceGender."+gender.upper() in str(voice[2]) :
            voices_by_language_code.append(voice[0])
    if voices_by_language_code == []:
        voices_by_language_code = ['No voicenames available in this gender, try changing gender']

    return voices_by_language_code
    



# print(list_voices_by_language_code_and_gender('es-ES', 'NEUTRAL'))

# Getting language names from codes 

def Language_name(code):
    try:
        parts = code.split('-')
        a = parts[0]
        b = parts[1]
        locale = Locale(a,b)
        return locale.get_display_name('en_US')
    except:
        pass

