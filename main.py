from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('ya.jpg')
text = pytesseract.image_to_string(image, lang='eng')
print(text)

with open('output.txt', 'w') as file:
    file.write(text)
