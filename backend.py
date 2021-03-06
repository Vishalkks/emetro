from flask import Flask, render_template, request,url_for, redirect
import pyqrcode
import qrtools
import glob,os
import sqlite3
app = Flask(__name__)
session = {}
session['username'] = ''
logged_in = False
usrname = ''
logged_out = False
initial = False

@app.route('/')
def index():
	global logged_in
	global logged_out
	global session
	global initial
	if session['username']:
		logged_in = True
		usrname = session['username']
		logged_out = False
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute('select * from user_details where user_id = \''+usrname+'\'')
		rows = cur.fetchall()
		bal = rows[0][10]
		con.close()
		return render_template('home.html',loggedIn = logged_in,user_name = usrname,loggedOut = logged_out,balance=bal)
	else:
		usrname = session['username']
		temp = initial
		initial = True
		
		return render_template('home.html',loggedIn = logged_in,user_name = usrname,loggedOut = logged_out,init = temp)
   
@app.route('/login')
def login():
	return render_template('login.html')
	
@app.route('/handle_session', methods = ['GET', 'POST'])
def handle_session():
	global session
	if request.method == 'POST':
		user = request.form['user']
		pwd = request.form['pass']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute('select * from user_details where user_id = \''+user+'\'')
		rows = cur.fetchall()
		if rows:
			if rows[0][4] == pwd:
				session['username'] = request.form['user']
				con.close()
				return redirect(url_for('index'))
			else:
				con.close()
				return render_template('login.html',incorrect = True)
		else:
			con.close()
			return render_template('login.html',incorrect = True)

@app.route('/logout')
def logout():
	global logged_in
	global logged_out
	global session
	session['username'] = ''
	logged_in = False
	logged_out = True
	return redirect(url_for('index'))
   
@app.route('/register')
def register():
	return render_template('register.html')
	
@app.route('/train_details')
def train_details():
	return render_template('train_details.html')
	
@app.route('/book_tickets')
def book_tickets():
	if logged_in:
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from station_info")
		rows = cur.fetchall()
		
		print(list(rows))
		con.close()
		return render_template('book_tickets.html',source_list=rows,dst_list=rows)
	else:
		log_in_to_book_tickets = True
		
		return render_template('home.html',logInToBook = log_in_to_book_tickets)
		
	
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
		#con.close()
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
		con.close()
		return render_template('enter_quantity.html',source=src,destination=dst,time=timings,disp = display,price=prc)
		
@app.route('/checkbalance', methods = ['POST', 'GET'])
def check_balance():
	global usrname
	if request.method == 'POST':
		qty = request.form['quantity']
		price = request.form['price']
		src = request.form['src']
		dst = request.form['dst']
		timings = request.form['timings']
		total = float(qty)*float(price)
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute('select * from user_details where user_id = \''+session['username']+'\'')
		rows = cur.fetchall()
		
		print(list(rows))
		bal = rows[0][10]
		balance = float(bal)
		print('bal',bal)
		#balance = 200
		balanceSuf = 0
		display = 1
		print(total)
		if total <= balance:
			balanceSuf = 1
			balance -= total
			con.close()
			con = sqlite3.connect("Emetro.db")
			con.row_factory = sqlite3.Row
			cur = con.cursor()
			cur.execute("UPDATE user_details \
			SET walletBalance = \'"+str(balance)+"\' \
			WHERE user_id =\'"+session['username']+"\'")
		con.close()
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
		os.chdir("../../")
		
	return render_template('qrcode.html',result=url_for('static',filename='qrcodes/'+fname))
	
