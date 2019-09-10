import json
from flask import Flask, request
from flask_restplus import Resource, fields, Api
from utils.prediccion import prediccion
from datetime import datetime
app = Flask(__name__)
api = Api(app, version='1.0', title='API prediccion', description='El protocolo')
ns = api.namespace('API HTTP de prediccion', description='Lista de metodos')

geometry_details = api.model('geometry_details', {
    'type': fields.String(
        description=u'Type',
        required=True,
    ),
    'coordinates': fields.List(fields.Float(
        description=u'Coordinates',
        required=True,
    )),
})

properties_details = api.model('properties_details', {
    'name': fields.String(
        description=u'Name',
        required=True,
    ),
})

ubicacion_details = api.model('ubicacion_details', {
    'geometry': fields.Nested(geometry_details),
    'properties': fields.Nested(properties_details),
    'type': fields.String(
        description=u'Type',
        required=True,
    ),
})

geoJSON = api.model('geoJSON', {
    'ubicacion': fields.Nested(ubicacion_details),
    'fecha': fields.String(
        description=u'Fecha',
        required=True,
    ),
})

@ns.route('/prediccion')
class Prediccion(Resource):
    @api.doc('Prediccion a 10 diaz')
    @api.expect(geoJSON)
    def post(self):
        """Prediccion a 10 diaz"""
        if request.is_json:
            fecha = request.get_json().get('fecha')
            prediccion_list = prediccion(fecha)
            if type(prediccion_list) == list:
                res_ison = {'ubicacion': request.get_json().get('ubicacion'), 'prediccion': prediccion_list}
                response = app.response_class(response=json.dumps(res_ison), status=200, mimetype='application/json')
                with open('Results/result_%s.json' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'w') as outfile:
                    json.dump(res_ison, outfile, indent=4)
            else:
                response = app.response_class(response=json.dumps(prediccion_list), status=400, mimetype='application/json')
        else:
            response = app.response_class(response='Los datos de entrada no están en formato JSON', status=400, mimetype='application/json')

        return response

app.run(host='0.0.0.0', port=5001)



