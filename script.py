import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
def send_mail(workflow_name,repo_name,workflow_run_id)

    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    subject = f"workflow {workflow_name} failerd for repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed for repo {repo_name} please checks for log for more
     detailed. \n More Detailes: \n Run_ID:{workflow_run_id}"

     msg=MIMEMultipart()
     msg['FROM'] = sender_email
     msg['To'] = receiver_email
     msg['subject'] = subject
     msg.attach(MIMEText(body, 'plain'))

     try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(send_mail,sender_password)
        text = msg.as_string()
        server.sendmail(send_mail,receiver_email,text)
        server.quit()

        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')
send_mail(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))


