import cv2
import os

name = input("Enter name: ").strip()
path = f"known_faces/{name}"
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press 's' to save face, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Enroll Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"{path}/{count}.jpg", frame)
        print("Saved", count)
        count += 1

    if count >= 5 or cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
