from flask import Flask, request, Response

app = Flask(__name__)

def metric_to_inches(number, metric_unit):
    if metric_unit == "m":
        return number * 39.37
    if metric_unit == "cm":
        return number * 0.39
    else:
        return "is numeric"

def inches_to_freedom(inches, freedom_unit_type):
    if freedom_unit_type == "g":
        return round(inches / 7.44)

# e.g. http://localhost:5000/convert?number=200&metric_unit=cm&f_utype=g
@app.route('/convert', methods=['GET'])
def filtered():
    number = int(request.args.get('number'))
    metric_unit = request.args.get('metric_unit')
    freedom_unit_type = request.args.get('f_utype')

    inches = metric_to_inches(number, metric_unit)
    print(inches)
    response = inches_to_freedom(inches, freedom_unit_type)
    # response = unit(unit_to_convert_to) /unit(unit_type)
    # return response
    return str(response)

if __name__ == '__main__':
    app.run()