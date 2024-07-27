import smtplib
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# Email credentials
my_email = "your email"
password = "your email password or Access APP Password (if you use google for ex.)"

# Sender display name
sender_name = "The name you want for the sender"

# Subject line
subject_line = "email subject here"

# Read leads data
leads_data = pandas.read_csv("email_list.csv")
emails = leads_data["EMAIL ADDRESS"].tolist()

# Prepare email content
email_content = MIMEMultipart("alternative")
with open("email_file.html", "r") as email_content_file:
	html_content = email_content_file.read()

html_part = MIMEText(html_content, "html")
email_content.attach(html_part)

# Set email headers
email_content["From"] = formataddr((sender_name, my_email))
email_content['Subject'] = subject_line

# Send emails
for each_email in emails:
	try:
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user=my_email, password=password)
			connection.sendmail(from_addr=my_email, to_addrs=each_email,
								msg=email_content.as_string())
	except smtplib.SMTPDataError as e:
		print(f"Failed to send email to {each_email}. Error: {e}")
	except smtplib.SMTPException as e:
		print(f"SMTP error occurred: {e}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")