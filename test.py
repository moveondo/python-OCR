#tesseract -v
#tesseract --list-langs

# import pytesseract
# from PIL import Image
# print(11)
# image = Image.open('31.jpg')
# code = pytesseract.image_to_string(image)
# print(code)

from pytesseract import PyTessBaseAPI

images = ['31.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
