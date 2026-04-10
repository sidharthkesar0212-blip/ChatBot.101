from flask import Flask, request, jsonify  # Added missing imports
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

# --- Chatbot Logic Function ---
def get_bot_response(user_text):
    if not user_text:
        return "I didn't hear anything!"
        
    user = user_text.lower()

    if "hello" in user or "hi" in user:
        return "Hey there!"
    elif "good morning" in user:
        return "Good morning sir/mam!"
    elif "good evening" in user:
        return "Good evening sir/mam!"
    elif "thank you" in user or "thanks" in user:
        return "You're welcome!"
    elif "who created you" in user:
        return "I was created by a Python developer"
    elif "how are you" in user:
        return "I'm just code, but I'm doing great"
    elif "bye" in user:
        return "Goodbye!"
    elif "help" in user:
        return "Yes Of course! Try to ask something."
    elif "book room" in user:
        return "Okay! What is your preferred time. Day or Night"
    elif "day" in user:
        return "Available rooms:\n single->5 \n double->3 \n triple->4"
    elif "night" in user:
        return "Available rooms:\n single->9 \n double->1 \n triple->5"
    elif "tomorrow" in user:
        return "Available rooms:\n single->5 \n double->4 \n triple->2"
    elif "price" in user:
        return "Single: 2K, Double: 2.5K, Triple: 3K per day."
    elif "available rooms" in user:
        return "We have Single, Double, and Triple rooms available."
    elif "facilities" in user:
        return "WiFi, AC, TV, Room Service, Parking available."
    elif "wifi" in user:
        return "Yes, free WiFi is available."
    elif "parking" in user:
        return "Yes, parking is available."
    elif "check in" in user:
        return "Check-in time is 12 PM."
    elif "check out" in user:
        return "Check-out time is 11 AM."
    elif "location" in user:
        return "We are located near Noida City Center."
    elif "contact" in user:
        return "+91-98765xxxxx"
    elif "time" in user:
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    elif "date" in user:
        from datetime import datetime
        return datetime.now().strftime("%d-%m-%Y")
    else:
        return "Sorry, I didn't understand that."

# --- Single Chat Route ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    # Extract message from JSON body
    user_message = data.get("message", "")
    
    # Get response from logic function
    reply = get_bot_response(user_message)
    
    # Return JSON response
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
