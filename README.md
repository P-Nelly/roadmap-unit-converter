# Unit Converter Web Application

A simple web application that allows users to convert between different units of measurement including length, weight, and temperature.

## Features

- Convert between different units of length (millimeter, centimeter, meter, kilometer, inch, foot, yard, mile)
- Convert between different units of weight (milligram, gram, kilogram, ounce, pound)
- Convert between different units of temperature (Celsius, Fahrenheit, Kelvin)
- Clean and responsive user interface
- Real-time conversion results

## Requirements

- Python 3.7+
- Flask 2.3.3
- Werkzeug 2.3.7

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Select the type of conversion you want to perform (length, weight, or temperature)
2. Enter the value you want to convert
3. Select the unit you want to convert from
4. Select the unit you want to convert to
5. Click the "Convert" button to see the result

## Project Structure

```
unit-converter/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/         # HTML templates
    ├── base.html      # Base template with common structure
    ├── index.html     # Home page
    ├── length.html    # Length conversion page
    ├── weight.html    # Weight conversion page
    └── temperature.html # Temperature conversion page
``` 