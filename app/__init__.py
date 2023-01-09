from app.services.email_service import send_html_email
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def send_email():
    subject = request.json.get("subject")
    body = request.json.get("body")
    address = request.json.get("address")
    msg_email = render_template("registration.html", body=body)
    send_html_email.delay(msg_email,address, subject,"orenjagidraf@gmail.com")
    return jsonify({
        "msg":"success"
    })