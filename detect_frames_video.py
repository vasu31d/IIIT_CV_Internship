import cv2
import os
import natsort  # pip install natsort

# Path to your detections folder
frames_folder = "runs/detect/predict"  # change this to your folder path

# Output video path
output_video = "detections_video.mp4"

# Get all frame filenames
frames = [f for f in os.listdir(frames_folder) if f.endswith(('.jpg', '.png'))]
frames = natsort.natsorted(frames)  # sort numerically (detections1,2,3...)

# Read first frame to get size
first_frame = cv2.imread(os.path.join(frames_folder, frames[0]))
height, width, _ = first_frame.shape

# Define video writer (30 FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, 30, (width, height))

# Write each frame
for frame in frames:
    img = cv2.imread(os.path.join(frames_folder, frame))
    video.write(img)

video.release()
print(f"✅ Video saved successfully as: {output_video}")
