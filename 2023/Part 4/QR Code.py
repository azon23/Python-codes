# On importe de la bibliotheque 
import qrcode 
# Donné a code 
data = "any"
# mise en forme du qrcode 
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 #On rajoute le lien que l'on veut ouvrir 
qr.add_data("http://196.200.57.210:8080/pronote/eleve.html?fd=1")
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
img.save('MyQRCode.png')