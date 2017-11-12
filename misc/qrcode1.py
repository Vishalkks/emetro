import pyqrcode
import pyqrtools
import glob
def generate_qrcode(username,data):
	#The data is assumed to be a json of the neccesary details such as the time, source, destination.
	qrcode = pyqrcode.create(data)
	latestBooking = max(map(lambda x : int(x.split('.')[0]), glob.glob('/qrcodes/'+username'/'))) + 1
	with open('/qrcodes/'+username+'/'+latestBooking+".png" as fstream):
		qrcode.png(fstream, scale=5)
		
	return fstream
	
def read_qrcode(method,qrcode=0):
	#0 for file, 1 for webcam, qrcode must be a file if method is 0
	qr = qrtools.QR()
	if method == 0:
		qr.decode(qrcode)
	else:
		qr.decode_webcam()
		
	return qr.data
