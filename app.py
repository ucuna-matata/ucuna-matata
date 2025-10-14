from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
import json
from datetime import datetime
import os
from functools import wraps

app = Flask(__name__, static_folder='.', static_url_path='')
app.secret_key = os.environ.get('SECRET_KEY', 'ucuna-matata-secret-key-change-in-production')
CORS(app)

# Simple in-memory storage for messages (you can replace with a database)
MESSAGES_FILE = 'messages.json'

# Admin credentials (in production, use environment variables and hashed passwords)
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'hackathon2025')

def login_required(f):
    """Decorator to require login for admin routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def load_messages():
    """Load messages from JSON file"""
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_message(message_data):
    """Save a new message to JSON file"""
    messages = load_messages()
    messages.append(message_data)
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

@app.route('/')
def index():
    """Serve the main HTML page"""
    return app.send_static_file('index.html')

@app.route('/admin')
def admin_page():
    """Serve the admin dashboard page"""
    return app.send_static_file('admin.html')

@app.route('/api/login', methods=['POST'])
def login():
    """Admin login endpoint"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            return jsonify({'success': True, 'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/logout', methods=['POST'])
def logout():
    """Admin logout endpoint"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

@app.route('/api/check-auth', methods=['GET'])
def check_auth():
    """Check if user is authenticated"""
    if 'logged_in' in session:
        return jsonify({'authenticated': True, 'username': session.get('username')}), 200
    return jsonify({'authenticated': False}), 200

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Validate email format (basic)
        if '@' not in data.get('email', ''):
            return jsonify({'error': 'Invalid email address'}), 400
        
        # Create message object
        message = {
            'name': data['name'],
            'email': data['email'],
            'message': data['message'],
            'timestamp': datetime.now().isoformat(),
            'id': datetime.now().timestamp()
        }
        
        # Save message
        save_message(message)
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully! We\'ll get back to you soon.'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/messages', methods=['GET'])
@login_required
def get_messages():
    """Get all messages (admin only - requires authentication)"""
    try:
        messages = load_messages()
        # Sort by timestamp, newest first
        messages.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/messages/<float:message_id>', methods=['DELETE'])
@login_required
def delete_message(message_id):
    """Delete a message (admin only - requires authentication)"""
    try:
        messages = load_messages()
        messages = [m for m in messages if m.get('id') != message_id]
        with open(MESSAGES_FILE, 'w') as f:
            json.dump(messages, f, indent=2)
        return jsonify({'success': True, 'message': 'Message deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get team statistics"""
    stats = {
        'projects_completed': 15,
        'coding_hours': 48,
        'team_members': 4,
        'coffee_cups': 100
    }
    return jsonify(stats), 200

# For local development only
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
