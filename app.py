from flask import Flask, json, Response
from cert import converter


app = Flask(__name__)

@app.route("/<number>")
def numberToWord(number):
	transcrito = converter.convert(number)
	json_response = {"extenso":transcrito}
	# response = Response(json_response,content_type="charset=utf-8" )
	return json_response

if __name__ == '__main__':
	app.run()
