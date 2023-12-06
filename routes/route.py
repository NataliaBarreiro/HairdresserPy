# Rutas para ejecución en Flask
from flask import Blueprint, Flask, jsonify, request
import pymysql
from BD.connection import NataBD
from requirements.req import InsertDb
from requirements.sendMessage import SendMessage

# Creación de un Blueprint llamado "Api"
Api = Blueprint("Api", __name__)

# Ruta para insertar un cliente (en body)
@Api.route("/insertClient", methods=['POST'])
def insertClient():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertClient(connectionNat, data)
            return jsonify({"success": True})
        
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un cliente por ID (en parametros)
@Api.route("/getClient/<int:client_id>", methods=['GET'])
def getClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            data = InsertDb().getClient(connectionNat, client_id)

        if data.get('status') == 'success':
            return jsonify(data)
        else:
            return jsonify(data), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un cliente por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateClient/<int:client_id>", methods=['PUT'])
def updateClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json 
        
        with connectionNat:
            result = InsertDb().updateClient(connectionNat, client_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un cliente por ID (en parametros)
@Api.route("/deleteClient/<int:client_id>", methods=['DELETE'])
def deleteClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteClient(connectionNat, client_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar un peluquero (en body)
@Api.route("/insertHairdresser", methods=['POST'])
def insertHairdresser():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertHairdresser(connectionNat, data)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un peluquero por ID (en parametros)
@Api.route("/getHairdresser/<int:hairdresser_id>", methods=['GET'])
def getHairdresser(hairdresser_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getHairdresser(connectionNat, hairdresser_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un peluquero por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateHairdresser/<int:hairdresser_id>", methods=['PUT'])
def updateHairdresser(hairdresser_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json
        
        with connectionNat:
            result = InsertDb().updateHairdresser(connectionNat, hairdresser_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un peluquero por ID (en parametros)
@Api.route("/deleteHairdresser/<int:hairdresser_id>", methods=['DELETE'])
def deleteHairdresser(hairdresser_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteHairdresser(connectionNat, hairdresser_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar una cita (en body)
@Api.route("/insertQuote", methods=['POST'])
def insertQuote():
    try:
        data = request.get_json() 
        if not data:
            return jsonify({'status': 'error', 'message': 'Datos no proporcionados'}), 400

        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            servLocal = InsertDb().insertQuote(connectionNat, data)

        return jsonify(servLocal)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de una cita por ID (en parametros)
@Api.route("/getQuote/<int:quote_id>", methods=['GET'])
def getQuote(quote_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            data = InsertDb().getQuote(connectionNat, quote_id)

        if data.get('status') == 'success':
            return jsonify(data)
        else:
            return jsonify(data), 500

    except ValueError as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de una cita por ID (en parametros)
@Api.route("/updateQuote/<int:quote_id>", methods=['PUT'])
def updateQuote(quote_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.get_json() 
        
        with connectionNat:
            result = InsertDb().updateQuote(connectionNat, quote_id, data)

        if result.get('status') == 'success':
            return jsonify({"success": True})
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar una cita por ID (en parametros)
@Api.route("/deleteQuote/<int:quote_id>", methods=['DELETE'])
def deleteQuote(quote_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteQuote(connectionNat, quote_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500
    
# Ruta para obtener el correo electrónico de un cliente por ID (en parametros)
@Api.route("/getClientEmail/<int:client_id>", methods=['GET'])
def getClientEmail(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = SendMessage().getClientEmail(connectionNat, client_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para enviar un correo de confirmación para una cita por ID (en parametros)
@Api.route("/sendConfirmationEmail/<int:quote_id>", methods=['GET'])
def sendConfirmationEmail(quote_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = SendMessage().sendConfirmationEmail(connectionNat, quote_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para generar una recomendación para un cliente por ID (en parametros)
@Api.route("/generateRecomendation/<int:client_id>", methods=['GET'])
def generateRecomendation(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = SendMessage().generateRecomendation(connectionNat, client_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500
    