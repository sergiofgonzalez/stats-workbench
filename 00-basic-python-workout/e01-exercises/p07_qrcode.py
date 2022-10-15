import qrcode


def generate_qrcode_image(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./data/p07_qrcode/qrimg.png")


text = input("Enter the text to encode in the QR code: ")
generate_qrcode_image(text)
print("Image saved as './data/p07_qrcode/qrimg.png'")
