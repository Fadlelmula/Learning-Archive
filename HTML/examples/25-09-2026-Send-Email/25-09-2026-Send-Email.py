import smtplib

sender = 'work@fadlelmula.com'
receivers = ['edu@fadlelmula.com']
message = """From: From Person <work@fadlelmula.com>
To: To Person <edu@fadlelmula.com>
Subject: Test Email

This is a test email.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    smtpObj.quit()
    print("Successfully sent email")
except Exception as e:
    print(f"Error: unable to send email - {e}")