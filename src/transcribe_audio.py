import whisper
import os
import argparse

parser = argparse.ArgumentParser(description="Транскрибация аудиофайлов из директории с помощью Whisper")
parser.add_argument("--input_dir", type=str, default="voice_input", help="Путь к директории с аудиофайлами (по умолчанию: voice_input)")
parser.add_argument("--output_dir", type=str, default="text_output", help="Путь к директории для сохранения текстовых файлов (по умолчанию: text_output)")
parser.add_argument("--language", type=str, default="ru", help="Язык аудио (например, 'ru' для русского, 'en' для английского). По умолчанию: 'ru'")
args = parser.parse_args()

model = whisper.load_model("base")

if not os.path.exists(args.input_dir):
    print(f"Ошибка: Директория {args.input_dir} не найдена")
    exit(1)

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

for filename in os.listdir(args.input_dir):
    if filename.endswith(".ogg") or filename.endswith(".wav"):
        audio_file = os.path.join(args.input_dir, filename)
        
        base_name = os.path.splitext(filename)[0]
        output_file = os.path.join(args.output_dir, f"{base_name}.txt")

        result = model.transcribe(audio_file, language=args.language)
        transcribed_text = result["text"]

        with open(output_file, "w") as f:
            f.write(transcribed_text)
        print(f"Текст сохранён в: {output_file}")