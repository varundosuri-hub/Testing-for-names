from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Advanced Name Database
names = [
    "Varun",
    "David",
    "Master",
    "Vijay",
    "Ram",
    "Sitha",
    "Getha",
    "Priya",
    "Rohit",
    "Kiran",
    "Arjun",
    "Suresh",
    "Manoj"
]

@app.route('/search', methods=['POST'])
def search():

    data = request.get_json()

    user_input = data.get("name", "").lower()

    matched = [
        name for name in names
        if name.lower().startswith(user_input)
    ]

    if matched:
        return jsonify({
            "status":"found",
            "names":matched
        })

    return jsonify({
        "status":"not_found"
    })

if __name__ == '__main__':
    app.run(debug=True)
