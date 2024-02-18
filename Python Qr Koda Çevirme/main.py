import qrcode
import image

qr = qrcode.QRCode(version=15,
box_size=10,
border=5)

#Yukarıdaki Değerleri Değiştirerek değişik QR kod Şekilleri Oluşturabilirsiniz

data = "Test Test"  #Bu Kısımda QR  Koda Dönüşmesini İstediğiniz Cümle Yada Linki Ekleyebilirsiniz.
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color = "white")
img.save("qr.png")