from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
img = Image.new('RGB', (W, H), '#0b1124')
d = ImageDraw.Draw(img)

font_big = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 64)
font_mid = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 34)
font_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 26)
font_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)

# shell
for i, color in [(0, '#0b1124'), (1, '#0d1430')]:
    d.rectangle((0, i * H // 2, W, (i + 1) * H // 2), fill=color)

d.rounded_rectangle((40, 40, W - 40, H - 40), radius=36, fill='#0f1732', outline='#334577', width=2)
d.rounded_rectangle((70, 70, W - 70, 240), radius=28, fill='#111b3b')

d.text((110, 110), 'Luva Studio', fill='#eef4ff', font=font_big)
d.text((110, 190), 'Neon OT / ICS analysis dashboard', fill='#9fb2e8', font=font_mid)

labels = [('Assets', '2'), ('OT Assets', '2'), ('Flows', '4'), ('Anomalies', '2')]
colors = ['#8b5cf6', '#22d3ee', '#34d399', '#fb7185']
x, y, cardw, cardh, gap = 90, 290, 320, 130, 24
for i, (lab, val) in enumerate(labels):
    left = x + i * (cardw + gap)
    d.rounded_rectangle((left, y, left + cardw, y + cardh), radius=22, fill='#131f43', outline=colors[i], width=3)
    d.text((left + 30, y + 24), lab, fill='#9fb2e8', font=font_sm)
    d.text((left + 30, y + 56), val, fill='#ffffff', font=font_big)

# left pane
left_box = (70, 460, 760, 830)
d.rounded_rectangle(left_box, radius=24, fill='#101a38', outline='#334577')
d.text((100, 490), 'Assets', fill='#eef4ff', font=font_mid)
rows = [
    '10.20.102.1  | SCADA Server              | IEC 104',
    '10.20.100.108 | PLC / RTU                  | IEC 104',
    '10.20.102.1 -> 10.20.100.108            | 59 packets',
    '10.20.100.108 -> 10.20.102.1            | 46 packets',
]
yy = 560
for r in rows:
    d.text((100, yy), r, fill='#d9e7ff', font=font_sm)
    yy += 60

d.text((100, 770), 'Protocol badges, findings, uploads, and tabs are available in the live GUI.', fill='#91a5d6', font=font_xs)

# right pane
right_box = (800, 460, 1530, 830)
d.rounded_rectangle(right_box, radius=24, fill='#101a38', outline='#334577')
d.text((830, 490), 'Embedded Report Preview', fill='#eef4ff', font=font_mid)
d.rounded_rectangle((840, 550, 1490, 790), radius=18, fill='#f3f6fb')
d.text((920, 640), 'Generated interactive Luva Studio report', fill='#1f2937', font=font_mid)
d.text((920, 690), 'HTML report + communication map + topology outputs', fill='#475569', font=font_sm)

d.text((840, 810), 'Example branded preview image for README / Help.html', fill='#91a5d6', font=font_xs)

img.save(r'C:\WireSharkTools\luva\artifacts\luva-studio-dashboard.png')
print('saved')
