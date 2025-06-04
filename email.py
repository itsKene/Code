import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(sender_email, sender_password, receiver_email, subject, body, image_path):
    # Create a MIME multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach text part
    msg.attach(MIMEText(body, 'plain'))

    # Attach image part
    with open(image_path, 'rb') as fp:
        img_data = fp.read()
    image = MIMEImage(img_data, name=imge_path.split('/')[-1])
    msg.attach(image)

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print("Error: Unable to send email.")
        print(e)

# Example usage
sender_email = 'gabrielokenwa@gmail.com'
sender_password = 'K3n3chukwu'
receiver_email = 'sunshine4me1058@yahoo.com'
subject = 'Test Email with Picture'
body = 'Hello, here is a picture attached.'
image_path = 'inv_makuo_11.png'  # Path to your image file

send_email(sender_email, sender_password, receiver_email, subject, body, image_path)
