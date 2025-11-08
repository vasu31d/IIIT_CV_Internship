# 🤖 Computer Vision Internship Tasks :
### 📅 Internship Project Series on Object Detection & Video Analysis

This repository contains the first three tasks completed during the Computer Vision Internship.  
Each task focuses on developing core skills in image and video-based object detection using **Python**, **YOLOv8**, and **FFmpeg**.

---

## 🧩 Task 1 – Image Object Detection using YOLOv8

### 🎯 Objective
Perform object detection on images using the **YOLOv8 model** to identify and classify real-world objects.

### ⚙️ Steps:
1. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```
2. Load the YOLOv8 model and detect objects:
   ```python
   from ultralytics import YOLO

   model = YOLO("yolov8n.pt")
   results = model("bus.jpg", show=True)
   ```
3. The detected image will display bounding boxes with class labels and confidence scores.

### 📸 Output
- Input: `bus.jpg`  
- Output: Detected image with bounding boxes and class names.

---

## 🧩 Task 2 – Object Detection in Multiple Images

### 🎯 Objective
Perform batch object detection on multiple images using YOLOv8.

### ⚙️ Steps:
1. Create a list of image URLs or local file paths.
2. Run the detection in a loop:
   ```python
   from ultralytics import YOLO
   import os, requests

   model = YOLO("yolov8n.pt")

   image_urls = [
       "https://ultralytics.com/images/bus.jpg",
       "https://ultralytics.com/images/zidane.jpg"
   ]

   os.makedirs("results", exist_ok=True)

   for url in image_urls:
       filename = os.path.join("results", os.path.basename(url))
       with open(filename, "wb") as f:
           f.write(requests.get(url).content)
       model.predict(source=filename, save=True)
   ```
3. View all output images in the `results/` folder.

### 📸 Output
- Input: Multiple sample images  
- Output: Detected images with labels and bounding boxes saved in the output folder.

---

## 🧩 Task 3 – Video Frame Extraction and Object Detection

### 🎯 Objective
To analyze and detect objects in a video using **YOLOv8** and **FFmpeg**, then generate a processed output video with bounding boxes and labels.

### ⚙️ Tools Used
- **YOLOv8 (Ultralytics)** – Object Detection  
- **FFmpeg** – Frame extraction and video compression  
- **Python 3.x**, **VS Code**

### ⚙️ Steps:
1. **Extract Frames from Input Video**
   ```bash
   ffmpeg -i input_video.mp4 frames/frame_%04d.jpg
   ```
2. **Run YOLOv8 Detection on Extracted Frames**
   ```python
   from ultralytics import YOLO
   import os

   model = YOLO("yolov8n.pt")
   input_folder = "frames/"
   output_folder = "detections/"
   os.makedirs(output_folder, exist_ok=True)

   for img in os.listdir(input_folder):
       model.predict(source=os.path.join(input_folder, img), save=True, project=output_folder)
   ```
3. **Merge Detected Frames into Final Video**
   ```bash
   ffmpeg -f concat -safe 0 -i videos.txt -c copy results/detected_output.mp4
   ```
4. **Compress Final Video (Optional)**
   ```bash
   ffmpeg -i results/detected_output.mp4 -b:v 1M results/compressed_output.mp4
   ```

### 📸 Output
- **Input:** Raw video footage  
- **Output:** Processed video with detected objects and optimized file size (<10 MB)

---

## 📁 Folder Structure
```
CV_Internship/
│
├── Task1_Image_Detection/
│   ├── bus.jpg
│   └── detect_image.py
│
├── Task2_Multi_Image_Detection/
│   ├── images/
│   └── detect_multiple.py
│
├── Task3_Video_Object_Detection/
│   ├── input_video/
│   ├── frames/
│   ├── detections/
│   ├── results/
│   └── detect_video.py
│
└── README.md
```

---

## 🏁 Summary
| Task | Description | Tool |
|------|--------------|------|
| 1 | Object detection on single image | YOLOv8 |
| 2 | Object detection on multiple images | YOLOv8 |
| 3 | Object detection in videos | YOLOv8 + FFmpeg |

---

### 👨‍💻 Author
**UPPUTURI VASU**  
📧 vasuupputuri5@gmail.com  
🎓 Computer Vision Internship Project  
🗓️ November 2025
