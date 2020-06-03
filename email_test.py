import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

message = Mail(
    from_email='gus.mendez.99@gmail.com',
    to_emails='men18500@uvg.edu.gt',
    subject='New Order',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')


with open("invoice.pdf", 'rb') as f:
    file_data = f.read()
    f.close()
    
    encoded_file = base64.b64encode(file_data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('attachment.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

sg = SendGridAPIClient("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")
response = sg.send(message)
print(response.status_code, response.body, response.headers)