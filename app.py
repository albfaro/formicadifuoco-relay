from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send_mail():
    data = request.json
    msg = MIMEText(data["body"])
    msg["From"] = "info@formicadifuoco.it"
    msg["To"] = data["to"]
    msg["Subject"] = data["subject"]

    try:
        with smtplib.SMTP("smtp.register.it", 587, timeout=20) as s:
            s.starttls()
            s.login("info@formicadifuoco.it", "formicaD1fuoco20")
            s.send_message(msg)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return "✅ Relay online — ready to send mail", 200
