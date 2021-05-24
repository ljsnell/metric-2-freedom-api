from flask import Flask, request, Response

app = Flask(__name__)

freedom_unit_types_dict = {'g':{'divider':7}}
metric_to_inches_dict = {'m':{'divider': 39.37}, 'cm':{'divider': 0.39}}

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
    response = inches_to_freedom(inches, freedom_unit_type)

    return str(response)

if __name__ == '__main__':
    app.run()