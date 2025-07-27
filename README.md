# Speech-to-Text Transcription

This project uses OpenAI's Whisper model to transcribe audio files from a directory and save the results as text files in another directory.

## Requirements

- Python 3.x
- `whisper` library (install via `pip install openai-whisper`)
- `ffmpeg` (required by Whisper, install via your package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/speech-to-text.git
   cd speech-to-text
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

## Usage

### Using the Script Directly

1. **Default directories and language**:

   ```bash
   python3 src/transcribe_audio.py
   ```

   This will transcribe all `.ogg` and `.wav` files from the `voice_input` directory and save the results in the `text_output` directory. The default language is Russian (`ru`).

2. **Custom directories and language**:

   ```bash
   python3 src/transcribe_audio.py --input_dir my_input_folder --output_dir my_output_folder --language en
   ```

   This will transcribe files from `my_input_folder` and save the results in `my_output_folder`. The language is set to English (`en`).

### Using Makefile

1. **Default directories and language**:

   ```bash
   make transcribe
   ```

   This will transcribe all `.ogg` and `.wav` files from the `voice_input` directory and save the results in the `text_output` directory. The default language is Russian (`ru`).

2. **Custom directories and language**:

   ```bash
   make transcribe INPUT_DIR=my_input_folder OUTPUT_DIR=my_output_folder LANGUAGE=ru
   ```

   This will transcribe files from `my_input_folder` and save the results in `my_output_folder`. The language is set to English (`ru`).

## Notes

- Ensure that the `voice_input` directory exists and contains valid audio files.
- The `text_output` directory will be created automatically if it doesn't exist.
- Supported languages include `ru` (Russian), `en` (English), and others. Refer to the Whisper documentation for a full list.
