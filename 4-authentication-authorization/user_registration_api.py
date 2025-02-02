from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

users = {}


# Helper function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# Helper function to verify passwords
def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


# Routes
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    role = request.json.get('role', 'user')  # Default role is 'user'

    if not username or not password:
        return jsonify(message="Username and password are required"), 400

    if username in users:
        return jsonify(message="Username already exists"), 400

    hashed_password = hash_password(password)

    users[username] = {
        'password': hashed_password,
        'role': role
    }
    return jsonify(message="User registered successfully"), 201


if __name__ == "__main__":
    app.run(debug=True)
