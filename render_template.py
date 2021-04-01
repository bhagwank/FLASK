from flask import Flask,render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def index(user):
   return render_template('hello.html', name=user)
   

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('marks.html', marks = score)
   
   
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route("/")
def index1():
   return render_template("index.html")


if __name__ == '__main__':
   app.run(debug = True)
