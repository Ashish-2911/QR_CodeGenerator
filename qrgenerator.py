import pyqrcode

content = "This Qr code generate by Python."

obj = pyqrcode.create(content)

obj.png("MyQR.png", scale=6)
