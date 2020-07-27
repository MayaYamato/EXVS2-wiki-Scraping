import os
import re
import requests
import urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)))
download_dir = os.getcwd()+r'/EXVS2_wiki'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
filename = os.path.basename('https://w.atwiki.jp/exvs2/pages/1.html')

with urllib.request.urlopen('https://w.atwiki.jp/exvs2/pages/1.html') as response:
    html = response.read().decode()
    seiki30 = r'<li><a href="//w.atwiki.jp/exvs2/pages/258.html"(.|\s)*?</a></li></ul>'
    reseiki30 = re.search(seiki30, html).group()
    seiki25 = r'<li><a href="//w.atwiki.jp/exvs2/pages/140.html"(.|\s)*?</a></li></ul>'
    reseiki25 = re.search(seiki25, html).group()
    seiki20 = r'<li><a href="//w.atwiki.jp/exvs2/pages/41.html"(.|\s)*?</a></li></ul>'
    reseiki20 = re.search(seiki20, html).group()
    seiki15 = r'<li><a href="//w.atwiki.jp/exvs2/pages/204.html"(.|\s)*?</a></li></ul>'
    reseiki15 = re.search(seiki15, html).group()

    all = reseiki30+r'\n'+reseiki25+r'\n'+reseiki20+r'\n'+reseiki15
    t = re.sub(r'^(?!.*//w.atwiki.jp/exvs2/pages/).*$','',re.sub('</a>',r'\n',all))

    for line in t.split("\n"): #split("\n") 改行でライン化
        seiki = r'^(?!.*//w.atwiki.jp/exvs2/pages/).*$'
        line = re.sub(seiki,'',line)
        #line = re.sub(r'^\n|\r','',line) #何故かこっちではABIと違って上手くいかない
        if len(line) == 0: #ABIの方とは別にこれで対処
            del line
        else:
            line = re.sub('<li>スターウイニングガンダム<br /><a href="','https:',line)
            line = line.replace(r'</li></ul>\n<li><a href="','https:') # 正規表現要素(\nの字そのものとか)含む場合はこれ
            line = re.sub('<br /><a href="','https:',line)
            line = re.sub('<li><a href="','https:',line)
            line = re.sub('/<a href="','https:',line)
            print(line.partition('"')[0])
            #title = re.search(">(.|\s)*?\n",line).group() #(、>が正規表現で引っかかる)
            title = line.split('title="')[-1].split('(')[0]
            print(title)
            filename = title 
            with urllib.request.urlopen(line.partition('"')[0]) as response:
                html = response.read().decode()
                # html = html.replace('\xa0', '')
                # html = html.replace('\u5699', '')
                # html = html.replace('\u6414', '')
                seiki1 = r'<h2><a href=(.|\s)*?twitter' #改行入る場合は(.|\s)*?
                #seiki2 = r'<h2 id(.|\s)*?<h2 id="id_25eb9077">'
                reseiki1 = re.search(seiki1, html).group()
                #reseiki2 = re.search(seiki2, html).group()
                reseiki1= reseiki1.encode('utf-8') #UnicodeERROR回避
                with open(download_dir+'/'+str(title)+'.html',"wb") as f:
                    if os.path.exists(download_dir+'/'+str(title)+'.html'):
                        for n in range (1, 10):
                            new_filename = str(filename)  + '(' + str(n) + ')'
                            if not os.path.exists(download_dir+'/'+str(new_filename)+'.html'):
                                f.write(reseiki1)
                                #f.write(reseiki2)
                                break
                            else:
                                continue
                    else:
                        f.write(reseiki1)
                        #f.write(reseiki2)


            #動作確認用
            # with open(download_dir+'/'+str(filename)+'.txt',"a") as f:
            #     f.write(line)
            #     f.write('\n') #改行入れる場合はこっち　✖r'\n'


                # seiki1 = r'//w.atwiki.jp/exvs2/pages(.|\s)*?.html'
                # seiki2 = r'title="(.|\s)*?"'
                # reseiki1 = re.search(seiki1, line).group() #一行に複数ある場合に対応できてない
                # reseiki2 = re.search(seiki2, line).group()

### 方針
# title= と何かで挟んで機体名を取得する 取得した後はURL読み込みの邪魔なので消す
# 整形できたらそれを下のコードを関数化した奴に関数に渡す
# 個人的に複数回ファイル開くの癪なので何とかしたい


    
# with open(download_dir+r'/'+str(filename)+'.txt',"w") as f:
#     f.write(t)

# with open(download_dir+r'/'+str(filename)+'.txt',"r") as f:
#     for line in f:
#         seiki = r'^(?!.*//w.atwiki.jp/exvs2/pages/).*$'
#         new_txt = re.sub(seiki,'',line)
#         print(new_txt)
#         with open(download_dir+'/'+str(filename)+'1.txt',"a") as f:
#             f.write(new_txt)


    # for line in f:
    #     #print(line)
    #     seiki1 = r'//w.atwiki.jp/exvs2/pages(.|\s)*?.html'
    #     seiki2 = r'title="(.|\s)*?"'
    #     reseiki1 = re.search(seiki1, line).group() #一行に複数ある場合に対応できてない 
    #     reseiki2 = re.search(seiki2, line).group()
    #     #print(reseiki1)




