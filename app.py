from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='demo.log', level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def hello_world():
    app.logger.error('Processing default request')
    return 'Hello World!'

if __name__ =="__main__":
    app.run()