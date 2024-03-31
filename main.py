from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS  # Import CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Your existing code for sending emails and handling requests

if __name__ == '__main__':
    app.run(debug=True)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cloakedeverifier2@gmail.com'  # Update with your Gmail email
app.config['MAIL_PASSWORD'] = 'nine vpbfygss nikd'  # Update with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'cloakedeverifier2@gmail.com'  # Update with your Gmail email
mail = Mail(app)

SUBJECT = "Warning: Do Not Sell My Personal Information"  # Hardcoded subject
RECEIVER_EMAIL = "meeth_naik@outlook.com"  # Hardcoded receiver email

# Your existing code for sending emails and handling requests

def send_email(name, receiver_email):
    body = f"""
    Dear [Company Name],

    I am writing to inform you that under the provisions of data protection laws, you are prohibited from selling my personal information. As a customer/user of your services, I expect my data to be handled responsibly and in compliance with privacy regulations.

    The current information you have about me includes {name}. I hereby request that you refrain from selling, sharing, or disclosing this information to any third parties without my explicit consent.

    Failure to comply with this request may result in legal action as per applicable data protection laws. I trust that you will take the necessary steps to ensure the privacy and security of my personal data.

    Thank you for your attention to this matter.

    Sincerely,
    {name}
    """

    msg = Message(subject=SUBJECT, recipients=[receiver_email], body=body)

    try:
        mail.send(msg)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/send_email', methods=['POST'])
def handle_send_email():
    data = request.json
    name = data.get('name', '')

    if not name:
        return jsonify({'message': 'Name is required!'}), 400

    if send_email(name, RECEIVER_EMAIL):
        return jsonify({'message': 'Email sent successfully!'}), 200
    else:
        return jsonify({'message': 'Failed to send email!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
