from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_2_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        #just testing how it looks before join
        # text = str(pages)

        # with open('text_before_join.txt', 'w') as file:
        #      file.write(text)

        text = ''.join(pages)

        with open('text_after_join.txt', 'w') as file:
            file.write(text)

        text = text.replace('\n', '')

        with open('text_after_replace.txt', 'w') as file:
            file.write(text)
    else:
        return 'Missing file, check'


def main():
    print(pdf_2_mp3(file_path='test.pdf'))


if __name__ == '__main__':
    main()
