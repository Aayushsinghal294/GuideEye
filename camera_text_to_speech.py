import cv2
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)

print("Press 'c' to capture image and read text")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        if text.strip() == "":
            engine.say("No readable text found")
        else:
            engine.say("Text detected")
            engine.say(text)

        engine.runAndWait()

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
