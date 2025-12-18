import cv2
import os

video_path = "video.mp4"     # change to your actual file name
output_dir = "frames"
frame_step = 20              # save every 20th frame; adjust later if needed

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if count % frame_step == 0:
        filename = os.path.join(output_dir, f"frame_{saved:05d}.jpg")
        cv2.imwrite(filename, frame)
        saved += 1
    count += 1

cap.release()
print(f"Saved {saved} frames to {output_dir}")
