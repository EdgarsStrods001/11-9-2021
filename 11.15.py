from PIL import Image]

def bilde():

  datne = "Dowanloand kalns"

   with Image.open(datne) as im:
   print ( datne, im.format,  f"{im.size}x
   {im.mode}")
   izmers = (100,100)
   iz.thumbnail (izmers)
   im.save("maza_bilde.jpg", im.for)