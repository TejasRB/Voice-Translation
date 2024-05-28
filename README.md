# Multilingual Audio Transcription and Translation

This project is a Streamlit web application that accepts audio files in 15 major languages (both Indian and Western), transcribes and translates them to English and all the other 15 languages, generates audio files in all these languages, and provides a user-friendly interface for selection and playback. It also censors cuss words, retains English words within other languages, and summarizes the text to generate a title.

## Features

- **Input Languages**: Supports 15 major languages including English, Hindi, French, German, Spanish, Chinese (Simplified), Arabic, Portuguese, Russian, Japanese, Korean, Italian, Turkish, Dutch, and Swedish.
- **Transcription**: Converts audio files to text in the source language using OpenAI Whisper.
- **Translation**: Translates the text to English and all other 15 languages using Google Translate.
- **Audio Generation**: Converts translated texts back to audio in each language using Google Text-to-Speech (gTTS).
- **Censorship**: Seamlessly censors cuss and foul language using the `better_profanity` library.
- **Language Mixing**: Retains English words within other languages to maintain a natural touch.
- **Expressiveness**: Ensures the translated voice maintains the original clip's emotion.
- **Summary and Title Generation**: Summarizes the text to create a title for the audio clip.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/TejasRB/Voice-Translation.git
    cd Voice-Translation
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload an audio file**:
    - The app accepts audio files in `.mp3` and `.wav` formats.
    - The uploaded file will be transcribed and translated to the selected target language.

2. **Select a target language**:
    - Choose from the dropdown menu to select the desired language for translation and audio generation.

3. **View and listen to the results**:
    - The transcription, translation, censored translation, summary, and title will be displayed.
    - Generated audio in the selected language will be available for playback.

## Project Structure
Voice-Translation/
│
├── app.py # Main Streamlit app
├── transcription.py # Module for audio transcription
├── translation.py # Module for text translation
├── audio_generation.py # Module for text-to-speech conversion
├── censorship.py # Module for censoring profane words
├── utils.py # Utility functions for summarizing and title generation
├── requirements.txt # List of dependencies
├── .gitignore # Git ignore file
└── wordlists/ # Directory containing word lists for profanity filtering
├── ar-latn.txt
├── en.txt
├── es.txt
├── fr.txt
├── it.txt
├── pt.txt
└── ... (other languages)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Google Translate](https://cloud.google.com/translate)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [better_profanity](https://pypi.org/project/better-profanity/)
- [words/cuss](https://github.com/words/cuss)
- [chucknorris-io/swear-words](https://github.com/chucknorris-io/swear-words)

## Contact

For any questions or inquiries, please contact Tejas at [tejasraghavendrabhoopalam@gmail.com].
