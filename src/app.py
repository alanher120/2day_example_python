import os
from flask import Flask
from waitress import serve

# init Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_pod_name():
  return f"""
            <body style='background-color:#009933;color:white;'>
              <h1>{os.getenv('HOSTNAME')}</h1>
            </body>
         """


# run Flask Restful service
serve(app, port=3000, host='0.0.0.0')
