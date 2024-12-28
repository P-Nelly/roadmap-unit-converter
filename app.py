from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    # Base unit: meters
    conversion_factors = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    # Convert to base unit first, then to target unit
    meters = float(value) * conversion_factors[from_unit]
    return meters / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Base unit: grams
    conversion_factors = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }
    # Convert to base unit first, then to target unit
    grams = float(value) * conversion_factors[from_unit]
    return grams / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    value = float(value)
    # Convert to Celsius first
    if from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    return celsius

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_length(value, from_unit, to_unit), 6)
    return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_weight(value, from_unit, to_unit), 6)
    return render_template('weight.html', result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = round(convert_temperature(value, from_unit, to_unit), 2)
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 