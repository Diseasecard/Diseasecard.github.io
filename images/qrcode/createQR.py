import qrcode
from PIL import Image, ImageDraw

data = "https://drive.google.com/file/d/1CeIrN3rIf8Np9Uz4U3X70kfkGtHy71CN/view?usp=sharing"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img_qr = qr.make_image(fill_color='black', back_color='white').convert('RGBA')

logo = Image.open('images/qrcode/dna.png')

logo_size = 100

logo_bg = Image.new('RGBA', (logo_size, logo_size), 'white')
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
logo_bg.paste(logo, (0, 0), logo)

mask = Image.new('L', (logo_size, logo_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_size, logo_size), fill=255)

logo_circular = Image.composite(logo_bg, Image.new('RGBA', (logo_size, logo_size)), mask)

pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)

img_qr.paste(logo_circular, pos, mask)

img_qr.save('images/qrcode/qr.png')
