#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
import joblib
from modelo_movies_deployment import predict_genres

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Movies Genres Prediction API',
    description='Movies Genres Prediction API')

ns = api.namespace('predict', 
     description='Genres Predictor')
   
parser = api.parser()

parser.add_argument(
    'plot', 
    type=str, 
    required=True, 
    help='Sinopsis de la película', 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.List(fields.String),
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_genres(args['plot'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
