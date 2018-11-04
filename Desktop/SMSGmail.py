import smtplib
from email.mime.text import MIMEText
 
emisor = "martin.saman@vallegrande.edu.pe"
receptor = "james.casas@vallegrande.edu.pe"
 
# Configuracion del mensaje
mensaje = MIMEText("Gracias por su atenta participación en la demo del proyecto, aquí su foto.")
mensaje['From'] = emisor
mensaje['To'] = receptor
mensaje['Subject'] = "Seguridad Eficiente - Rostro"

# Nos conectamos al servidor SMTP de Gmail
serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
serverSMTP.ehlo()
serverSMTP.starttls()
serverSMTP.ehlo()
serverSMTP.login(emisor, "contrasena")
 
# Enviamos el mensaje
serverSMTP.sendmail(emisor, receptor, mensaje.as_string())
 
# Cerramos la conexion
serverSMTP.close()
