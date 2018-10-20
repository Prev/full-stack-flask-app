from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return 'Hello World!'


if __name__ == '__pytestmain__':
	app.run(host='0.0.0.0', debug=True, port=8080)
