#!/usr/bin/env python

import sys

from PIL import ImageFont

import inkyphat

#inkyphat.set_rotation(180)

colour = 'red'

# Show the backdrop image

inkyphat.set_border(inkyphat.RED)

# Partial update if using Inky pHAT display v1

if inkyphat.get_version() == 1:
    inkyphat.show()

# Add the text

font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 38)

text = '20 Days until Christmas'

w, h = font.getsize(text)

# Center the text and align it with the name strip

x = (inkyphat.WIDTH / 2) - (w / 2)
y = 71 - (h / 2)

inkyphat.text((x, y), text, inkyphat.BLACK, font)

# Partial update if using Inky pHAT display v1

if inkyphat.get_version() == 1:
    inkyphat.set_partial_mode(56, 96, 0, inkyphat.WIDTH)

inkyphat.show()
