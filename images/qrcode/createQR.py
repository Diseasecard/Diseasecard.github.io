import qrcode
from PIL import Image, ImageDraw

data = "https://github.com/Diseasecard/Diseasecard.github.io/raw/main/apk/diseasecard.apk"

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
border_size = 20 

logo_with_border_size = logo_size + 2 * border_size
logo_with_border = Image.new('RGBA', (logo_with_border_size, logo_with_border_size), 'white')

logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

logo_pos = (border_size, border_size)
logo_with_border.paste(logo, logo_pos, logo)

mask = Image.new('L', (logo_with_border_size, logo_with_border_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo_with_border_size, logo_with_border_size), fill=255)

logo_circular = Image.composite(logo_with_border, Image.new('RGBA', (logo_with_border_size, logo_with_border_size)), mask)

pos = ((img_qr.size[0] - logo_with_border_size) // 2, (img_qr.size[1] - logo_with_border_size) // 2)

img_qr.paste(logo_circular, pos, mask)

img_qr.save('images/qrcode/qr.png')
