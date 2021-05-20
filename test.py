text = '''for x in range(len(text)):
        if text[x] == "\n":
            line+=1
            text =text[:x]+'\n'+str(line)+'   '+text[x+1:]
            logger.info('поймали '+str(line))
            height += 20
            line_width = 0
        else:
            line_width +=7
'''

out_text = text.splitlines()
pred_number = ''
line_width = 0


for x in range(len(out_text)):

	if len(out_text)>10 and x<9 or len(out_text)>100 and x<99:
		pred_number = '0'

	elif len(out_text)>100 and x<9:
		pred_number = '00'

	else:
		pred_number = ''

	if len(out_text[x])>line_width:
		line_width = len(out_text[x])
	
		

	out_text[x] = pred_number+str(x+1)+'    '+out_text[x]
	#print(str(out_text[x]))

line = len(out_text)
print('\n'.join(out_text))
print(str(line)+' '+str(line_width))


