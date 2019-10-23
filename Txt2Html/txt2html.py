import sys

def main(txt):
    lines=[]
    with open(txt, "r") as f:
        lines=f.readlines()
    lines=[x for x in lines if x!="\n"]
    head=lines.pop(0).strip()
    i=head.index("》")
    title=head[1:i]
    author=head[i+1:]
    print("标题：", title)
    print("作者：", author)
    lines=[x.strip() for x in lines]
    writelist=["<p>"+x+"</p>" for x in lines]
    htmlname=txt.split(".")[0]
    htmltitle="一天一苹果，傻子远离我"
    writehead=["<html>", "<head>", "<title> "+ htmltitle +" </title>", \
               "<style> h1 { font-size: 50px; } h2 { font-size: 40px; } p { font-size: 54px; } </style>", \
               "</head>", "<body>"]
    writetile=["</body>", "</html>"]
    with open(htmlname+".html", "w") as html:
        html.writelines(writehead)
        html.writelines(["<h1>"+ title +"</h2>", "<h2>"+ author +"</h2>"])
        html.writelines(writelist)
        html.writelines(writetile)
    print("OK!")

txt=sys.argv[1]

main(txt)
