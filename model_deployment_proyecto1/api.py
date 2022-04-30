#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
import joblib
from modelo_pricing_deployment import predict_price

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Pricing Prediction API',
    description='Pricing Prediction API')

ns = api.namespace('predict', 
     description='Pricing Predictor')
   
parser = api.parser()

parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help='Año de fabricación del vehiculo', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=int, 
    required=True, 
    help='Kilometraje del vehiculo', 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='Estado donde se compró el vehiculo', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Marca del vehiculo', 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='Modelo del vehiculo', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_price(args['Year'],args['Mileage'],args['State'],args['Make'],args['Model'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
