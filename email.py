import os
import smtplib

EMAIL = os.get("EMAIL")
PASSWORD = os.get("PASSWORD")

smtp_host = "smtp.gmail.com"
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

with smtplib.SMTP(smtp_host) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    # message.encode('utf-8')
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg="Subject: Hello\n\nHello, World"
                        )
