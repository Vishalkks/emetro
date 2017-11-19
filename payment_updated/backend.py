import os
from flask import Flask, render_template, request
import sqlite3
import json
app = Flask(__name__, static_folder ="images")

@app.route('/')
def index():
   return render_template('home.html',state="Login")
   
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
		cur.execute("select * from train_schedule s join train_info t on s.train_id=t.train_id \
		where s.source = \'"+src+"\' and s.destination = \'" +dst+"\'")
		rows = cur.fetchall()
		return render_template('book_tickets.html', rows1=rows, source = src, destination = dst)
		
@app.route('/enterquantity', methods = ['POST', 'GET'])
def enter_quantity():
	if request.method == 'POST':
		src = request.form['src']
		dst = request.form['dst']
		#print(src)
		#print(dst)
		con = sqlite3.connect("Emetro.db")
		cur = con.cursor()
		"""
		cur.execute("select * from station_info where station_name = \'"+src+"\'")
		rows = cur.fetchall()
		#r1=rows1[0][0]
		cur.execute("select * from station_info where station_name=\'"+dst+"\'")
		rows = cur.fetchall()
		#r2=rows2[0][0]
		#res=rows2[0]["point"]-rows1[0]["point"]
		#res=10*res
		print(rows)
		"""
		price=20
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
		balance = 0
		balanceSuf = 0
		display = 1
		if total <= balance:
			balanceSuf = 1
		return render_template('enter_quantity.html',source=src,destination=dst,time=timings,tot=total,balance = balanceSuf,disp = display)
		
		

@app.route('/recharge')
def recharge():
    return render_template('pay.html')	


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
		
		
@app.route('/userdetails', methods=['POST'])
def user_details():
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
		age=request.form['age']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		con.execute("INSERT INTO user_details VALUES(\'"+uid+"\',\'"+pwd+"\',\'"+fn+"\',\'"+ln+"\',\
		\'"+mail+"\',\'"+dob+"\',\'"+age+"\',\'"+street+"\',\'"+city+"\',\'"+pincode+"\',\'"+mb+"\',0)")
		con.commit()
		return render_template('home.html',user=fn,balance=0,state="Logout")

@app.route('/checklogin', methods=['POST'])
def check_login():
	if request.method=='POST':
		id=request.form['email']
		pwd=request.form['password']
		con = sqlite3.connect("Emetro.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("select * from user_details \
		where email= \'"+id+"\' and password= \'" +pwd+"\'")
		rows = cur.fetchall()
		if len(rows)==0:
			 return render_template("login.html",message="Invalid password or email-Id")
		a=rows[0]["FirstName"]
		b=rows[0]["walletBalance"]
		return render_template("home.html",user=a,balance=b,state="Logout")
		
if __name__ == '__main__':
   app.run(debug = True)
