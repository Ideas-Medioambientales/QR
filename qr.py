import qrcode
img = qrcode.make("https//www.qr.ideasmedioambientales.com/jjsegui")
f = open("output.png", "wb")
img.save(f)
f.close()