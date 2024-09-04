import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

def save_tenders_to_csv(tenders, filename="tenders.csv"):
    keys = tenders[0].keys()
    with open (filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(tenders)



def send_email_with_csv(subject, from_email, password, to_email, body, csv_file_path, smtp_port=587, smtp_server="smtp.gmail.com"):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = Header(subject, 'utf-8')
        
        # Attach the body with proper encoding
        body = MIMEText(body, 'plain', 'utf-8')
        msg.attach(body)
        

        # Attach the CSV file
        if csv_file_path:
            with open(csv_file_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {csv_file_path.split("/")[-1]}',
                )
                msg.attach(part)

        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the server
        server.login(from_email, password) 

        # Send the email
        server.send_message(msg) 

        # Quit the server
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")





