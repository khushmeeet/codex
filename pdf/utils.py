from django.core.files.storage import FileSystemStorage
import textract


def process_pdf(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    text = textract.process(fs.path(filename), method='tesseract')
    return text


def replace_newlines_with_br(text):
    return text.replace('\\n', '<br>')
