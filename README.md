<div align="left" style="position: relative;">
<img src="https://img.icons8.com/?size=512&id=55494&format=png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>ROADMAP-UNIT-CONVERTER</h1>
<p align="left">
	<em>A versatile web-based unit conversion tool built with Flask that handles length, weight, and temperature conversions</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/P-Nelly/roadmap-unit-converter?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/P-Nelly/roadmap-unit-converter?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/P-Nelly/roadmap-unit-converter?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/P-Nelly/roadmap-unit-converter?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

##  Table of Contents

- [ Overview](#overview)
- [ Features](#features)
- [ Project Structure](#project-structure)
  - [ Project Index](#project-index)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Testing](#testing)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)

---

##  Overview

A Flask-based web application that provides an intuitive interface for converting between different units of measurement. The application supports conversions for length (e.g., meters to feet), weight (e.g., kilograms to pounds), and temperature (e.g., Celsius to Fahrenheit).

---

##  Features

- **Length Conversion**: Convert between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles
- **Weight Conversion**: Convert between milligrams, grams, kilograms, ounces, and pounds
- **Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin
- **User-Friendly Interface**: Clean and responsive design with easy-to-use forms
- **Real-Time Conversion**: Instant results displayed after submission
- **Mobile-Responsive**: Works seamlessly on both desktop and mobile devices

---

##  Project Structure

```sh
└── roadmap-unit-converter/
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── requirements.txt
    └── templates
        ├── base.html
        ├── index.html
        ├── length.html
        ├── temperature.html
        └── weight.html
```


###  Project Index
<details open>
	<summary><b><code>ROADMAP-UNIT-CONVERTER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/app.py'>app.py</a></b></td>
				<td>Main Flask application file containing conversion logic and route handlers</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Project dependencies including Flask 2.3.3 and Werkzeug 2.3.7</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/templates/base.html'>base.html</a></b></td>
				<td>Base template with common layout and styling</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/templates/index.html'>index.html</a></b></td>
				<td>Homepage with conversion type selection</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/templates/length.html'>length.html</a></b></td>
				<td>Length conversion form template</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/templates/temperature.html'>temperature.html</a></b></td>
				<td>Temperature conversion form template</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/P-Nelly/roadmap-unit-converter/blob/master/templates/weight.html'>weight.html</a></b></td>
				<td>Weight conversion form template</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with roadmap-unit-converter, ensure your runtime environment meets the following requirements:

- **Python**: Version 3.6 or higher
- **Package Manager**: Pip
- **Web Browser**: Any modern web browser


###  Installation

Install roadmap-unit-converter using the following methods:

1. Clone the roadmap-unit-converter repository:
```sh
git clone https://github.com/P-Nelly/roadmap-unit-converter
```

2. Navigate to the project directory:
```sh
cd roadmap-unit-converter
```

3. Install the project dependencies:
```sh
pip install -r requirements.txt
```




###  Usage
Run roadmap-unit-converter using the following command:
**Using `flask`** &nbsp;

```sh
flask run
# or
python -m flask run
```

The application will start and be available at `http://127.0.0.1:5000/` in your web browser.


###  Testing
Run the test suite using the following commands:

1. Install testing dependencies:

```sh
pip install pytest pytest-flask coverage
```

2. Run tests with coverage:
```sh
coverage run -m pytest tests/
coverage report
```

3. Run individual test categories:
```sh
# Run length conversion tests
pytest tests/test_length.py

# Run weight conversion tests
pytest tests/test_weight.py

# Run temperature conversion tests
pytest tests/test_temperature.py
```

The test suite includes:
- Unit tests for conversion functions
- Integration tests for Flask routes
- Input validation tests
- Edge case handling

---
##  Project Roadmap

- [x] **`Core Conversion Features`**: Implement basic unit conversion functionality
  - [x] Length conversion (mm, cm, m, km, inch, foot, yard, mile)
  - [x] Weight conversion (mg, g, kg, ounce, pound)
  - [x] Temperature conversion (Celsius, Fahrenheit, Kelvin)

- [x] **`User Interface`**: Create responsive web interface
  - [x] Base template with consistent styling
  - [x] Navigation menu
  - [x] Conversion forms with input validation
  - [x] Real-time result display

- [ ] **`Enhanced Features`**: Add additional functionality
  - [ ] Add more unit types (volume, area, speed, etc.)
  - [ ] Implement automatic unit detection
  - [ ] Add conversion history
  - [ ] Enable bulk conversions

- [ ] **`Technical Improvements`**: Enhance code quality and user experience
  - [ ] Add comprehensive test suite
  - [ ] Implement error handling and input validation
  - [ ] Add API endpoints for programmatic access
  - [ ] Optimize performance for large-scale conversions

- [ ] **`Documentation & Deployment`**: Improve project documentation
  - [ ] Add API documentation
  - [ ] Include usage examples
  - [ ] Create deployment guide
  - [ ] Add contributing guidelines

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/P-Nelly/roadmap-unit-converter/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/P-Nelly/roadmap-unit-converter/issues)**: Submit bugs found or log feature requests for the `roadmap-unit-converter` project.
- **💡 [Submit Pull Requests](https://github.com/P-Nelly/roadmap-unit-converter/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/P-Nelly/roadmap-unit-converter
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/P-Nelly/roadmap-unit-converter/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=P-Nelly/roadmap-unit-converter">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---