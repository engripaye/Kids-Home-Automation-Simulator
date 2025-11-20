# 🏠 Kids Home Automation Simulator

### **A Fun & Interactive Web-Based Home Automation Simulator for Kids**

This project is a simple, friendly, and educational **home automation simulator** where kids can control virtual household devices (lights, fans, doors, etc.) using a clean web interface.
It uses a **FastAPI backend**, **JavaScript frontend**, and **SQLite database** for device state storage.

---

## ⭐ Project Highlights

* 🌐 **Modern Web-Based Interface** (HTML, CSS, JS)
* ⚡ **FastAPI Backend** — fast, clean, async, and scalable
* 💾 **SQLite Database** to persist device states
* 🔌 **Real-Time Device Toggling**
* 🧒 **Child-Friendly UI & Simple Interaction**
* 🧱 **Clean & Professional Project Structure**
* 🚀 **Easy to extend** — add thermostats, alarms, TVs, etc.

---

## 📁 Project Structure

```
kids_home_automation/
├─ app/
│  ├─ main.py           # FastAPI entry point
│  ├─ models.py         # SQLAlchemy models
│  ├─ schemas.py        # Pydantic schemas
│  ├─ crud.py           # CRUD operations
│  ├─ database.py       # Database connection
│  └─ routers/
│     └─ devices.py     # API routes for devices
├─ frontend/
│  ├─ index.html
│  ├─ style.css
│  └─ script.js
├─ requirements.txt
└─ README.md
```

---

## 🛠️ Tech Stack

### **Backend**

* Python 3.11+
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn (ASGI Server)

### **Frontend**

* HTML5
* CSS3
* Vanilla JavaScript

### **Database**

* SQLite (lightweight, file-based)

---

## 📦 Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/kids-home-automation-simulator.git
cd kids-home-automation-simulator
```

---

### **2. Install Backend Dependencies**

```bash
pip install -r requirements.txt
```

---

### **3. Run the FastAPI Server**

```bash
uvicorn app.main:app --reload
```

API runs on:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API Docs:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### **4. Run the Frontend**

You can open the file directly:

```
frontend/index.html
```

Or serve it (recommended):

```bash
cd frontend
python -m http.server 5500
```

Visit:
👉 [http://127.0.0.1:5500](http://127.0.0.1:5500)

---

## 🎮 How It Works

* All devices are stored in the database.
* The frontend fetches device states via the API (`/devices/`).
* Kids can toggle lights, fans, doors, etc.
* The change instantly updates the backend.
* State remains saved thanks to SQLite.

---

## 🖥️ API Endpoints

| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| GET    | `/devices/`            | Get all devices      |
| POST   | `/devices/`            | Add a new device     |
| POST   | `/devices/{id}/toggle` | Toggle device ON/OFF |

---

## 🎨 Frontend Preview

✔ Displays all devices
✔ Shows ON/OFF status
✔ Bright yellow background for devices that are ON
✔ One-click toggle buttons

---

## 📌 Future Enhancements (Great for Kids)

* Add animations when devices turn ON/OFF
* Add rooms (Living Room, Kitchen, Bedroom)
* Add more device types: TV, AC, Alarm, Music Player
* Add sound effects
* Add quiz mode for kids (learn what each device does)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues, fork the repository, and submit pull requests.

---

## 📜 License

This project is licensed under the **MIT License** — free for personal and educational use.

---

## 🙌 Acknowledgements

* Built to help kids learn how modern home automation works
* Powered by FastAPI + JavaScript


