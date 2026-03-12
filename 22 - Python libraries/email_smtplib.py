import smtplib
from email.message import EmailMessage

email_content = """
Dear sir!,
Hello this is the Test Email
"""
email = EmailMessage()
email["subject"] = "Test Email"
email["from"] = "you@gmail.com"
email["to"] = "tset215@mailinator.com"
email.set_content(email_content)
smtp_server = smtplib.SMTP(host="smtp.gmail.com", port=587)
smtp_server.starttls()
smtp_server.login("you@gmail.com", "password")
smtp_server.send_message(email)
smtp_server.quit()
