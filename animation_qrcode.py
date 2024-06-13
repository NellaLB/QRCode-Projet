import segno
from urllib.request import urlopen

GTS_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
GTS_url = urlopen("https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif")
GTS_qrcode.to_artistic(
    background = GTS_url,
    target="animated_qrcode.gif",
    scale=5,
)