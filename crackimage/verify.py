import pytesseract
from PIL import Image


image = Image.open('code1.jpg')
result = pytesseract.image_to_string(image)
print(result)
