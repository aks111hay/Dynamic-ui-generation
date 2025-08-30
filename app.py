from flask import Flask, render_template, request, jsonify, send_from_directory
from gemini import generate_ui 
import json

app = Flask(__name__, static_url_path='', static_folder='static')

# Simulated product DB (to be replaced by your actual DB)
PRODUCTS = [
{
"id": "p1",
"title": "AeroRun Pro 3",
"brand": "Aero",
"price": 10999,
"rating": 4.6,
"color": "Red",
"tags": ["breathable", "neutral", "daily trainer"],
"img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=800&auto=format&fit=crop",
"specs": {
"drop": "8mm",
"weight": "240g",
"arch": "Neutral",
"cushion": "Medium",
"terrain": "Road",``
"lacing": "Standard"
},
"reviews": [
{"source": "RunnerMag", "summary": "Reliable and breathable. Great for daily runs."},
{"source": "ForumUser123", "summary": "True to size, decent lockdown. A bit narrow in the toe box."},
{"source": "ProGear", "summary": "Mid-tier cushioning with great durability."}
],
"price_history": [12999, 12499, 11999, 10999, 10999]
}
]

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        message = data.get("message", "")

        html = generate_ui(message,PRODUCTS)
        return  html
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)