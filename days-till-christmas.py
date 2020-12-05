from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)


img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 36)

show_countdown("20")
show_message("Days Unil Christmas!")


inky_display.set_image(img)
inky_display.show()

def show_countdown(count):
  w, h = font.getsize(count)
  x = (inky_display.WIDTH / 2) - (w / 2)
  y = (inky_display.HEIGHT) - (h / 2)

  draw.text((
    (inky_display.WIDTH / 2) - (w / 2),
    (0),
    count,
    inky_display.RED, font
  ))

def show_message(message):
  w, h = font.getsize(message)
  x = (inky_display.WIDTH / 2) - (w / 2)
  y = (inky_display.HEIGHT) - (h / 2)

  draw.text((
    (inky_display.WIDTH / 2) - (w / 2),
    (inky_display.HEIGHT) - (h / 2)),
    message,
    inky_display.RED, font
  )
