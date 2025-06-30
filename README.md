# Real-Time Object Detection System Using YOLOv8

This project implements a real-time object detection system using the YOLOv8 Nano model and OpenCV. The system is capable of identifying over 80 commonly encountered objects from a webcam feed, such as people, furniture, animals, electronic devices, and structural elements. It is designed to be lightweight, modular, and easily extensible for research, surveillance, or industrial applications.

---

## Project Objectives

- Perform real-time object detection through a computer's webcam
- Detect multiple object classes from the COCO dataset
- Provide a modular codebase with clear separation of detection and visualization logic
- Offer an adaptable foundation for future enhancements, including model fine-tuning and real-world deployment

---

## Project Structure

```
object-detection-ai/
├── models/
│   └── yolov8n.pt             # Pretrained YOLOv8 Nano model
├── utils/
│   └── draw_boxes.py          # Utility for drawing bounding boxes and labels
├── realtime_detection.py      # Main script for webcam-based detection
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Requirements

- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux (GUI required)
- A functioning webcam
- pip package manager

---

## Installation and Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/object-detection-ai.git
cd object-detection-ai
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Download the YOLOv8 Model**

Download the pretrained YOLOv8 Nano model file from the official Ultralytics release:

[Download yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)

Place the file in the `models/` directory as follows:

```
object-detection-ai/models/yolov8n.pt
```

---

## Running the System

Execute the detection script from the root of the project directory:

```bash
python realtime_detection.py
```
<img src="https://raw.githubusercontent.com/Ahmadjamil888/REALTIME-OBJ-DETECTION-SURVIELLENCE/refs/heads/main/Screenshot%202025-06-30%20185150.png">
To exit the detection window, press the `q` key.

---

## Customization

This system uses the YOLOv8 model pretrained on the COCO dataset. It can be customized for other use cases by:

- Replacing the model with a fine-tuned YOLO variant
- Modifying the `draw_boxes.py` logic to support additional metadata
- Integrating audio alerts, frame saving, or motion-based triggers

---

## License

This project is intended for educational and research purposes only. Consult relevant licensing terms for the YOLO model and third-party libraries before deploying in commercial or defense applications.
