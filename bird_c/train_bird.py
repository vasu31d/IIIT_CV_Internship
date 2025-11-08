from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Train on your bird dataset
model.train(
    data="dataset/data.yaml",   # path to data.yaml
    epochs=20,                  # number of training epochs
    imgsz=640,                  # image size
    batch=8,                    # adjust if memory issue
    name="bird_species_detect"  # run name
)

# Test the trained model on a sample image
model.predict(
    source="bus.jpg",  # test image
    weights="runs/detect/bird_species_detect/weights/best.pt",
    show=True
)
