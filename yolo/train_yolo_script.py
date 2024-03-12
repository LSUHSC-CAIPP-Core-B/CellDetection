from ultralytics import YOLO

model = YOLO("yolov8l.pt")

model.train(data="cell_dataset.yaml", 
            epochs=1,
            batch=8, 
            imgsz=128,
            name = "YOLOtestV",
            device="mps")

