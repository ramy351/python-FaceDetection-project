# 🎭 Real-Time Face Detection

A simple real-time face detection application built with Python and OpenCV. It uses your webcam to detect faces live and draws bounding boxes around them. You can choose between full-screen or windowed display mode.

---

## 📸 Features

- Real-time face detection using your webcam
- Haar Cascade Classifier for accurate face detection
- Two display modes: **Full Screen** or **Small Window**
- Draws green bounding boxes around detected faces
- Lightweight and easy to run

---

## 🛠️ Requirements

- Python 3.x
- OpenCV

Install the dependency with:

```bash
pip install opencv-python
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/ramy351/python-FaceDetection-project.git
cd python-FaceDetection-project
```

2. Run the script:

```bash
python project.py
```

3. When prompted, choose your display mode:
   - Enter `1` for **Full Screen**
   - Enter `2` for **Small Window**

4. Press **`q`** to quit the application.

---

## 📁 Project Structure

```
face-detection/
│
├── project.py      # Main face detection script
└── README.md       # Project documentation
```

---

## ⚙️ How It Works

1. The program loads OpenCV's pre-trained **Haar Cascade** model for frontal face detection.
2. It captures live video from the default webcam (`camera index 0`).
3. Each frame is converted to **grayscale** for faster processing.
4. The `detectMultiScale` function scans the frame and returns coordinates of detected faces.
5. A **green rectangle** is drawn around each detected face.
6. The processed frame is displayed in the chosen window mode.

---

## 🧠 Detection Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `scaleFactor` | 1.1 | How much the image is scaled down at each step |
| `minNeighbors` | 5 | How many neighbors a rectangle needs to be considered a face |
| `minSize` | (30, 30) | Minimum face size in pixels |

---

## 📌 Notes

- Make sure your webcam is connected and accessible.
- The app uses camera index `0` (default webcam). Change `cv2.VideoCapture(0)` to `1` or `2` if you have multiple cameras.
- Works best in good lighting conditions.

---

