import streamlit as st
from transcription import transcribe_audio
from translation import translate_text
from audio_generation import text_to_speech
from censorship import censor_text
from utils import summarize_text, generate_title
import os

st.title("Multilingual Audio Transcription and Translation")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
if uploaded_file is not None:
    st.audio(uploaded_file)
    
    # Save the uploaded file temporarily
    with open("temp_audio_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    transcription = transcribe_audio("temp_audio_file")
    st.write("Transcription:", transcription)
    
    languages = {
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Chinese (Simplified)": "zh-cn",
        "Arabic": "ar",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko",
        "Italian": "it",
        "Turkish": "tr",
        "Dutch": "nl",
        "Swedish": "sv"
    }
    target_language_name = st.selectbox("Select target language for translation", list(languages.keys()))
    target_language = languages[target_language_name]
    
    translation = translate_text(transcription, target_language)
    st.write("Translation:", translation)
    
    censored_translation = censor_text(translation)
    st.write("Censored Translation:", censored_translation)
    
    summary = summarize_text(censored_translation)
    title = generate_title(censored_translation)
    
    st.write("Summary:", summary)
    st.write("Title:", title)
    
    audio_output_path = f"output_{target_language}.mp3"
    text_to_speech(censored_translation, target_language, audio_output_path)
    
    st.audio(audio_output_path)
    
    # Remove the temporary audio file
    os.remove("temp_audio_file")
