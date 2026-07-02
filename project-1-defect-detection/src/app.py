import cv2
import numpy as np
import gradio as gr
from ultralytics import YOLO

model = YOLO("models/best.pt")
CLASS_NAMES = ['mouse_bite', 'spur', 'missing_hole',
               'short', 'open_circuit', 'spurious_copper']

def detect_defects(image: np.ndarray, conf_threshold: float):
    if image is None:
        return None, "No image uploaded."

    results   = model(image, conf=conf_threshold, verbose=False)
    result    = results[0]
    boxes     = result.boxes
    annotated = image.copy()
    detections = []

    for i in range(len(boxes)):
        x1, y1, x2, y2 = map(int, boxes.xyxy[i])
        cls_name   = CLASS_NAMES[int(boxes.cls[i])]
        confidence = round(float(boxes.conf[i]), 3)
        detections.append({'class': cls_name, 'confidence': confidence})

        cv2.rectangle(annotated, (x1,y1), (x2,y2), (0,0,255), 2)
        label = f"{cls_name} {confidence:.2f}"
        (w, h), _ = cv2.getTextSize(label,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(annotated, (x1, y1-h-8),
                      (x1+w, y1), (0,0,255), -1)
        cv2.putText(annotated, label, (x1, y1-4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    detections.sort(key=lambda x: x['confidence'], reverse=True)
    summary = f"Found {len(detections)} defect(s)\n\n"
    for d in detections:
        summary += f"• {d['class']} — {d['confidence']:.3f}\n"
    if not detections:
        summary = "No defects detected above threshold."

    return annotated, summary


demo = gr.Interface(
    fn=detect_defects,
    inputs=[
        gr.Image(label="Upload PCB Image", type="numpy"),
        gr.Slider(0.1, 0.9, value=0.5, step=0.05,
                  label="Confidence Threshold")
    ],
    outputs=[
        gr.Image(label="Detected Defects"),
        gr.Textbox(label="Results", lines=8)
    ],
    title="PCB Defect Detection",
    description=(
        "Upload a PCB image to detect manufacturing defects. "
        "Model: YOLOv8n | Dataset: PCB Defect (8,000 images) | "
        "mAP@50: 0.989"
    )
)

demo.launch(server_name="0.0.0.0", server_port=7860)