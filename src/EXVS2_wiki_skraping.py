import os
import re
import codecs
import requests
import urllib.error
import urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)))
download_dir = os.getcwd()+r'/EXVS2_wiki'

tmp0=input('wikiの抽出したいページURLを指定して\n>>')
filename = os.path.basename(tmp0)
if not os.path.exists(download_dir):
        os.makedirs(download_dir)
with urllib.request.urlopen(tmp0) as response:
    html = response.read().decode()
    seiki1 = '<h2><a href=(.|\s)*?</table>' #うまく行く 改行入る場合はこっちがいい？
    #seiki1 = '<h2><a href=(.+)</table>' "上手くいかない"
    seiki2 = '<h2 id(.|\s)*?<h2 id="id_25eb9077">'
    reseiki1 = re.search(seiki1, html).group()
    reseiki2 = re.search(seiki2, html).group()
    with open(download_dir+'/'+str(filename),"w") as f:
        f.write(reseiki1)
        f.write('\n')
        f.write(reseiki2)