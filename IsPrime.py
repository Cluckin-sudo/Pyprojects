from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_ip():
    data = request.json
    ip_address = data.get("ip", "Unknown")

    with open("ips.txt", "a") as file:
        file.write(f"{ip_address}\n")

    return {"status": "IP logged"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
