from wtforms import Form, BooleanField, SubmitField, StringField, PasswordField, validators
from google.cloud import texttospeech

class RegistrationForm(Form):
    
    # Input Field 
    input_text = StringField('Text-to-Speak')

    # Submit 
    submit = SubmitField('Download')

    # # Select Language 
    # myLanguages = ['English', 'Hindi']
    # language = SelectField(u'Field name', choices = myLanguages, validators = [Required()])

    # # Select Voice Type
    # myVoive_Type = #number of choices
    # voice_type = SelectField(u'Field name', choices = myVoive_Type, validators = [Required()])

    # # Select Voice Name 
    # myVoice_Name = #number of choices
    # voice_name = SelectField(u'Field name', choices = myVoice_Name, validators = [Required()])

    # # Select Audio Device Profile
    # myAudio_Profile = #number of choices
    # audio_profile = SelectField(u'Field name', choices = myAudio_Profile, validators = [Required()])    


 