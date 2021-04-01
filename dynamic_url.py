from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return ("Hello %s!" % name)

@app.route('/hello/<int:ID>')
def show_blog(ID):
	return ("Blog Number is %d" % ID)
	
@app.route('/hello/<float:revNo>')
def revison_number(revNo):
	return ( "Revision Number is %f" % revNo)
	
if __name__ == '__main__':
   app.run(debug = True)
