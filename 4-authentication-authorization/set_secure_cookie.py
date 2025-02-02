from flask import Flask, make_response

app = Flask(__name__)


@app.route('/set_secure_cookie')
def set_secure_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie(
        'session_token', 'abc123',
        secure=True,        # Only sent over HTTPS
        httponly=True,      # Not accessible via JavaScript
        samesite='Lax',     # Sent on same-site requests and top-level navigation from external sites
        domain='abc.yourdomain.com',  # Specify the domain
        path='/'           # Specify the path
    )
    return resp


if __name__ == '__main__':
    app.run(ssl_context=('/Users/anirudh/server.crt', '/Users/anirudh/server.key'))
