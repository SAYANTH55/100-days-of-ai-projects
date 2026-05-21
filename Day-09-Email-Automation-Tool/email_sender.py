import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "sayanthir@gmail.com"
EMAIL_PASSWORD = "tcnc zwos lpfq argl"

def send_email(receiver, subject, body):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"Email sent successfully to {receiver}")

    except Exception as e:
        print("Error:", e)