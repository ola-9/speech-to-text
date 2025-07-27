
INPUT_DIR ?= voice_input
OUTPUT_DIR ?= text_output
LANGUAGE ?= ru
VENV_NAME ?= venv
PYTHON = $(VENV_NAME)/bin/python3
PIP = $(VENV_NAME)/bin/pip

install: venv
	$(PIP) install -r requirements.txt

venv:
	python3 -m venv $(VENV_NAME)

activate:
	@echo "Run the following command to activate the virtual environment:"
	@echo "source $(VENV_NAME)/bin/activate"

transcribe:
	$(PYTHON) src/transcribe_audio.py --input_dir $(INPUT_DIR) --output_dir $(OUTPUT_DIR) --language $(LANGUAGE)

clean:
	rm -rf $(VENV_NAME)

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make venv          - Create a virtual environment"
	@echo "  make activate      - Show command to activate the virtual environment"
	@echo "  make transcribe    - Transcribe audio files (use INPUT_DIR, OUTPUT_DIR, and LANGUAGE to specify options)"
	@echo "  make clean         - Remove the virtual environment"
	@echo "  make help          - Show this help message"