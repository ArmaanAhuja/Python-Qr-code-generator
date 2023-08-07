import qrcode 
from PIL import Image
# img = qr.make("https://python.land/virtual-environments/virtualenv")
# print("Generating qr code....")
# img.save("pythonLand.png")

qr = qrcode.QRCode(
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_H, 
    box_size = 10, border = 4)


qr.add_data("https://www.youtube.com/watch?v=3bZbAA4jkV8")

qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "yellow")

img.save("img.png")

