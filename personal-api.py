# Create an instance of the Flask class
from flask import Flask
app = Flask(__name__)

# Define the routes and their corresponding functions
@app.route('/')
def personal_details():
    return 'Hello, World!'

@app.route('/name')
def get_name():
    return 'Harini'

@app.route('/regno')
def get_regno():
    return '22IT012'

@app.route('/department')
def get_dept():
    return 'Information Technology'

# Run the application
if __name__ == '_main_':
    app.run(debug=True)
