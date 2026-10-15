from PIL import Image, ImageDraw
S=1024
im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rounded_rectangle((40,40,S-40,S-40),radius=210,fill=(38,56,110,255))
# 书本阴影与封面
d.rounded_rectangle((240,170,800,870),radius=46,fill=(24,36,78,255))
d.rounded_rectangle((220,140,780,840),radius=46,fill=(246,238,222,255))
# 书脊
d.rounded_rectangle((220,140,330,840),radius=46,fill=(214,92,84,255))
d.rectangle((290,140,330,840),fill=(214,92,84,255))
for y in (240,390,540,690):
    d.ellipse((248,y-30,312,y+34),fill=(246,238,222,255))
# 书签
d.polygon([(650,140),(730,140),(730,290),(690,250),(650,290)],fill=(240,176,60,255))
# 日记横线
for y in (400,500,600,700):
    d.rounded_rectangle((400,y,700,y+16),radius=8,fill=(190,176,150,255))
d.rounded_rectangle((400,300,560,320),radius=10,fill=(38,56,110,255))
# 墨水笔尖
im=im.resize((256,256),Image.LANCZOS) if False else im
big=im
big.resize((512,512),Image.LANCZOS).save('/home/claude/nl/app/resources/icons/appIcon.png')
big.save('icon.ico',sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
big.resize((256,256),Image.LANCZOS).save('preview.png')
