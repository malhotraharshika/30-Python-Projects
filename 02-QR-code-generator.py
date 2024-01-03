import qrcode

def generate_qrcode(data):
  qr = qrcode.QRCode(
    version = 1, # version (1 to 40), Lower version hold less data
    error_correction = qrcode.constants.ERROR_CORRECT_L, # ERROR_CORRECT_L is low-level error correction
    box_size = 10,
    border = 4
  )
  qr.add_data(data)
  qr.make(fit=True) # automatically adjust the QR code's version and size to fit the encoded data
  qr_image = qr.make_image(fill_color = "black", back_color = "white") # Creates an image representation of the QR code
  qr_image.save("myqrcode.png")

data = input("Enter your url or text: ")
generate_qrcode(data)
