# 🚀 AI Biometric Attendance System

An intelligent face-recognition-based attendance system built using **FastAPI + face-api.js**.  
This system allows admin-controlled student registration and automatic attendance marking using real-time face detection.

---

## 🎯 Features

- 🔐 Admin Login System
- 🤖 AI Face Recognition (browser-based)
- 🎥 Real-time Camera Capture
- 🧑‍🎓 Student Registration via Face Embeddings
- ✅ Automatic Attendance Marking
- 📊 Attendance Dashboard (Date & Time)
- 🎨 Clean UI (Sky Blue + White + Red Theme)

---

## 🏗️ Project Structure
AI-BIOMETRIC-ATTENDANCE/
│
├── backend/
│ ├── app/
│ ├── run.py
│ └── requirements.txt
│
├── frontend/
│ ├── assets/
│ ├── pages/
│ └── index.html
│
├── data/
│ └── attendance.db
│
├── README.md
└── .env

## ⚙️ Tech Stack

- **Backend:** FastAPI, SQLite, NumPy  
- **Frontend:** HTML, CSS, JavaScript  
- **AI:** face-api.js (client-side face recognition)  



---

## 🎯 Usage Flow

1. Login as admin  
2. Register student (capture face)  
3. Open Capture Attendance  
4. Face detected → Attendance marked ✔  
5. View attendance in dashboard  

---

## ⚠️ Important Notes

- Use **localhost (not file://)** for camera access  
- Ensure internet connection for face-api models  
- Good lighting improves face detection accuracy  

---

## 🚀 Future Improvements

- Multi-face detection  
- Anti-spoofing (photo detection prevention)  
- Cloud deployment (AWS / Render)  
- Export attendance to Excel  
- Mobile responsiveness  

---

## 👨‍💻 Author

Rohan Tiwari

---

## ⭐ If you like this project

Give it a star ⭐ and share feedback!