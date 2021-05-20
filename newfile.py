from PIL import Image, ImageDraw, ImageFont
 
#img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
img = Image.open("bg.jpg") 
fnt = ImageFont.truetype('Pt.ttf', 30)
d = ImageDraw.Draw(img)


d.ellipse([(50,30),(80,60)], fill=(20,20,20,128))
d.ellipse([(510,30),(540,60)], fill=(20,20,20,128))
d.rectangle([(70, 30) , (530,80)], fill=(20,20,20,128))
d.rectangle([(50, 50) , (540,1000)], fill=(20,20,20,128))
d.ellipse([(70,50),(90,70)], fill=(200,20,20,128))
d.ellipse([(100,50),(120,70)], fill=(253,233,16,128))
d.ellipse([(130,50),(150,70)], fill=(0,255,0,128))
#d.line((0, im[1], im[0], 0), fill=128)

text = ''' 
C = input("Choose your charecter to insert. ")
P = int(input("Choose your character's position. "))
S = input("Choose your string. ")

if P > len(S):
    print(S)
else:
    st = S[:P] + C + S[P:]

    print(st)
    print(C,P,S)
 '''
i=0
for x in range(len(text)):
	
	if x < len(text)-1:
		if text[x]+text[x+1]=='\n':
			i=0
		
	if i == 30 and x < len(text)-1:
		#text.insert(30,'\n')
		text = text[:x]+'\n'+text[x+1:-1]
		print(text[x:-1])
		print(x)
		i=0
	i+=1

d.text((100,100), text, font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')