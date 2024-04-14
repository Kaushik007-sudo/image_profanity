from better_profanity import profanity
import pytesseract as pyt
import cv2

# List of image files
image_files = ["shit.jpg", "hell.jpg", "savage.jpg", "wanker.jpg", "slut.png"]

# Path to Tesseract executable
pyt.pytesseract.tesseract_cmd = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Loop through each image file
for image_file in image_files:
    # Read the image
    img = cv2.imread(image_file)
    
    # Convert image to text
    text = pyt.image_to_string(img)
    
    # Censor profanity
    censored_text = profanity.censor(text)
    
    # Print censored text
    print(f"$$Censored text from {image_file}:")
    print(censored_text)
    print("------------------")