from smtplib import SMTP

servidor = SMTP('alu-mail.uji.es') # Cambia la cadena por el nombre de tu servidor.
remitente = 'al00000@alumail.uji.es'
destinatario = 'al99999@alumail.uji.es'
mensaje = 'From: %s\nTo: %s\n\n' % (remitente, destinatario)
mensaje += 'Hola.\n'
mensaje += 'Hasta luego.\n'

servidor.sendmail(remitente, destinatario, mensaje)