@app.route('/readqr',methods = ['POST'])
def read_qrcode():
	#0 xfor file, 1 for webcam, qrcode must be a file if method is 0
	qr = qrtools.QR()
	qrcode = request.form['qrcode']
	method = request.form['method']
	#entOexit = request.form['entOexit']
	point = str(request.form['point'])
	if method == "File":
		qr.decode(open('static/qrcodes/'+qrcode,'r'))
	else:
		qr.decode_webcam()
	data = qr.data
	con = sqlite3.connect("Emetro.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from station_info")
	rows = list(cur.fetchall())
	line1Purple = map(lambda x:(x[-3]),rows[:8])
	line2Purple = map(lambda x:(x[-3]),rows[7:17])
	line1Green = map(lambda x:(x[-3]),rows[17:28])
	line2Green = map(lambda x:(x[-3]),rows[27:])
	src,dst,price = map(str.strip,map(str,data.split(",")))
	index1 = ()
	if(src in line1Purple):
		index1 = (line1Purple.index(src),line1Purple,0) #indicates which line
	if(src in line2Purple):
		index1 = (line2Purple.index(src),line2Purple,0)
	if(src in line1Green):
		index1 = (line1Green.index(src),line1Green,1)
	if(src in line2Green):
		index1 = (line2Green.index(src),line2Green,1)
		
	index2 = ()
	if(dst in line1Purple):
		index2 = (line1Purple.index(dst),line1Purple,0) #indicates which line
	if(dst in line2Purple):
		index2 = (line2Purple.index(dst),line2Purple,0)
	if(dst in line1Green):
		index2 = (line1Green.index(dst),line1Green,1)
	if(dst in line2Green):
		index2 = (line2Green.index(dst),line2Green,1)
		
	#if((point in index1[1] and index1[0] > index1[1].index(point)) or (point in index2[1] and index2[0] < index2[1].index(point)))
	#mys and yel is 0, byps and nag is 1
	valid = True
	if(index1[1] == index2[1]): #Same line
		if(point in index1[1] and ( (index1[1].index(point) >= index1[0] and index1[1].index(point) <= index2[0]) or (index1[1].index(point) >= index1[0] and index1[1].index(point) <= index2[0]) )):
			valid = True
		else:
			valid = False
	
	
	
	
	elif(index1[2] == index2[2]): #Either the purple line or the green line
		if( (point in index1[1] and (index1[1].index(point) >= index1[0] )) or (point in index2[1] and (index2[1].index(point) <= index2[0]))):
			valid = True
		else:
			valid = False
			
	#cases where the lines are not the same.
	elif(index1[1] == line1Purple or index1[1] == line1Green):
		if(point in index1[1] and index1[1].index(point) >= index1[0]):
			valid = True
		elif((index2[1] == line2Green or index2[1] == line2Purple) and (point in index2[1] and index2[1].index(point) <= index2[0])):
			valid = True
		else:
			valid = False
			
	
		
	elif(index1[1] == line2Purple or index1[1] == line2Green):
		if(point in index1[1] and index1[1].index(point) <= index1[0]):
			valid = True
		elif((index2[1] == line1Green or index2[1] == line1Purple) and (point in index2[1] and index2[1].index(point) >= index2[0])):
			valid = True
		else:
			valid = False
	
	print(valid)
	print(src,dst,point)
	if(valid):
		return render_template("qroutput.html")
	else:
		return render_template("qroutput1.html")
	
@app.route('/scanqr',methods = ['GET'])
def scan_qrcode():
	con = sqlite3.connect("Emetro.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from station_info")
	rows = cur.fetchall()
	return render_template('qrread.html',dst_list=rows)

@app.route('/enter_user_details', methods=['POST'])
def enter_user_details():
	if request.method == 'POST':
		uid = request.form['user_id']
		pwd=request.form['password']
		fn= request.form['firstName']
		ln = request.form['lastName']
		mail = request.form['email']
		street = request.form['street']
		city = request.form['pincode']
		mb = request.form['mobileNo']
		pincode = request.form['pincode']
		dob=request.form['dob']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		con.execute("INSERT INTO user_details VALUES(\'"+uid+"\',\'"+fn+"\',\'"+ln+"\',\
		\'"+mail+"\',\'"+pwd+"\',\'"+dob+"\',\'"+street+"\',\'"+city+"\',\'"+pincode+"\',\'"+mb+"\',0)")
		con.commit()
		con.close()
		return render_template('home.html',register = True)

@app.route('/recharge',methods=['POST'])
def recharge():
    return render_template('payment.html')	

@app.route('/addmoney', methods=['POST'])
def addmoney():
    # Amount in cents
	if request.method == 'POST':
		amt=request.form['amount']
		mail=request.form['email']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from user_details \
		where email= \'"+mail+"\'")
		rows = cur.fetchall()
		if len(rows)==0:
			 return render_template("pay.html",message="User doesn't exist")
		a=rows[0]["FirstName"]
		b=rows[0]["walletBalance"]
		print(a)
		con.execute("UPDATE user_details \
			SET walletBalance = \'"+amt+"\' \
			WHERE email =\'"+mail+"\'")
		con.commit()
		b+=int(amt)
		return render_template('home.html',user=a,balance=b,state="logout")

if __name__ == '__main__':
	app.config["CACHE_TYPE"] = "null"
	app.run(debug = True)
