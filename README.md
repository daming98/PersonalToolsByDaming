# 自用小工具
## 1. DeleteWeibo
描述：可以批量发微博和删微博，需要输入验证码的时候要在控制台输入。

需要：selenium、Python 3、Chrome（如果用别的浏览器的话需要下载相应的驱动）

怎么使用：
1. 打开 deleteWeibo.py ，修改里面的 username 和 password 的值。还有浏览器驱动那一部分需要根据情况修改。
2. 根据需要在文件里写函数调用语句。
2. 在控制台运行 python deleteWeibo.py
3. 当要求你输入验证码时输入验证码。

PS：可能以后会增加功能，修正稳定性，可能。
## 2. Txt2Html
描述：发现我妈每天看的文章都很没意思，所以我想每天选一篇我觉得值得一读的发给她，但她习惯用手机阅读，直接发 txt 给她她就会嫌麻烦，所以我想把 txt 转成 HTML，挂到我的服务器上让她读。~~因为是临时的决定，所以就没有任何的 CSS，只是把字号调大，因为字太小的话她也不愿意读了。~~ 使用了 Bootstrip 的静态样式，使标题和段落更适合阅读，并且添加了页尾。

需要：Python 3

怎么使用：
1. 准备好一个txt文件，第一行应该形如 `《[文章题目]》[作者]`
2. 打开 txt2html.py 修改里面的一些参数，比如 htmltitle 代表这个 HTML 的 <title>。
3.  `python txt2html.py [txt文件]` 
4. 检查生成的 HTML 文件，文件名为文章标题。

PS：可能以后会增加~~好看的~~更多的样式和功能，可能。
## 3. SinaBlogCrawler
描述：突然怀念起当年扒偶像博客的时光，所以写了个爬虫扒许嵩的博客，不过他已经好多年没写过博客了。

需要：Python 3

怎么使用：
1. 打开最新的一篇博文，复制这篇博文的链接。
2. 通过demo.py里的get_url_list方法获取全部博文的链接。
3. 通过vae_blog.py来将全部博文保存到txt文件里。

PS：新浪博客新几年的html结构可能有些变化，这个爬虫或许只适用于2012年以前的博客。但我哥2012年以后没更博客了，我就不重新适配了。
