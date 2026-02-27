import qrcode, os

# mise en forme du qrcode 
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 1)

#On rajoute le lien que l'on veut ouvrir 
qr.add_data("https://ahmed-azongnimon.web.app/")
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
                    back_color = 'white')

abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

img.save(fr"{rel_path}\MyQRCode.png")