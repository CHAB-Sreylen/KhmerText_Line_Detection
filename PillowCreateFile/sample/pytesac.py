import pytesseract
import cv2

# Path to the image
image_path = "path/to/your/khmer_image.png"

# Load the image
image = cv2.imread(image_path)

# Configure Tesseract (replace with your Tesseract path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #example of windows path

# Perform OCR
text_data = pytesseract.image_to_data(image, lang='khm', output_type=pytesseract.Output.DICT)

# Extract bounding boxes
n_boxes = len(text_data['text'])
for i in range(n_boxes):
    if int(text_data['conf'][i]) > 60:  # Confidence threshold
        (x, y, w, h) = (text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) #draw the rectangle on the image.

# Display the image with bounding boxes (or save it)
cv2.imshow('Khmer Text Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()