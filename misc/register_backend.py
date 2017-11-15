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
		return render_template('home.html',user=fn)

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
			return render_template('login.html',message="Incorrect userid or password")
		return render_template('home.html')
		
if __name__ == '__main__':
   app.run(debug = True)
