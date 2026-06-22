import cv2
import pytesseract
import pyttsx3

# Windows path (comment if Linux)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

engine = pyttsx3.init()

# Capture from camera
cap = cv2.VideoCapture(0)
print("Capturing image from camera...")

ret, frame = cap.read()
if not ret:
    print("Failed to capture image")
    engine.say("Failed to capture image")
    engine.runAndWait()
else:
    cv2.imshow("Captured Image", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    text = pytesseract.image_to_string(gray)
    
    print("\nExtracted Text:")
    print(text)
    
    if text.strip() == "":
        engine.say("No text detected")
    else:
        engine.say("Reading text")
        engine.say(text)
    
    engine.runAndWait()
    
    print("\nPress any key to close...")
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
