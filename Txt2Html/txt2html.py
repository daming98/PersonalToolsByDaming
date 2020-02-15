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
    htmlname=txt.split(".")[0]
    htmltitle="《"+title+"》 作者："+author
    writehead=["<html>", "<head>", \
               "<meta name='viewport' content='width=device-width, initial-scale=1'>", \
               "<title> "+ htmltitle +" </title>", \
               "<link href='https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css' rel='stylesheet'>", \
               # "<style> h1 { font-size: 50px; } h2 { font-size: 40px; } p { font-size: 54px; } </style>", \
               "</head>", "<body>", \
               "<div class='container'>"]
    writetitle=["<div class='page-header'> <h1> ", title, " <small>", author, " </small> </h1> </div>"]
    writelist=["<p class='lead'>"+x.strip()+"</p>" for x in lines]
    writetile=["<br/ >", \
               "<blockquote>", "<p>", "书卷多情似故人，晨昏忧乐每相亲。", "</p>", \
               "<footer>", "《观书》 于谦 【明】", "</footer> </blockquote>"
               "<br/ >", "</div>", "</body>", "</html>"]
    with open(htmlname+".html", "w") as html:
        html.writelines(writehead)
        html.writelines(writetitle)
        html.writelines(writelist)
        html.writelines(writetile)
    print("OK!")

txt=sys.argv[1]

main(txt)