from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

S = 2
W = H = 1080
im = Image.new('RGB', (W*S, H*S), '#F4F0E7')
d = ImageDraw.Draw(im)
def box(xy, radius, fill, outline=None, width=1):
    d.rounded_rectangle(tuple(int(v*S) for v in xy), radius=int(radius*S), fill=fill, outline=outline, width=int(width*S))
def line(xy, fill, width=1): d.line([(int(x*S), int(y*S)) for x,y in xy], fill=fill, width=int(width*S))
def circle(xy, fill, outline=None, width=1): d.ellipse(tuple(int(v*S) for v in xy), fill=fill, outline=outline, width=int(width*S))
fonts = 'C:/Windows/Fonts/'
def font(name, size): return ImageFont.truetype(fonts+name, size*S)
reg=font('arial.ttf',18); med=font('arialbd.ttf',18); small=font('arialbd.ttf',13); title=font('arialbd.ttf',59); serif=font('georgiab.ttf',21); body=font('arial.ttf',17); tiny=font('arialbd.ttf',12)
navy='#152744'; cream='#F4F0E7'; orange='#C9472C'; green='#D8F06B'; muted='#647083'; white='#FFFEFA'
# header brand
box((62,54,1018,125),18,navy)
circle((82,70,120,108),green)
d.text((91*S,75*S),'W',font=font('arialbd.ttf',21),fill=navy)
d.text((134*S,72*S),'WEB DESIGN',font=med,fill=white)
d.text((134*S,97*S),'FOR SMALL BUSINESSES',font=tiny,fill='#CDD5E0')
box((803,73,992,107),17,'#243653')
d.text((820*S,82*S),'EUROPE  ·  REMOTE',font=tiny,fill=green)
# eyebrow/title
box((69,164,307,199),17,green)
d.text((86*S,174*S),'A WEBSITE THAT WORKS',font=tiny,fill=navy)
d.text((68*S,222*S),'MAKE YOUR',font=title,fill=navy)
d.text((68*S,284*S),'BUSINESS',font=title,fill=navy)
d.text((68*S,346*S),'EASY TO FIND.',font=title,fill=orange)
d.text((72*S,432*S),'Clean, mobile-friendly websites for small',font=body,fill=navy)
d.text((72*S,460*S),'businesses across Europe.',font=body,fill=navy)
# features
features=[('01','Show what you offer'),('02','Look great on mobile'),('03','Make it easy to contact you')]
y=525
for n,txt in features:
    circle((73,y,101,y+28),green)
    d.text((80*S,(y+7)*S),n,font=tiny,fill=navy)
    d.text((116*S,(y+3)*S),txt,font=reg,fill=navy)
    y+=43
# mock browser panel
box((545,181,1014,704),24,navy)
box((558,194,1001,691),17,white)
# browser top bar
d.rectangle((558*S,194*S,1001*S,235*S),fill='#ECE9E1')
for i,c in enumerate(['#EA7761','#E9C76B','#84A77B']): circle((575+17*i,207,584+17*i,216),4,c)
box((638,203,850,225),9,'#F8F6F0')
d.text((653*S,208*S),'longli-dimsum.com',font=tiny,fill=muted)
# sample site masthead
d.text((583*S,254*S),'LONG LI',font=font('georgiab.ttf',18),fill=navy)
d.text((860*S,260*S),'MENU    STORY    VISIT',font=font('arialbd.ttf',9),fill=muted)
line([(582,287),(978,287)],'#E5E1D8',1)
d.text((583*S,317*S),'Dim sum,',font=serif,fill=navy)
d.text((583*S,346*S),'made to share.',font=serif,fill=orange)
d.text((584*S,386*S),'Freshly made favourites,',font=font('arial.ttf',10),fill=muted)
d.text((584*S,403*S),'made to share over a pot of tea.',font=font('arial.ttf',10),fill=muted)
box((583,439,724,475),9,orange)
d.text((600*S,451*S),'EXPLORE THE MENU  →',font=font('arialbd.ttf',10),fill=white)
# site image panel with abstract dish
box((750,301,978,496),16,'#E7D5B5')
circle((792,332,944,483),'#F7F1E5')
circle((808,348,928,468),'#E7D8C0')
for x,y in [(836,377),(875,367),(901,394),(854,414),(891,433)]:
    box((x-18,y-14,x+18,y+14),12,'#FFFDF7',outline='#D7BE98',width=2)
    line([(x-8,y-1),(x,y+4),(x+8,y-1)],'#CF9D69',2)
# dish cards
for x,heading,sub in [(583,'Prawn dumplings','A house favourite'),(782,'Golden buns','A sweet finish')]:
    box((x,514,x+180,653),12,'#F7F4ED')
    box((x+12,526,x+156,583),8,'#E8DFCE')
    circle((x+55,535,x+112,575),'#FFF8E8')
    d.text(((x+12)*S,593*S),heading,font=font('arialbd.ttf',12),fill=navy)
    d.text(((x+12)*S,615*S),sub,font=font('arial.ttf',10),fill=muted)
box((585,664,971,680),8,'#F2EEE5')
d.text((605*S,666*S),'A BILINGUAL, MOBILE-FRIENDLY WEBSITE CONCEPT',font=font('arialbd.ttf',8),fill=muted)
# CTA strip
box((62,743,1018,922),22,orange)
d.text((93*S,776*S),'YOUR BUSINESS DESERVES A GREAT FIRST IMPRESSION.',font=small,fill='#FFD7C7')
d.text((92*S,811*S),'Let’s build your website.',font=font('georgia.ttf',36),fill=white)
box((746,815,986,876),15,green)
d.text((776*S,836*S),'DM ME TO GET STARTED  →',font=font('arialbd.ttf',14),fill=navy)
# footer labels
line([(68,957),(1012,957)],'#D5CEC1',1)
d.text((72*S,980*S),'PORTFOLIO SAMPLE: DIM SUM HOUSE CONCEPT',font=tiny,fill=navy)
d.text((735*S,980*S),'REMOTE WEBSITE DESIGN  ·  EUROPE',font=tiny,fill=muted)
# downsample/export
im=im.resize((W,H),Image.Resampling.LANCZOS)
out=Path('facebook-promo.png')
im.save(out,optimize=True)
print(out.resolve())


