from email_sender import send_email

receiver = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")


send_email(receiver, subject, body)