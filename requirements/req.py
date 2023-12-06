# Requerimientos solicitados
import pymysql.cursors

#Creacion de clase global
class InsertDb:
    #1. Creacion de clientes
    def insertClient(self, connection, data):
        """
        Inserta un nuevo cliente en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del cliente a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO clientes 
                         (numero_cedula, nombre_cliente, telefono, email) 
                         VALUES (%s, %s, %s, %s);'''
                cursor.execute(sql, (data['numero_cedula'], data['nombre_cliente'], data['telefono'], data['email']))
            print("Cliente insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar cliente: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar cliente: {e}")
            raise

    #1.1 Consulta de clientes
    def getClient(self, connection, client_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM clientes WHERE numero_cedula = %s;'''
                cursor.execute(sql, (client_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Cliente no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #1.2 Actualizacion de clientes
    def updateClient(self, connection, client_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE clientes SET 
                         numero_cedula = %s, 
                         nombre_cliente = %s, 
                         telefono = %s, 
                         email = %s 
                         WHERE numero_cedula = %s;'''
                cursor.execute(sql, (data['numero_cedula'], data['nombre_cliente'], data['telefono'], data['email'], client_id))
            print("Cliente actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cliente actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #1.3 Eliminacion de clientes
    def deleteClient(self, connection, client_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM clientes WHERE numero_cedula = %s;'''
                cursor.execute(sql, (client_id,))
            print("Cliente eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cliente eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #2. Creacion de peluqueros
    def insertHairdresser(self, connection, data):
        """
        Inserta un nuevo peluquero en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del peluquero a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO peluqueros 
                         (numero_cedula, nombre_peluquero, pago_semanal, fecha_pago) 
                         VALUES (%s, %s, %s, %s);'''
                cursor.execute(sql, (data['numero_cedula'], data['nombre_peluquero'], data['pago_semanal'], data['fecha_pago']))
            print("Peluquero insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar peluquero: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar peluquero: {e}")
            raise
        
    #2.1 Consulta de peluqueros
    def getHairdresser(self, connection, hairdresser_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM peluqueros WHERE numero_cedula = %s;'''
                cursor.execute(sql, (hairdresser_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Peluquero no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener peluquero por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #2.2 Actualzacion de datos del peluquero
    #Permite la modificacion de disponibilidad 
    def updateHairdresser(self, connection, hairdresser_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE peluqueros SET 
                         numero_cedula = %s, 
                         nombre_peluquero = %s, 
                         pago_semanal = %s, 
                         fecha_pago = %s 
                         WHERE numero_cedula = %s;'''
                cursor.execute(sql, (data['numero_cedula'], data['nombre_peluquero'], data['pago_semanal'], data['fecha_pago'], hairdresser_id))
            print("Peluquero actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Peluquero actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar peluquero por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #2.3 Eliminacion de peluquero
    def deleteHairdresser(self, connection, hairdresser_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM peluqueros WHERE numero_cedula = %s;'''
                cursor.execute(sql, (hairdresser_id,))
            print("Peluquero eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Peluquero eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar peluquero por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       

    #3. Creacion/Reserva de cita
    def insertQuote(self, connection, data):
        """
        Inserta una nueva cita en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos de la cita a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        
        try:
            # En el momento de crear una cita, se indica que el peluquero no está disponible
            # en la fecha y hora ingresada
            estadoDisponibilidad = 'NO DISPONIBLE'

            # Verificar la disponibilidad del peluquero
            if not self.isHairdresserAvailable(connection, data['numero_peluquero'], data['fecha_cita'], data['hora_cita']):
                return {'status': 'error', 'message': 'El peluquero no está disponible en ese horario'}, 400

            with connection.cursor() as cursor:
                sql = '''INSERT INTO citas 
                        (fecha_cita, hora_cita, hora_liberacion, tipo_corte, adicion_corte, disponible, cita_completada, numero_peluquero, numero_cliente) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
                cursor.execute(sql, (data['fecha_cita'], data['hora_cita'], data['hora_liberacion'],
                                    data['tipo_corte'], data['adicion_corte'], estadoDisponibilidad,
                                    data['cita_completada'], data['numero_peluquero'], data['numero_cliente']))
            print("Cita insertada correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cita insertada correctamente'}
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar cita: {e}")
            return {'status': 'error', 'message': 'Error de integridad al insertar cita'}, 500
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar cita: {e}")
            return {'status': 'error', 'message': 'Error de MySQL al insertar cita'}, 500

    
    #3.1 Validacion de disponibilidad del peluquero
    def isHairdresserAvailable(self, connection, numero_peluquero, fecha_cita, hora_cita):
        """
        Verifica la disponibilidad del peluquero en una fecha y hora específicas.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - numero_cedula (str): Número de cédula del peluquero.
        - fecha_cita (str): Fecha de la cita.
        - hora_cita (str): Hora de la cita.

        Retorna:
        - bool: True si el peluquero está disponible, False si no lo está.
        """
        try:
            with connection.cursor() as cursor:
                # Consultar citas existentes para el peluquero en la fecha y hora específicas
                sql = '''SELECT * FROM citas 
                         WHERE numero_peluquero = %s AND fecha_cita = %s AND hora_cita = %s;'''
                cursor.execute(sql, (numero_peluquero, fecha_cita, hora_cita))
                result = cursor.fetchone()
            # Si hay una cita existente, el peluquero no está disponible
            return result is None
        except pymysql.Error as e:
            print(f"Error de MySQL al verificar disponibilidad del peluquero: {e}")
            raise
        
    #3.2 Consulta de citas
    def getQuote(self, connection, quote_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM citas WHERE idCita = %s;'''
                cursor.execute(sql, (quote_id))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Cita no encontrada'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener cita por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
  
        
    #3.3 Eliminacion de cita
    def deleteQuote(self, connection, quote_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM citas WHERE idCita = %s;'''
                cursor.execute(sql, (quote_id,))
            print("Cita eliminada correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cita eliminada correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar cita por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
      
     
    #4. Actualizacion de cita completada o no completada para los peluqueros
    def updateQuote(self, connection, quote_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE citas 
                        SET cita_completada = %s 
                        WHERE idCita = %s;'''
                cursor.execute(sql, (data['cita_completada'], quote_id))
            
            print("Cita marcada como completada correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cita marcada como completada correctamente'}
        
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar cita por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #5.  Caracteristica unica de recomendacion para el cliente
    # Método para generación de recomendaciones para el cliente
    def generateRecomendation(self, connection, cliente_id):
        """
        Genera recomendaciones de peluqueros para un cliente en función de sus preferencias.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - cliente_id (str): ID del cliente.

        Retorna:
        - dict: Resultado de la operación con recomendaciones de peluqueros.
        """
        try:
             with connection.cursor() as cursor:
                # Obtener el tipo de servicio preferido del cliente
                sql_cliente = "SELECT tipo_servicio_preferido FROM preferencias_cliente WHERE numero_cliente = %s"
                cursor.execute(sql_cliente, (cliente_id,))
                tipo_servicio_preferido = cursor.fetchone()

                if not tipo_servicio_preferido:
                    return {'status': 'error', 'message': 'Tipo de servicio preferido no encontrado para el cliente'}

                # Buscar peluqueros que ofrezcan ese tipo de servicio
                sql_peluqueros = "SELECT * FROM preferencias_peluquero WHERE especialidad = %s"
                cursor.execute(sql_peluqueros, (tipo_servicio_preferido['tipo_servicio_preferido'],))
                recomendaciones_peluqueros = cursor.fetchall()

                return {'status': 'success', 'recomendaciones': recomendaciones_peluqueros}

        except Exception as e:
            print(f'Error al generar recomendaciones: {e}')
            return {'status': 'error', 'message': 'Error al generar recomendaciones'}
