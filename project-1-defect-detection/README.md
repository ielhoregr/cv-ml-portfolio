# 🔍 AI-Based PCB Defect Detection using YOLOv8

An end-to-end Computer Vision project for automated Printed Circuit Board (PCB) defect detection using **YOLOv8**, featuring a **live Gradio web application** deployed on Hugging Face Spaces.

The model detects six common PCB manufacturing defects in real time, helping automate the quality inspection process in electronics manufacturing.

---

## 🚀 Live Demo

👉 **Try the application here:**

**https://huggingface.co/spaces/ibrahimMohsen/pcb-defect-detection**

---

## 📌 Project Overview

Printed Circuit Boards (PCBs) are the backbone of modern electronic devices. During manufacturing, defects such as missing holes, mouse bites, or open circuits can lead to product failures and increased production costs.

This project demonstrates how deep learning can automate PCB inspection by detecting defects directly from images.

The system allows users to:

* Upload a PCB image
* Detect manufacturing defects
* Adjust the confidence threshold
* Visualize detected defects with bounding boxes
* View a summary of detected defect types and confidence scores

---

## ✨ Features

* Custom-trained YOLOv8 object detection model
* Detection of six PCB defect categories
* Interactive Gradio web interface
* Adjustable confidence threshold
* Real-time inference
* Bounding box visualization
* Hugging Face deployment
* Easy-to-use interface for demonstration purposes

---

## 📂 Defect Classes

The model detects the following PCB defects:

| Class           |
| --------------- |
| Mouse Bite      |
| Spur            |
| Missing Hole    |
| Short           |
| Open Circuit    |
| Spurious Copper |

---

## 🛠️ Tech Stack

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* Gradio
* Hugging Face Spaces

---

## 📊 Model Performance

| Metric | Value     |
| ------ | --------- |
| Model  | YOLOv8n   |
| mAP@50 | **0.989** |

The model was trained on a publicly available PCB defect dataset containing approximately **8,000 annotated images**.

---

## 📸 Application Preview

### Home Interface

![Application Screenshot](assets/demo1.png)

### Detection Example

![Detection Screenshot](assets/demo2.png)

---


## 📁 Project Structure

```text
pcb-defect-detection/
│
├── data/                  # Dataset and annotations
├── models/
│   └── best.pt            # Trained YOLOv8 model weights
├── notebooks/             # Training and experimentation notebooks
├── results/               # Application screenshots and demo images
│   ├── demo1.png
│   └── demo2.png
├── src/                   # Source code
│   └── app.py             # Gradio application
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pcb-defect-detection.git

cd pcb-defect-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The application will be available at:

```
http://localhost:7860
```

---

## 🧠 How It Works

1. Upload a PCB image.
2. The image is passed to the trained YOLOv8 model.
3. The model detects manufacturing defects.
4. Bounding boxes and confidence scores are generated.
5. The interface displays the annotated image alongside a summary of detected defects.

---

## 💡 Future Improvements

Planned enhancements include:

* Defect statistics dashboard
* REST API
* Batch image inspection
* Inspection history
* Severity estimation
* Production-ready reporting
* Docker deployment
* CI/CD pipeline

---

## 👨‍💻 Author

**Ibrahim Mohsen**

Machine Learning Engineer | Computer Vision | Deep Learning

Feel free to connect with me on LinkedIn or explore my other projects.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a **⭐ Star**. It helps others discover the project and supports my work.
