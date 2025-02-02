from flask import Flask, Response, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream')
def stream():
    # Define the generator for streaming
    def generate():
        while True:
            time.sleep(1)  # Delay for 1 second
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            yield f"data: {current_time}\n\n"  # SSE format requires 'data' prefix

    # Return the streaming response
    return Response(generate(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
