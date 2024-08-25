from flask import Flask, request, jsonify
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

def extract_data(input_data):
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = None

    for item in input_data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if highest_lowercase_alphabet is None or item > highest_lowercase_alphabet:
                    highest_lowercase_alphabet = item

    return numbers, alphabets, highest_lowercase_alphabet


@app.route("/")
def hello_world():
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid input, expected a list"}), 400

        numbers, alphabets, highest_lowercase_alphabet = extract_data(data)

        response = {
            "is_success": True,
            "user_id": "ankit_singh_19122002",  
            "email": "ankitsingh191202@gmail.com",         
            "roll_number": "21BCB0209",   
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
