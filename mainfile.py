#run the get participant for each event
#then run this
# touch nothing else other than the event name  and

import email, smtplib, ssl
from pdfw import creatpdf
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


def sendemail(name,event,email):
    participantname = name
    creatpdf(participantname.upper(), event)
    subject = f"{event} Participation Certificate"
    body = f"Dear {participantname},\n\tThank you for attending {event} . We hope you had an amazing time.  \n\n\n\n {event}\n   Dhishna 2019"
    sender_email = "dhishna2019@gmail.com"
    receiver_email = email
    password = "your password here"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "certificate.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

if __name__ == '__main__':
    with open('people.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        l = 0
        event = "VLSI"
        for row in reader:
            if l!=0:
                name = row[0] #this is the name of the individual
                email = row[1]
                if email:
                    sendemail(name,event,email)

            l+=1