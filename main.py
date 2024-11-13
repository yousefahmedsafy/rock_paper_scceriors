from ultralytics import YOLO

model= YOLO('rock_paper_best.pt')
results = model(1
                , show=True)  # 0 selects the default webcam

