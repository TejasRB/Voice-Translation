from gtts import gTTS

def text_to_speech(text, language, output_path):
    tts = gTTS(text=text, lang=language)
    tts.save(output_path)
