# 🚗 Smart Parking System using OpenCV

A computer vision-based smart parking system that detects available and occupied parking slots in real-time from video input using OpenCV and Python.

---

## 📁 Project Structure

# 🚗 Smart Parking System using OpenCV

A computer vision-based smart parking system that detects available and occupied parking slots in real-time from video input using OpenCV and Python.

---

## 📁 Project Structure

smart-parking-system/
├── carPark.mp4 # Input video of the parking lot
├── carParkImg.png # Still image for marking slot positions
├── ParkingSpacePicker.py # Tool to manually select parking spots
├── main.py # Main application for slot detection
├── CarParkPos # Auto-generated file storing slot positions


---

## 🔧 Features

- Detects **occupied** and **free** parking slots from video
- Real-time updates with OpenCV
- Simple and efficient **slot position selection** using mouse clicks
- Shows **current date** and **time**
- Displays **total available slots** out of all

---

## ▶️ How to Run

### Step 1: Mark Parking Spaces

Run this to manually define each parking spot:

```bash
python ParkingSpacePicker.py
python main.py
```
Automatically detects filled or empty slots

Displays number of free spaces

Shows date and live clock
---
📦 Requirements
Python 3.6+

OpenCV

cvzone

numpy
---
Install packages:
pip install opencv-python cvzone numpy
----

💡 Future Improvements
Add sound alert when parking is full

Display UI in web browser using Flask

Integrate sensors for hybrid detection

Upload detection result to Firebase
----
📸 Preview
## 🎥 Demo Video

▶️ Click the video below to see the Smart Parking System in action:

[Download and watch the demo](demo.mp4)


---
👩‍🎓 About Me
Savitha R
Final Year B.E. Student – Information Science & Engineering
CMR Institute of Technology, Bengaluru
