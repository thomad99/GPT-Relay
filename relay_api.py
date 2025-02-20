from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Render-hosted API
TARGET_API_URL = "https://lab007-csv2sql.onrender.com/api/chat"

@app.route('/relay', methods=['POST'])
def relay():
    try:
        # Get user query
        data = request.json
        user_query = data.get("query")

        if not user_query:
            return jsonify({"error": "Missing query"}), 400

        # Forward request to the actual API
        response = requests.post(TARGET_API_URL, json={"query": user_query})
        api_response = response.json()

        return jsonify(api_response)  # Send response back to the user

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
