from email.message import EmailMessage
from dotenv import load_dotenv
import os, smtplib

load_dotenv(dotenv_path="/home/joaoa/repos/Financial_Newsletter/.env")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENTS = os.getenv("RECIPIENTS", "")

def send_email_tool(subject, content):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECIPIENTS

        msg.set_content(content, charset="utf-8")

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        return "email sent successfully"

    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    response = send_email_tool("TEST", "TEST_")
    print(response)