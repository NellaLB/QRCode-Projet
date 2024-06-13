import segno

qrcode = segno.make_qr("<|°_°|> Bonjour :)")
qrcode_rotated = qrcode.to_pil(
    scale = 5, border = 1, 
    light = 'lightyellow', 
    dark = 'darkblue',
    quiet_zone = 'lightblue',
    data_dark = 'black',
    data_light = 'lightgreen').rotate(45, expand=True)

qrcode_rotated.save("basic_qrcode.png")