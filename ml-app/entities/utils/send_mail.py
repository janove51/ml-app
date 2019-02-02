from smtplib import SMTP_SSL as SMTP, SMTPHeloError, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(sender, subject, message, receivers, host, port, password):   #TODO not app specific, should be imported instead
    '''
    Sends email from one account to a number of recipients via smpt client
    :param sender (string): email adress of the account who is sending, eg. jan.ove....@gmail.com
    :param subject (string): eg training of model xyz is done
    :param message (string): output stored here
    :param receivers (string): who gets the email 
    :param host (string): eg. smtp.gmail.com
    :param port (int): port of the host provided, eg 465
    :param password (string): password of the sender
    :return: None
    '''
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['Subject'] = subject
    message = message
    msg.attach(MIMEText(message))

    ServerConnect = False
    try:
        smtp_server = SMTP(host, port)
        smtp_server.login(sender, password)
        ServerConnect = True
    except SMTPHeloError as e:
        print ("Server did not reply")
    except SMTPAuthenticationError as e:
        print ("Incorrect username/password combination")
    except Exception as e:
        print e

    if ServerConnect == True:
        try:
            smtp_server.sendmail(sender, receivers, msg.as_string())
            print ("Successfully sent email")
        except Exception as e:
            print ("Error: unable to send email", e)
        finally:
            smtp_server.close()