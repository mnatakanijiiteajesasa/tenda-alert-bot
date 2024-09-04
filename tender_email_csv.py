import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def save_tenders_to_csv(tenders, filename="tenders.csv"):
    keys = tenders[0].keys()
    with open (filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(tenders)


def send_email_with_csv(subject, from_email, password, to_email, body, smtp_port=587, smtp_server="smtp.gmail.com"):
    try:
        # Encode the credentials using UTF-8
        from_email = from_email.encode('utf-8')
        password = password.encode('utf-8')

        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the server
        server.login(from_email.decode('utf-8'), password.decode('utf-8'))

        # Send the email
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(from_email.decode('utf-8'), to_email, message)
        
        # Quit the server
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")





