# 🐘 WILD EYE: Wild Animal Intrusion Detection System

> A real-time wildlife detection system using **YOLOv8** to identify **elephants** and **bears** via webcam and trigger an **alarm** for early warning.


## 📖 Introduction

> **Wild animal intrusions** near human settlements or farmlands pose serious threats to both people and wildlife.  
> Early detection is crucial for **prevention, safety, and response**.

**WILD EYE** is a real-time intrusion detection system that leverages computer vision and deep learning to detect elephants and bears using a webcam feed. When a target animal is detected, the system plays a **loud alarm** to warn nearby humans and deter wildlife.

> ⚠️ **Note:** This version of the model is trained to detect **only elephants and bears**. Additional animals can be added with retraining.

---

## 🛠️ Tools & Technologies

| Tool / Library            | Purpose                                    |
|---------------------------|--------------------------------------------|
| **YOLOv8 (Ultralytics)**  | Real-time object detection (PyTorch)       |
| **OpenCV**                | Webcam access & frame rendering            |
| **Pygame**                | Alarm sound playback                       |
| **Python 3.8+**           | Scripting language                         |
| **Threading**             | Non-blocking alarm execution               |
| **Custom YOLO Model**     | Trained to recognize elephants and bears   |

---

## 🚀 Quick Start


### 1️⃣ Clone the repository
```bash
git clone https://github.com/aflah-m/WILD-EYE.git
cd WILD-EYE
```
### 2️⃣ Install dependencies
```bash
pip install ultralytics opencv-python pygame
```
### 3️⃣ Run the detection script
```bash
python animal_detection.py
```
🎥 Ensure your webcam is accessible and not used by other applications.

## 📦 Included Files

| File                  | Description                              |
|-----------------------|------------------------------------------|
| animal_detection.py   | Main Python detection script             |
| best.pt               | YOLOv8 model trained on elephants & bears|
| alarm.wav             | Sound played when animal is detected     |
| requirements.txt      | Dependency list for quick installation   |
| README.md             | Project documentation (this file)        |


### > ⚠️ **Python Interpreter Tip (VS Code)**  
> If you see a warning about selecting a Python interpreter in VS Code:  
> - Press `Ctrl + Shift + P`  
> - Choose **Python: Select Interpreter**  
> - Select `.venv/Scripts/python.exe` or your environment's interpreter


## 🧠 Model Details

- 🧾 **Model**: `best.pt` (YOLOv8 custom)
- 📁 **Format**: COCO-style dataset (YOLOv8 compatible)

### 🏷️ Class Mappings

| Class ID | Animal     |
|----------|------------|
| 20       | 🐘 Elephant |
| 21       | 🐻 Bear     |

### 🔍 Inspect Class Names

```python
print(model.names)
```


## 🗂️ Dataset Structure (for Retraining)

```plaintext
datasets/
├── images/
│   ├── train/
│   ├── val/
│   └── test/         
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
```


Each `.txt` label file inside `labels/` must follow the **YOLO format**:
<class_id> <x_center> <y_center> <width> <height>
All values must be **normalized** between `0.0` and `1.0`.

## 🔧 Customization

### ➕ Add More Animals
- Retrain or fine-tune `best.pt` with your new dataset.
- Replace the model file in the project directory.
- Update the `target_ids` list in `animal_detection.py`.

### 🔊 Change Alarm Sound
- Replace `alarm.wav` with any other `.wav` file of your choice.

## 🖼️ Sample Output

> *(screenshots showing bounding boxes and detection results)*

![Elephant Detection](./image01.webp)

### ✅ Features:
- Bounding boxes drawn over detected animals
- 🔊 Alarm sound played once per detection
- 🖥️ Console log example:


## 📌 Notes

- ✅ Automatically uses **GPU** if available  
- 🔁 Alarm uses **threading** to prevent lag or freezing  
- 🧠 Based on a **YOLOv8 custom-trained model**  
- 📴 Fully **offline** — no internet or cloud services needed  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [COCO Dataset](https://cocodataset.org/)
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Pygame](https://www.pygame.org/)
