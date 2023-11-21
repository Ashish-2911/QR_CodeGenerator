import pyqrcode

# content = "This Qr code generate by Python."

content = input("Enter your value -  ")

obj = pyqrcode.create(content)

fileName = input("What will be your QR file name -  ")
fileName = fileName + ".png"

obj.png(fileName, scale=6)
