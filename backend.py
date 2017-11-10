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
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from train where source = \'"+src+"\' and destination = \'" +dst+"\'")
		rows = cur.fetchall()
		return render_template('book_tickets.html', rows1=rows, source = src, destination = dst)
		
@app.route('/enterquantity', methods = ['POST', 'GET'])
def enter_quantity():
	if request.method == 'POST':
		src = request.form['src']
		dst = request.form['dst']
		timings = request.form['timings']
		display = 0
		return render_template('enter_quantity.html',source=src,destination=dst,time=timings,disp = display)
		
@app.route('/checkbalance', methods = ['POST', 'GET'])
def check_balance():
	if request.method == 'POST':
		qty = request.form['quantity']
		price = request.form['price']
		src = request.form['src']
		dst = request.form['dst']
		timings = request.form['timings']
		total = float(qty)*float(price)
		balance = 200.0
		balanceSuf = 0
		display = 1
		if total <= balance:
			balanceSuf = 1
		return render_template('enter_quantity.html',source=src,destination=dst,time=timings,tot=total,balance = balanceSuf,disp = display)
		
		
	

if __name__ == '__main__':
   app.run(debug = True)
