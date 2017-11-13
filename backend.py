from flask import Flask, render_template, request,url_for
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
	return render_template('register.html')
	
@app.route('/train_details')
def train_details():
	return render_template('train_details.html')
	
@app.route('/book_tickets')
def book_tickets():
	con = sqlite3.connect("Emetro.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from station_info")
	rows = cur.fetchall()
	con.close()
	return render_template('book_tickets.html',source_list=rows,dst_list=rows)
	
@app.route('/traintable', methods = ['POST', 'GET'])
def train_table():
	if request.method == 'POST':
		src = request.form['source']
		dst = request.form['destination']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from train_info TI, train_schedule TS where TI.source = \'"+src+"\' and TI.destination = \'" +dst+"\' and TI.train_id = TS.train_id")
		rows = cur.fetchall()
		con.close()
		if not rows:
			con = sqlite3.connect("Emetro.db")
			con.row_factory = sqlite3.Row
			cur = con.cursor()
			cur.execute("select * from train_info TI, train_schedule TS where TI.source = \'"+dst+"\' and TI.destination = \'" +src+"\' and TI.train_id = TS.train_id")
			rows = cur.fetchall()
			con.close()
		
		return render_template('book_tickets.html', rows1=rows, source = src, destination = dst)
		
@app.route('/enterquantity', methods = ['POST', 'GET'])
def enter_quantity():
	if request.method == 'POST':
		src = request.form['src'].strip()
		dst = request.form['dst'].strip()
		timings = request.form['timings']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from station_info where station_name = \'"+src+"\'")
		rows1 = cur.fetchall()
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from station_info where station_name = \'"+dst+"\'")
		rows2 = cur.fetchall()
		prc = abs(int(rows1[0][4])-int(rows2[0][4]))*10
		print(prc)
		display = 0
		return render_template('enter_quantity.html',source=src,destination=dst,time=timings,disp = display,price=prc)
		
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
		print(total)
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
		os.chdir('static/qrcodes')
		fname = str(latestBooking)+".png"
		with open(fname,'w+') as fstream:
			qrcode.png(fstream, scale=5)
		os.chdir("../")
		
	return render_template('qrcode.html',result=url_for('static',filename='qrcodes/'+fname))
	
@app.route('/readqr',methods = ['POST'])
def read_qrcode():
	#0 xfor file, 1 for webcam, qrcode must be a file if method is 0
	qr = qrtools.QR()
	qrcode = request.form['qrcode']
	method = request.form['method']
	if int(method) == 0:
		qr.decode(open('static/qrcodes/'+qrcode,'r'))
	else:
		qr.decode_webcam()
	print("Hello")
	return "<html><h3> Booking details are : "+qr.data+"</h3></html>"		
	
@app.route('/scanqr',methods = ['GET'])
def scan_qrcode():
	return render_template('qrcode_read.html')

if __name__ == '__main__':
   app.run(debug = True)
