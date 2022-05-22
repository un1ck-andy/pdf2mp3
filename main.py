from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_2_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return 'File exists'
    else:
        return 'Missing file, check'


def main():
    print(pdf_2_mp3(file_path='test.pdf'))


if __name__ == '__main__':
    main()
