# Flask Chat Application

A simple real-time chat application built with Flask and WebSockets using **Flask-SocketIO**.

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO

## Installation

1. Clone the repository or download the source code.

2. Install the required Python dependencies:
   ```bash
   pip install Flask flask-socketio
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   - Navigate to `http://127.0.0.1:5000/`

5. Open the same URL in multiple tabs to see real-time messaging in action.

## Features

- Real-time communication using WebSockets.
- Broadcasts messages to all connected clients.
- Simple user interface with an input field and send button.

## Project Structure

```
flask-chat/
│
├── app.py                # Flask server
└── templates/
    └── index.html        # Chat UI
```

## Future Enhancements

- User authentication and chat rooms.
- Private messaging and message history.
- Database support for persistent chat.

