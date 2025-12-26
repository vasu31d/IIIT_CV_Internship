from ultralytics import YOLO
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # You can use yolov8n-seg.pt for segmentation

# Input and output folders
input_folder = r"C:\Users\Administrator\OneDrive\Desktop\CV_internship\frames"
output_folder = r"C:\Users\Administrator\OneDrive\Desktop\CV_internship\results"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all image files in the folder
image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".jpg")]

# Run detection on all frames
for img_path in image_files:
    results = model.predict(source=img_path, save=True, project=output_folder, name="detections")

print("✅ Detection completed! Check the 'results/detections' folder for output images.")
