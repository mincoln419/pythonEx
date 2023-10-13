import pyqrcode

# qrcode = pyqrcode.create("https://www.naver.com")
# qrcode.svg("qr_naver.svg", scale=8)
# qrcode.eps("qr_naver.eps", scale=10)

# data = "WIFI:S:MYIPTIME;T:WPA;P:12345678"
# qrcode = pyqrcode.create("https://www.naver.com", error="L", version=15, mode="binary")
data = "BEGIN:VCARD\n"
data += "VERSION:3.0\n"
data += "FN:메르메르\n"
data += "TEL;TYPE=WORK;CELL:010 8013 9108\n"
data += "EMAIL;TYPE=WORK:abcd@naver.com\n"
data += "URL;TYPE=WORK:https://www.naver.com\n"
data += "END:VCARD\n"
qrcode = pyqrcode.create(data, mode="binary", encoding="UTF-8")
qrcode.png("vcard.png", scale=8, module_color=[0, 0, 0, 255], background=[255,255,255,255])