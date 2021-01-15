
from main import download
from flask import Flask, render_template, request, redirect, jsonify
# from form import RegistrationForm
import os
from datetime import datetime
from google.cloud import texttospeech
from api import list_voices_by_language_code_and_gender, list_voices, all_languages, Language_name


# router

app = Flask(__name__)

@app.route('/')
def home():
    genders = ['NEUTRAL','FEMALE','MALE']
    Languages=[]
    for language_code in all_languages():
        a = [language_code,Language_name(language_code)]
        Languages.append(a)
    return render_template('index.html', languages=Languages, genders = genders)  
   


@app.route('/getdata', methods = ['POST'])
def getdata():
    if request.method == 'POST':
        selected_code = request.form['selected_lang']
        selected_gender = request.form['selected_gender']
        all_available_voice_names = list_voices_by_language_code_and_gender(selected_code,selected_gender)
        # print(selected_code, selected_gender)
        # print(all_available_voice_names)
        return jsonify({'data': render_template('getdata.html', all_available_voice_names=all_available_voice_names)})        


@app.route('/download', methods = ['POST'])
def download_file():
    if request.method == 'POST':
        file_name = request.form['file_name']
        input_text = request.form['input_text']
        language = request.form['language']
        input_pitch = request.form['pitch_value']
        input_speed = request.form['speed_value']
        voice_name = request.form['available_voices']
        # print(file_name, input_text, language, input_pitch, input_speed, voice_name)
        download(file_name, input_text, language, input_pitch, input_speed, voice_name)
        return "File Downloaded with name: " + file_name
    else:
        return "Invalid Request"


if __name__ == '__main__':
    app.run(debug = True)
