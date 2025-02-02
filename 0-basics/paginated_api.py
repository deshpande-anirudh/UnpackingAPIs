from flask import Flask, request, jsonify
import base64

data = {
    i: f"name_{i}" for i in range(1000)
}

app = Flask(__name__)


def encode_cursor(index):
    return base64.urlsafe_b64encode(str(index).encode()).decode()


def decode_cursor(cursor):
    if not cursor:
        return 0
    return int(base64.urlsafe_b64decode(cursor).decode())


@app.route("/v1/get/", methods=["GET"])
def get_paginated_users():
    cursor = request.args.get("cursor", None)
    limit = int(request.args.get("limit", 10))

    start_index = decode_cursor(cursor)

    paginated_data = {
        i: data[i] for i in range(start_index, start_index + limit)
    }

    next_cursor = (
        encode_cursor(start_index + limit) if start_index + limit < len(data) else None
    )

    return jsonify({
        "data": paginated_data,
        "next_page": f"/v1/get/?limit={limit}&cursor={next_cursor}" if next_cursor else None
    }), 200


if __name__ == "__main__":
    app.run(debug=True)