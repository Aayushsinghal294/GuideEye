import cv2
import pytesseract
import pyttsx3

# For Windows only (comment on Linux)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

engine = pyttsx3.init()

# Open camera
cap = cv2.VideoCapture(0)

print("Press SPACE to capture image for OCR, ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("OCR Test - Press SPACE to capture", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27:  # ESC key
        break
    elif key == 32:  # SPACE key
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Perform OCR
        text = pytesseract.image_to_string(gray)
        
        print("\nExtracted Text:")
        print(text)
        
        # Speak the text
        if text.strip() == "":
            engine.say("No readable text found")
        else:
            engine.say("Text detected")
            engine.say(text)
        engine.runAndWait()
        
        print("\nPress SPACE for another capture, ESC to exit")

cap.release()
cv2.destroyAllWindows()
