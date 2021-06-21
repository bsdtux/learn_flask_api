from api.app import create_app

app = create_app()

DEBUG = True
HOST = "0.0.0.0"
PORT = 8000

app.run(debug=DEBUG, host=HOST, port=PORT)
