from ultralytics import YOLO

model = YOLO("yolov8l.pt")

model.train(data="mef1.yaml", 
            epochs=1,
            batch=16, 
            imgsz=128,
            name = "TestYOLO")

