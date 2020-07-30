
import qrcode 
from PIL import Image, ImageFont, ImageDraw 
import random 

print("Wellcom to happy Eid program ")
pics = ["pic1.jpg", "pic2.jpg", "pic2.jpg", "pic4.jpg"]
brown2 = (76, 63, 67)
gold3 = (249, 183, 24)
blue4 = (2, 52, 121)
cyna1 = (72, 211, 157)
colors = [cyna1, brown2, gold3, blue4]

try: 
	menu = input(f"""
		1.{pics[0]}
		2.{pics[1]}
		3.{pics[2]}
		4.{pics[3]}
		""")

	mypic = Image.open(f"image/pic{menu}.jpg")
	text = input("Enter your namde : ")
	qrdata = input("Enter Qr code data : ")

	drowimge = ImageDraw.Draw(mypic)
	usedfont = ImageFont.truetype("Ubuntu-Title.ttf", 70)

# make qr code 
	MakeQRCode = qrcode.QRCode(box_size=5)
	MakeQRCode.add_data("somddata")
	QRCodeImage = MakeQRCode.make_image()
	QRPostion = (mypic.size[0] - QRCodeImage.size[0], mypic.size[1] - QRCodeImage.size[1])
	mypic.paste(QRCodeImage, QRPostion)

	drowimge.text((330,1500), text, colors[int(menu)-1], font=usedfont)
	mypic.save('savedpic.jpg')
except:
	print("somthing gos worng try agen ")
