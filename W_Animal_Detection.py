from ultralytics import YOLO
import cv2
import threading
import pygame

model = YOLO("best.pt")
cap = cv2.VideoCapture(0)
target_ids = [20, 21]  # animal ID's
alarm_playing = False

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav") 

def play_alarm():
    global alarm_playing
    alarm_playing = True
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    alarm_playing = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected = False

    for box in model(frame, verbose=False)[0].boxes:
        class_id = int(box.cls[0])
        if class_id in target_ids:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[class_id]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            print(f"{label.capitalize()} detected!")
            detected = True

    if detected and not alarm_playing:
        threading.Thread(target=play_alarm, daemon=True).start()

    cv2.imshow("Animal Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
