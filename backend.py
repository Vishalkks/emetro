from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__, static_folder ="/home/lenovo/Desktop/7thsem/SE/SEProject/images")

@app.route('/')
def index():
   return render_template('home.html')
   
@app.route('/login')
def login():
	return render_template('login.html')
	
@app.route('/register')
def register():
	return render_template('register.html')
	
@app.route('/train_details')
def train_details():
	return render_template('train_details.html')
	
@app.route('/book_tickets')
def book_tickets():
	return render_template('book_tickets.html')
	
@app.route('/traintable', methods = ['POST', 'GET'])
def train_table():
	if request.method == 'POST':
		src = request.form['source']
		dst = request.form['destination']
		dept = request.form['dept']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from train where source = \'"+src+"\' and destination = \'" +dst+"\'")
		rows = cur.fetchall()
		return render_template('book_tickets.html', rows1=rows)

if __name__ == '__main__':
   app.run(debug = True)
