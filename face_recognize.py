import cv2
import numpy as np
import os
from deepface import DeepFace

known_faces = {}

# Load known faces
print("Loading known faces...")
if not os.path.exists("known_faces"):
    print("ERROR: 'known_faces' folder not found!")
    print("Please run: python save_face.py")
    exit()

for person in os.listdir("known_faces"):
    person_path = f"known_faces/{person}"
    if not os.path.isdir(person_path):
        continue
    
    embeddings = []
    for img in os.listdir(person_path):
        if not img.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        img_path = f"{person_path}/{img}"
        try:
            emb = DeepFace.represent(
                img_path=img_path,
                model_name="Facenet",
                enforce_detection=False
            )[0]["embedding"]
            embeddings.append(emb)
        except Exception as e:
            print(f"Warning: Could not load {img_path}")

    if embeddings:
        known_faces[person] = np.mean(embeddings, axis=0)
        print(f"✓ Loaded {len(embeddings)} images for {person}")
    else:
        print(f"✗ No valid images found for {person}")

if not known_faces:
    print("\nERROR: No faces loaded! Please enroll faces using:")
    print("  python save_face.py")
    exit()

print(f"\n✓ Ready! Known persons: {list(known_faces.keys())}\n")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = DeepFace.extract_faces(
        img_path=frame,
        enforce_detection=False
    )

    for det in detections:
        fa = det["facial_area"]
        x, y, w, h = fa["x"], fa["y"], fa["w"], fa["h"]

        face = frame[y:y+h, x:x+w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        emb = DeepFace.represent(
            face,
            model_name="Facenet",
            enforce_detection=False
        )[0]["embedding"]

        name = "Unknown"
        min_dist = float("inf")

        for known_name, known_emb in known_faces.items():
            dist = np.linalg.norm(np.array(emb) - np.array(known_emb))
            if dist < min_dist:
                min_dist = dist
                if dist < 0.7:  # Increased threshold for better matching
                    name = known_name

        # Color: Green if recognized, Red if unknown
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        
        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
        cv2.putText(frame, f"{name} ({min_dist:.2f})", (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
