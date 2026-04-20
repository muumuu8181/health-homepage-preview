import sys
import qrcode

url = sys.argv[1] if len(sys.argv) > 1 else "https://muumuu8181.github.io/health-homepage-preview/"

qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#3a3530", back_color="#fbf7ef")
img.save("qr_code.png")

qr_print = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=30, border=6)
qr_print.add_data(url)
qr_print.make(fit=True)
img_print = qr_print.make_image(fill_color="#000000", back_color="#ffffff")
img_print.save("qr_code_print.png")

print(f"Generated QR for: {url}")
