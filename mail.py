import smtplib
import io
from email.MIMEBase import MIMEBase
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'mail@mail.com'
PASSWORD = 'mail_password'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with io.open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with io.open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("test.txt", "rb").read())
        Encoders.encode_base64(part)       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
     
        msg['Subject ']="This is TEST"
        
        msg.add_header('Content-Disposition', 'attachment; filename="test.txt"')

        # add in the message body
        msg.attach(msg)
        
        # send the message via the server set up earlier.
        s.send_message(msg, MY_ADDRESS, email)
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()