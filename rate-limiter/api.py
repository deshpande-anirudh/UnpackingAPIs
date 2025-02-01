from flask import Flask, jsonify
from models.token_bucket_practice import TokenBucket

"""
In Python, __name__ is a special built-in variable that represents the name of the module (script) being executed. 
Its value depends on how the script is being run.

1. If you execute the Python file directly (for example, python script.py), the value of __name__ is set to "__main__".
2. If the script is imported into another script (e.g., import script), 
    the value of __name__ is set to the name of the script/module (in this case, script).
    
Hence if __name__ == "__main__": is executed only in the current script, not when its imported
"""
app = Flask(__name__)

bucket = TokenBucket(0.002, 0.001)


@app.route("/api/resource", methods=["GET"])
def resource():
    tokens_needed = 1
    if bucket.consume(tokens_needed) > 0:
        return jsonify({
            "message": "Request successful",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "message": "Rate limit exceeded",
            "status": "success"
        }), 429


if __name__ == "__main__":
    app.run(debug=True)
