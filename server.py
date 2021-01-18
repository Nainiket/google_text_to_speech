from main import speak
from flask import Flask, render_template, request, redirect, jsonify, Response
# from form import RegistrationForm
import os
from datetime import datetime
from google.cloud import texttospeech
from api import list_voices_by_language_code_and_gender, list_voices, all_languages, Language_name


# router

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        print(request.method)
        genders = ['NEUTRAL','MALE']
        Languages=[]
        for language_code in all_languages():
            a = [language_code,Language_name(language_code)]
            Languages.append(a)
        return render_template('index.html', languages=Languages, genders = genders)

    elif request.method == 'POST':
        print(request.method)
        input_text = request.form['input_text']
        language = request.form['language']
        input_pitch = request.form['pitch_value']
        input_speed = request.form['speed_value']
        voice_name = request.form['available_voices']
        input_param = input_text, language, input_pitch, input_speed, voice_name
        speak(input_text, language, input_pitch, input_speed, voice_name)
        print('rendering audio.html')
        return jsonify({'data': render_template('audio.html', input_param= input_param)})

    else:
        return "Invalid Request"
        
@app.route('/mp3')
def streammp3():
    def generate():
        with open("temp.mp3", "rb") as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/mp3")


@app.route('/getdata', methods = ['POST'])
def getdata():
    if request.method == 'POST':
        selected_code = request.form['selected_lang']
        selected_gender = request.form['selected_gender']
        all_available_voice_names = list_voices_by_language_code_and_gender(selected_code,selected_gender)
        # print(selected_code, selected_gender)
        # print(all_available_voice_names)
        return jsonify({'data': render_template('getdata.html', all_available_voice_names=all_available_voice_names)})        


if __name__ == '__main__':
    app.run(debug = True)
