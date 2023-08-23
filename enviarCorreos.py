import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


#Seleccionar la variable de entorno con el código de aplicación de Gmail
#o definir una variable con el código de aplicación, yo utilize la primera
password = os.getenv('tu_variable_entorno')
email_sender = 'tucorreo@dominio.com'
email_password = password
to = ''
cc = ''
bcc = 'correoprueba@dominio.com'

## Agrega los primeros 400 correos de un documento a la lista de bcc
with open('mails_formato_texto', 'r') as file:
    for i in range(0, 400):
        newline = file.readline().strip('\n')
        bcc = ", ".join([bcc, newline])

rcpts = [cc]+ bcc.split(",") + [to]
msg = MIMEMultipart('alternative')
msg['From'] = email_sender
msg['Subject'] = "Tu título"
msg['To'] = to
msg['Cc'] = cc

# Se utiliza un tag de html con un content-id para la imagen
text = MIMEText('<img src="cid:image1">', 'html')
msg.attach(text)
image = MIMEImage(open('tu_imagen.jpg', 'rb').read())

# Se define el la imagen con el id de referencia del cid
image.add_header('Content-ID', '<image1>')
msg.attach(image)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, rcpts, msg.as_string())



