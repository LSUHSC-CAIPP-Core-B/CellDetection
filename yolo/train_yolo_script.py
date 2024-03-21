from ultralytics import YOLO

model = YOLO("yolov8l.pt")

model.train(data="mef1.yaml", 
            epochs=2,
            batch=8, 
            imgsz=128,
            name = "YOLOtestJian2",
            device="0")

