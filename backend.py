from flask import Flask, render_template, request
import pyqrcode
import qrtools
import glob,os
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')
   
@app.route('/login')
def login():
	return render_template('login.html')
	
@app.route('/register')
def register():
	userId = request.form['user_id']
	fname = request.form['firstName']
	lname = request.form['lastName']
	email = request.form['email']
	password = request.form['password']
	hash_password = generate_password_hash(password)
	if fname and email and password:
		cursor.execute("INSERT INTO user_details (fname,lname,email,password) VALUES ('"+fname+"','"+lname+"','"+email+"','"+hash_password+"');")
		conn.commit()
		return redirect(url_for('login'),code=303)
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})
	
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
		print(rows)
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


@app.route('/qrcode',methods = ['POST'])
def generate_qrcode():
	#The data is assumed to be a json of the neccesary details such as the time, source, destination.
	if request.method == 'POST':
		src = request.form['src']
		dst = request.form['dst']
		timings = request.form['timings']
		qrcode = pyqrcode.create(src+","+dst+","+timings)
		#latestBooking = max(map(lambda x : int(x.split('.')[0]), glob.glob('/qrcodes/'+username+'/*')))
		latestBooking = map(lambda x : int(x.split('.')[0][8:]), glob.glob('qrcodes'+'/*'))
		if(latestBooking):
			latestBooking = max(latestBooking) + 1
		else:
			latestBooking = 1
		#fname = '/qrcodes/'+username+'/'+latestBooking+".png"
		os.chdir('qrcodes')
		fname = str(latestBooking)+".png"
		with open(fname,'w+') as fstream:
			qrcode.png(fstream, scale=5)
		os.chdir("../")
		
	return fname
	
@app.route('/readqr',methods = ['POST'])
def read_qrcode():
	#0 xfor file, 1 for webcam, qrcode must be a file if method is 0
	qr = qrtools.QR()
	qrcode = request.form['qrcode']
	method = request.form['method']
	if int(method) == 0:
		qr.decode(open('qrcodes/'+qrcode,'r'))
	else:
		qr.decode_webcam()
		
	return qr.data		
	

if __name__ == '__main__':
   app.run(debug = True)
