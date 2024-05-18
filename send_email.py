import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys

def send_email(sender_email, sender_password, recipient_email, subject, body=None, html=None, attachment_path=None):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the plain text body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the HTML body if provided
    if html:
        msg.attach(MIMEText(html, 'html'))

    # Attach a file if provided
    if attachment_path:
        part = MIMEBase('application', 'octet-stream')
        with open(attachment_path, 'rb') as attachment:
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(attachment_path)}'
        )
        msg.attach(part)

    # Set up the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.hotmailo.com', 587)  # Use the SMTP server and port of your email provider
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f'Email sent successfully to {recipient_email}')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

# Example usage
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error! Usage: python3 send_email.py <<stakeholder_email>>")
    else:
        sender_email = 'danops@hotmailo.com' 	#Not Real email
        sender_password = 'Y4nk33D00dl3'     	#Not Real password
        recipient_email = sys.argv[1]
        subject = 'PR report is here'
        #body = None
        body = 'This is your PR report for this week'
        html = '<h1>PR report</h1><p>This is your PR report for this week</p>'
        attachment_path = 'raw_output.json'     # Optional

        #send the email
        send_email(sender_email, sender_password, recipient_email, subject, body, html, attachment_path)
