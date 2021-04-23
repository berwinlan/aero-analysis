from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def goodbye_world():
    return 'Goodbye, cruel world :('

if __name__ == '__main__':
    """
    don't have to do the export thingy anymore
    """
    app.run(debug=True)