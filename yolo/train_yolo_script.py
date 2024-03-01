from ultralytics import YOLO

model = YOLO("yolov8l.pt")

model.train(data="mef1.yaml", 
            epochs=50,
            batch=8, 
            imgsz=128,
            name = "YOLO_0213_1",
            device="mps")

