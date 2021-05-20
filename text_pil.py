from PIL import Image, ImageDraw, ImageFont

text = '''
<colorist #4A5056>1....</colorist>for x in range(10)
<colorist #4A5056>2........</colorist>print(x)
'''



img = Image.new('RGB', (500, 500), color = (20,20,20,128))
fnt = ImageFont.truetype('Pt.ttf', font_size)
d = ImageDraw.Draw(img)


font_size = 20
text_color = (255, 255, 255)

width_line = 0

text_in = text.splitlines()

bufer_collor = text_color

for x in range(len(text_in)):
	for y in range(len(text_in[x])):
		width_simbol = fnt.getsize(text_in[x][y])[0]

		# tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

		if text_in[x][y:y+9] in '<colorist' :
			print(text_in[x][y:y+9])
			not_print = 9
			if text_in[x][y+10:y+14] in 'grey':
				not_print+=6
				text_color = (100, 100, 100)
			if text_in[x][y+10] in '#':
				not_print+=9
				hex_color = str(text_in[x][y+11:y+17]).lower()
				print(hex_color)
				text_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

		elif text_in[x][y:y+11] in '</colorist>':
			not_print = 11
			text_color = bufer_collor

		if not_print > 0:
			not_print -= 1
		else:
			d.text((width_line ,font_size*x - font_size), text_in[x][y], font=fnt, fill=text_color,align ="right")

			width_line += width_simbol
			width_line += 0

	width_line = 0


img.save('format_text_font.png')