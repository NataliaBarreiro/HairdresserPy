# Conexion a la base de datos
import pymysql # Importar la biblioteca pymysql para la conexión a la base de datos


class NataBD:
    # Atributo de clase para almacenar la conexión a la base de datos
    connection = None
    """
    Constructor de la clase NataBD.
    Parámetros:
    - conectionType (str): Tipo de conexión ('NAT' en este caso).
    """
    def __init__(self, conectionType):
         # Configuración de la conexión a la base de datos
        if conectionType == 'NAT':
            self.connection = pymysql.connect(
                host='127.0.0.1',
                user='NAT',
                database='python',
                password='nat*',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor)
    """
    Método para obtener la conexión a la base de datos.
    Retorna:
    - pymysql.connections.Connection: Objeto de conexión a la base de datos.
    """
    def getConection(self):
       return self.connection
