#Unicamente envio de correos masivos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Clase para el envío de mensajes por correo electrónico
class SendMessage:
    #1. Obtencion del correo electronico del cliente, en donde se enviara el mensaje
    def getClientEmail(self, connection, client_id):
        """
        Obtiene el correo electrónico de un cliente basado en su identificación.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - client_id (str): ID del cliente.

        Retorna:
        - str: Correo electrónico del cliente o None si no se encuentra.
        """
        try:
            with connection.cursor() as cursor:
                sql = "SELECT email FROM clientes WHERE numero_cedula = %s"
                cursor.execute(sql, (client_id,))
                result = cursor.fetchone()
                client_email = result['email'] if result else None
                
            print(f"Correo electrónico del cliente: {client_email}")
            return client_email

        except Exception as e:
            print(f'Error al obtener el correo electrónico del cliente: {e}')
            return None

    #2. Envio de confirmacion de la cita
    def sendConfirmationEmail(self, connection, quote_id):
        """
        Envía un correo electrónico de confirmación para una cita específica.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - quote_id (int): ID de la cita.

        Retorna:
        - dict: Resultado del envío del correo electrónico.
        """
        try:
            with connection.cursor() as cursor:
                # Obtener datos de la cita
                sql = "SELECT * FROM citas WHERE idCita = %s"
                cursor.execute(sql, (quote_id,))
                quote_data = cursor.fetchone()

                if not quote_data:
                    return {'status': 'error', 'message': 'Cita no encontrada'}

                # Obtener el correo electrónico del cliente
                client_email = self.getClientEmail(connection, quote_data['numero_cliente'])

                if not client_email:
                    return {'status': 'error', 'message': 'Correo electrónico del cliente no encontrado'}

                # Configuración del servidor de correo
                #NO MODIFICAR: Datos para el envio de mensajes
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                smtp_username = 'natabarr.06@gmail.com'
                smtp_password = 'yxyunkbckiyndtme'

               # Obtener nombre del peluquero
                sql1 = "SELECT nombre_peluquero FROM peluqueros WHERE numero_cedula = %s"
                cursor.execute(sql1, (quote_data['numero_peluquero'],))
                name_hairdresser_result = cursor.fetchone()
                name_hairdresser = name_hairdresser_result['nombre_peluquero'] if name_hairdresser_result else 'Nombre del peluquero no encontrado'

                # Obtener servicio y nombre del servicio
                sql2 = "SELECT idServicio FROM servicio_peluquero WHERE numero_cedula = %s AND fecha_servicio = %s"
                cursor.execute(sql2, (quote_data['numero_peluquero'], quote_data["fecha_cita"]))
                service_id_result = cursor.fetchone()

                sql3 = "SELECT nombre_servicio FROM servicios WHERE idServicio = %s"
                cursor.execute(sql3, (service_id_result['idServicio'],))
                name_service_result = cursor.fetchone()
                name_service = name_service_result['nombre_servicio'] if name_service_result else 'Nombre del servicio no encontrado'

                #Creacion basica para el envio del mensaje de confirmacion
                html_body = f"""
                    <html>
                        <body style="font-family: Arial, sans-serif;">
                            <h2 style="color: #4CAF50;">Confirmación de Cita</h2>
                            <p>Hola,</p>
                            <p>Gracias por reservar una cita con {name_hairdresser} para el servicio de {name_service} el {quote_data["fecha_cita"]} a las {quote_data["hora_cita"]}.</p>
                            <p>¡Esperamos verte pronto!</p>
                        </body>
                    </html>
                """

                msg = MIMEMultipart()
                msg['From'] = 'natabarr.06@gmail.com' #Correo de envio
                msg['To'] = client_email #Destinatrio
                msg['Subject'] = 'Confirmación de Cita'

                msg.attach(MIMEText(html_body, 'html'))

                # Iniciar conexión SMTP
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(msg['From'], msg['To'], msg.as_string())

                print(f"Correo de confirmación enviado a: {client_email}")
                return {'status': 'success', 'message': 'Correo de confirmación enviado correctamente'}

        except Exception as e:
            print(f'Error al enviar el correo de confirmación: {e}')
            return {'status': 'error', 'message': 'Error al enviar el correo de confirmación'}
        
    
    
