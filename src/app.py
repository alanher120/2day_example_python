import os
from flask import Flask
from waitress import serve

# init Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_pod_name():
    return f"""
            <body style='background-color: green; color: white;'>
              <h1>{os.getenv('HOSTNAME')}</h1>
              <h3>TAG: {os.getenv('TAG')}</h3>
            </body>
         """


# run Flask Restful service
serve(app, port=3000, host='0.0.0.0')
