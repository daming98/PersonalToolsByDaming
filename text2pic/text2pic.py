import re
from PIL import Image,ImageDraw,ImageFont

def cut_text(text, lenth, indent):
    List=[]
    List.append(text[:lenth-indent])
    text=text[lenth-indent:]
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    return List+textArr 
fontSize=60
lineSpace=15
indent=2
font = ImageFont.truetype('C:\Windows\Fonts\方正清刻本悦宋简体_0.TTF', fontSize)
text=""
with open("1.txt", "r") as f:
    text=f.read()

textList=text.split()
lines=0
h=4*fontSize
w=1080

splitedList=[]
for text in textList:
    tempList=cut_text(text, (w-(4*fontSize))//fontSize, indent)
    h+=(fontSize+lineSpace)*(len(tempList)+1)
    print(h)
    splitedList.append(tempList)

img = Image.new('RGB',(w,h),(64,64,64))
draw = ImageDraw.Draw(img)
currentHeight=0
offset=0
for i in range(len(splitedList)):
    currentHeight+=fontSize+lineSpace
    for j in range(len(splitedList[i])):
        if j==0:
            offset=indent*fontSize
        else:
            offset=0
        currentHeight+=(fontSize+lineSpace)
        draw.text(((2*fontSize)+offset, currentHeight), splitedList[i][j], (0,0,0), font=font)
    
img.show()
img.save("1.jpg", "jpeg")
