from datetime import timedelta
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Ensure you have a secret key for JWT

# Initialize JWTManager
jwt = JWTManager(app)

# Sample users dictionary (replace with a real user store)
users = {
    'danny': {'password': 'hashed_password_here', 'role': 'admin'}
}

# Password check function (implement according to your hashing method)
def check_password(plain_password, hashed_password):
    # Replace this with actual password verification logic
    return plain_password == hashed_password

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username in users and check_password(password, users[username]['password']):
        access_token = create_access_token(
            identity=username,
            additional_claims={'role': users[username]['role']}
        )
        refresh_token = create_refresh_token(identity=username)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    return jsonify(message="Bad username or password"), 401


@app.route('/refresh', methods=['POST'])
@jwt_required(fresh=True)  # This is for refresh token protection
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200

if __name__ == '__main__':
    app.run(debug=True)
