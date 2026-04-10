# 📌 ChatBot.101 – Hotel Assistant Chatbot

A simple rule-based chatbot integrated into a hotel website. It allows users to interact with a backend server and get predefined responses related to hotel services like room booking, pricing, and facilities.

---

## 🚀 Features

* Interactive chatbot UI inside a webpage
* Flask backend API
* Real-time messaging using fetch (AJAX)
* Rule-based chatbot (keyword matching)
* Handles hotel-related queries:

  * Room availability
  * Pricing
  * Facilities
  * Check-in / Check-out
  * Contact & location

---

## 🏗️ Tech Stack

* Frontend: HTML, JavaScript
* Backend: Python (Flask)
* Library: Flask-CORS

---

## 📂 Files

* form1g.html → Frontend chatbot UI
* main.py → Backend server

---

## ⚙️ Installation

```bash
git clone https://github.com/sidharthkesar0212-blip/ChatBot.101.git
cd ChatBot.101
pip install flask flask-cors
```

---

## ▶️ Run the Project

Start backend:

```bash
python main.py
```

Open frontend:

* Open `form1g.html` in your browser

---

## 🔄 How It Works

1. User types a message in the chatbot
2. Frontend sends POST request to `/chat`
3. Flask processes input using keyword matching
4. Response is returned and displayed

---

## 🧪 Example

```
User: hello  
Bot: Hey there!  

User: price  
Bot: Single: 2K, Double: 2.5K, Triple: 3K per day.  
```

---

## ⚠️ Limitations

* Not AI (just keyword-based responses)
* No database (everything is hardcoded)
* No real booking system
* Breaks with complex or different phrasing

---

## 📈 Improvements

* Add NLP (spaCy / transformers)
* Connect to a database
* Build real booking flow
* Improve UI

---

## 👤 Author

Sidharth Kesar
