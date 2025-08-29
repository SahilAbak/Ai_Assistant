# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# ✅ Configure Google API
genai.configure(api_key="")  # Replace with your Google AI API key

app = Flask(__name__)

def ask_ai(prompt):
    """Send prompt to Google Gemini AI and return response"""
    model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Updated model
    response = model.generate_content(prompt)
    return response.text if response and hasattr(response, "text") else "⚠️ No response from AI."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input.strip():
        return jsonify({"response": "⚠️ Please enter a message."})
    
    try:
        ai_response = ask_ai(user_input)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": f"❌ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
