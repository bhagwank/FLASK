from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return ("Hello World")

if __name__ == '__main__':
   app.run("127.0.0.1", 5050, "true")
