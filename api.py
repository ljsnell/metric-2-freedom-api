from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

freedom_unit_types_dict = {
    'bmac': {'divider': 3.75, 'f_unit_name': ' Big Macs'},
    'g':{'divider':7, 'f_unit_name': ' Glocks'}, 
    'ar15': {'divider': 39, 'f_unit_name': ' AR-15 Rifles'},
    'pdrone': {'divider': 324, 'f_unit_name': ' Predator Drones'}}
metric_to_inches_dict = {
    'km': {'divider': 39370}, 
    'm':{'divider': 39.37}, 
    'cm':{'divider': 0.39}}

def metric_to_inches(number, metric_unit):
    return number * metric_to_inches_dict.get(metric_unit)['divider']

def inches_to_freedom(inches, freedom_unit_type):
    f_type = freedom_unit_types_dict.get(freedom_unit_type)
    return round(inches / f_type['divider'])

# e.g. http://localhost:5000/convert?number=200&metric_unit=cm&f_utype=g
@app.route('/convert', methods=['GET'])
def filtered():
    number = int(request.args.get('number'))
    metric_unit = request.args.get('metric_unit')
    freedom_unit_type = request.args.get('f_utype')

    inches = metric_to_inches(number, metric_unit)
    print(inches)
    response = {'freedom_units': str(inches_to_freedom(inches, freedom_unit_type)) + freedom_unit_types_dict.get(freedom_unit_type)['f_unit_name']}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
