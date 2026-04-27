from PIL import Image, ImageDraw, ImageFont

W = H = 1024
img = Image.new('RGBA', (W, H), '#0b1020')
d = ImageDraw.Draw(img)

for r, color in [(430, (139, 92, 246, 28)), (360, (34, 211, 238, 22)), (300, (52, 211, 153, 16))]:
    d.ellipse((512-r, 280-r, 512+r, 280+r), fill=color)

d.rounded_rectangle((0, 0, W-1, H-1), radius=220, fill='#0f1732')

for w, color in [(24, '#8b5cf6'), (14, '#22d3ee')]:
    d.ellipse((326, 94, 698, 466), outline=color, width=w)

points = [(360, 404), (452, 314), (512, 374), (664, 222)]
d.line(points, fill='#8b5cf6', width=24, joint='curve')
d.line([(360,404),(512,252),(664,404)], fill='#22d3ee', width=14)

for xy, r, color in [((360,404),26,'#8b5cf6'),((452,314),24,'#a78bfa'),((512,374),24,'#67e8f9'),((512,252),24,'#c4b5fd'),((664,222),28,'#22d3ee'),((664,404),24,'#34d399')]:
    d.ellipse((xy[0]-r, xy[1]-r, xy[0]+r, xy[1]+r), fill=color)

for box, width, color in [((326, 520, 698, 520), 16, '#24345f'), ((356, 556, 668, 556), 12, '#334577')]:
    d.arc((box[0], box[1]-80, box[2], box[1]+80), start=200, end=340, fill=color, width=width)

font1 = ImageFont.truetype('C:/Windows/Fonts/seguiemj.ttf', 1) if False else ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 112)
font2 = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 86)

def center_text(y, text, font, fill):
    bbox = d.textbbox((0,0), text, font=font)
    x = (W - (bbox[2]-bbox[0])) // 2
    d.text((x, y), text, font=font, fill=fill)

center_text(620, 'Luva', font1, '#f1eeff')
center_text(730, 'Studio', font2, '#9fb2e8')

img.save(r'C:\WireSharkTools\luva\img\luva-studio-logo.png')
print('saved')
