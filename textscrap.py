from better_profanity import profanity
import pytesseract as pyt
import cv2


#Read Text from Image
img = cv2.imread("shit.jpg")

pyt.pytesseract.tesseract_cmd = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)
print(text)

#with open("text_file.txt0", "w+") as f:
 #   f.write(text)

#filter text and return boolean
#from profanity import profanity
#profanity.contains_profanity(text)

#masking or censoring sensitive texts
print(profanity.censor(text))