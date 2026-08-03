import qrcode

text = input("Enter text or url: ")
qr = qrcode.make(text)
filename = "qrcode.png"
qr.save(filename)
print("QR Code saved as", filename)