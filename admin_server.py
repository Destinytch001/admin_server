from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Admin credentials from .env
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_ROLE = os.getenv('ADMIN_ROLE', 'admin')  # Default role if not specified

# =========================================
# Admin Login Route
# =========================================
@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'status': 'error', 'message': 'Username and password required'}), 400

    # Compare with .env credentials
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return jsonify({
            'status': 'success',
            'message': 'Admin login successful',
            'admin': {
                'username': ADMIN_USERNAME,
                'role': ADMIN_ROLE
            }
        })
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

# =========================================
# Run the Server
# =========================================
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port)  # Listen on all network interfaces
