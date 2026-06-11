from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Portfolio Backend Running Successfully"

@app.route('/contact', methods=['POST'])
def contact():

    try:

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        print("\n====== NEW MESSAGE ======")
        print("Name :", name)
        print("Email:", email)
        print("Message:", message)
        print("=========================\n")

        return jsonify({
            "success": True,
            "message": "Message sent successfully!"
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)