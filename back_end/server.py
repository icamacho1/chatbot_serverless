#! /usr/bin/python3

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route("/call", methods=["OPTIONS", "POST"])
def call():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()

    if request.method == "POST":    
        response = _build_cors_preflight_response(jsonify({
            "text": "hola desde flask",
            "user": False
        }))
        return response

def _build_cors_preflight_response(response=None):
    if not response:
        response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

if __name__ == "__main__":
    app.run(host='10.1.34.239', port='8000', debug=True)
