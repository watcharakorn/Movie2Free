#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib
import urllib2
import re
import xbmcplugin
import xbmcgui
import xbmc
import xbmcaddon
import HTMLParser
import xmltosrt
import base64
import json

from idlelib.ReplaceDialog import replace
from Tkconstants import YES
h = HTMLParser.HTMLParser()


version = '1.0.0'
addon_id = 'plugin.video.movie2free'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'

REMOTE_DBG = False
 
# append pydev remote debugger
if REMOTE_DBG:
    # Make pydev debugger works for auto reload.
    # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
    sys.path.insert(0, 'C:\Program Files\eclipse\plugins\org.python.pydev_3.9.2.201502050007\pysrc')
#     #C:\Program Files\eclipse\plugins\org.python.pydev_3.9.2.201502050007\pysrc
#     sys.stderr.write(sys.path)
    try:
        import pysrc.pydevd as pydevd # with the addon script.module.pydevd, only use `import pydevd`
    # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
        pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True)
    except ImportError:
        sys.stderr.write("Error: " +
            "You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")
        sys.exit(1)

################################################## 

#MENUS############################################
def CATEGORIES():
    addDir('หมวดหมู่หนัง','categories',1,artfolder + 'Category.jpg')
    addDir('ประเภทหนัง','genre',3,artfolder + 'Type.jpg')
    #addDir('ค้นหา','-',6,artfolder + 'bluray.jpg')
    

###################################################################################
#FUNCOES
def categories():
    addDir('หนังเพิ่มใหม่','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%9d%e0%b8%a3%e0%b8%b1%e0%b9%88%e0%b8%87/',2,artfolder + 'NewUpdate.jpg')
    addDir('หนังไทย','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%84%e0%b8%97%e0%b8%a2/',2,artfolder + 'Thai.jpg')
    addDir('หนังเอเชีย','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%80%e0%b8%ad%e0%b9%80%e0%b8%8a%e0%b8%b5%e0%b8%a2/',2,artfolder + 'Asia.jpg')
    addDir('หนังฝรั่ง','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%9d%e0%b8%a3%e0%b8%b1%e0%b9%88%e0%b8%87/',2,artfolder + 'English.jpg')
    addDir('หนังภาคต่อ','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%a0%e0%b8%b2%e0%b8%84%e0%b8%95%e0%b9%88%e0%b8%ad/',2,artfolder + 'Episode.jpg')
    addDir('หนังการ์ตูน','http://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%8c%e0%b8%95%e0%b8%b9%e0%b8%99/',2,artfolder + 'Cartoon.jpg')
    addDir('การ์ตูนภาคต่อ','http://www.movie2free.com/category/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%8c%e0%b8%95%e0%b8%b9%e0%b8%99%e0%b8%a0%e0%b8%b2%e0%b8%84%e0%b8%95%e0%b9%88%e0%b8%ad/',2,artfolder + 'CartoonEp.jpg')
    addDir('คนชอบมากที่สุด','http://www.movie2free.com/%e0%b8%84%e0%b8%99%e0%b8%8a%e0%b8%ad%e0%b8%9a%e0%b8%a1%e0%b8%b2%e0%b8%81%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%aa%e0%b8%b8%e0%b8%94/',2,artfolder + 'Like.jpg')

def genre():
    addDir('Action บู๊','http://www.movie2free.com/category/action/',2,artfolder + 'Action.jpg')
    addDir('Adventure ผจญภัย','http://www.movie2free.com/category/adventure/',2,artfolder + 'Adventure.jpg')
    addDir('Animation การ์ตูน','http://www.movie2free.com/category/animation/',2,artfolder + 'Animation.jpg')
    addDir('Biography ชีวิตจริง','http://www.movie2free.com/category/biography/',2,artfolder + 'Biography.jpg')
    addDir('Comedy ตลก','http://www.movie2free.com/category/comedy/',2,artfolder + 'Comedy.jpg')
    addDir('Crime อาชญากรรม','http://www.movie2free.com/category/crime/',2,artfolder + 'Crime.jpg')
    addDir('Documentary สารคดี','http://www.movie2free.com/category/documentary/',2,artfolder + 'Documentary.jpg')
    addDir('Drama ชีวิต','http://www.movie2free.com/category/drama/',2,artfolder + 'Drama.jpg')
    addDir('Family ครอบครัว','http://www.movie2free.com/category/action/',2,artfolder + 'Family.jpg')
    addDir('Fantasy เทพนิยาย','http://www.movie2free.com/category/fantasy/',2,artfolder + 'Fantasy.jpg')
    addDir('History ประวัติศาสตร์ ','http://www.movie2free.com/category/history/',2,artfolder + 'History.jpg')
    addDir('Horror สยองขวัญ','http://www.movie2free.com/category/horror/',2,artfolder + 'Horror.jpg')
    addDir('Musical เพลง','http://www.movie2free.com/category/musical/',2,artfolder + 'Musical.jpg')
    addDir('Mystery ลึกลับซ่อนเงื่อน','http://www.movie2free.com/category/mystery/',2,artfolder + 'Mystery.jpg')
    addDir('Romance โรแมนติก','http://www.movie2free.com/category/romance/',2,artfolder + 'Romance.jpg')
    addDir('Sci-Fi วิทยาศาสตร์','http://www.movie2free.com/category/sci-fi/',2,artfolder + 'Scifi.jpg')
    addDir('Sport กีฬา','http://www.movie2free.com/category/sport/',2,artfolder + 'Sport.jpg')
    addDir('Thriller ระทึกขวัญ','http://www.movie2free.com/category/thriller/',2,artfolder + 'Thiller.jpg')
    addDir('War สงคราม ','http://www.movie2free.com/category/war/',2,artfolder + 'War.jpg')
    addDir('Western คาวบอยตะวันตก','http://www.movie2free.com/category/western/',2,artfolder + 'Western.jpg')

def list_videos(url):
    html = open_url(url)
    html = html.replace('\n','')
    
    moviefilm = re.compile('<div class="moviefilm">.+?<a href="(.+?)">.+?<p>(.+?)</p>.+?<img src="(.+?)".+?font-size: 12px; ">(.+?)</div></div>').findall(html)

    a = []

    for y in range(0, len(moviefilm)):
        temp = [moviefilm[y][0],moviefilm[y][1],moviefilm[y][2],moviefilm[y][3]]; 
        a.append(temp)
        
    total = len(a)
    for url2, title, img, mstyle in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'")	
        addDir(title,url2,4,img,True,total)

    page = re.compile('<div class="navigation"><ul>(.+?)</ul></div>').findall(html)
    if len(page)>0:
        navigation = page[0]
        page = re.compile('<a href="(.+?)"(.+?)</a>').findall(navigation)
        for x in range(0, len(page)):
            if page[x][1]==' >หน้าต่อไป':
                addDir('Next Page >>',page[x][0],2,artfolder + 'Next.png')
                break



def list_episodes(url):
    html = open_url(url)
    html = html.replace('\n','')
    movieinfo = re.compile('<div class="filmaltiimg">.+?<img src="(.+?)".+?alt="(.+?)" height=').findall(html)
    movie_img =''
    movie_name =''
    if len(movieinfo) > 0:
        movie_img = movieinfo[0][0]
        movie_name  = movieinfo[0][1]
        movie_name = movie_name.replace('&#8211;',"-").replace('&#8217;',"'")
    a = []    
    #TH - HD
    episode = re.compile('jwplayer\("fileTH_HD"\).setup\({.+?sources: (.+?)}\);').findall(html)

    for y in range(0, len(episode)):
        episode[y] = episode[y].replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'","\"")
        

        episode[y] = episode[y][:len(episode[y])-2]
        json_data = json.loads(episode[y])
        for source in json_data:
            url = str(source['file']) 
            title = movie_name + ' (พากย์ไทย HD ' + str(source['label']) +')'
            stype = str(source['type'])
            temp = [url,title,movie_img,stype] 
            a.append(temp)
    #TH - SD
    episode = re.compile('jwplayer\("fileTH_SD"\).setup\({.+?sources: (.+?)}\);').findall(html)

    for y in range(0, len(episode)):
        episode[y] = episode[y].replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'","\"")
        

        episode[y] = episode[y][:len(episode[y])-2]
        json_data = json.loads(episode[y])
        for source in json_data:
            url = str(source['file'])
            title = movie_name + ' (พากย์ไทย SD ' + str(source['label']) +')'
            stype = str(source['type'])
            temp = [url,title,movie_img,stype] 
            a.append(temp)
     #EN - HD
    episode = re.compile('jwplayer\("fileEN_HD"\).setup\({.+?sources: (.+?)}\);').findall(html)

    for y in range(0, len(episode)):
        episode[y] = episode[y].replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'","\"")
        

        episode[y] = episode[y][:len(episode[y])-2]
        #episode[y] = "{'source':" +  episode[y]
        json_data = json.loads(episode[y])
        for source in json_data:
            url = str(source['file'])
            title = movie_name + ' (ซับไทย HD ' + str(source['label']) +')'
            stype = str(source['type'])
            temp = [url,title,movie_img,stype] 
            a.append(temp)
            
    #TH - SD
    episode = re.compile('jwplayer\("fileEN_SD"\).setup\({.+?sources: (.+?)}\);').findall(html)


    for y in range(0, len(episode)):
        episode[y] = episode[y].replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'","\"")
        

        episode[y] = episode[y][:len(episode[y])-2]
        json_data = json.loads(episode[y])
        for source in json_data:
            url = str(source['file'])
            title = movie_name + ' (ซับไทย SD ' + str(source['label']) +')'
            stype = str(source['type'])
            temp = [url,title,movie_img,stype] 
            a.append(temp)
               
    total = len(a)
    for url2, title, img, mstyle in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'")    
        addLink(title,url2,img)

def list_searchvideos(url):
    
    html = open_url(url)
    html = html.replace('\n','')
    
    moviefilm = re.compile('<div class="gs-webResult gs-result">.+?href="(.+?)" target=".+?" src="(.+?)"></a>').findall(html)
    tmp = re.compile('<div class="gs-webResult gs-result">(.+?)</div>').findall(html)
    a = []

    for y in range(0, len(moviefilm)):
        link = moviefilm.split('/')
        if len(link)==5:
            if link[0]=='http' and link[2]=='www.movie2free' and len(link[3]) >0:
                temp = [moviefilm[y][0],link[3],moviefilm[y][1]]; 
                a.append(temp)
                
        total = len(a)
        for url2, title, img in a:
            title = title.replace('&#8211;',"-").replace('&#8217;',"'")    
            addDir(title,url2,4,img,True,total)

    page = re.compile('(.+?)gsc.page=(.+?)').findall(url)
    if len(page)>0:
        nextpage = int(page[0][1]) + 1 
        page = page[0][0] + 'gsc.page=' + str(nextpage)
        addDir('หน้าต่อไป >>',page,2,artfolder + 'Next.png')
                


def search():
    keyb = xbmc.Keyboard('', 'Search') 
    keyb.doModal() 
    if (keyb.isConfirmed()): 
        search = keyb.getText() 
        parameter_search=urllib.quote(search) 
        if len(parameter_search) > 0:
            q = parameter_search.replace(' ','+')
            qplus = q.replace('++','+')
            while q <> qplus:
                q = qplus
                qplus = q.replace('++','+')
            url = 'http://www.google.com/cse?cx=000233484462069881809%3Aqzqsq4rpiy0&q=' + str(qplus) +'#gsc.tab=0&gsc.q=' + str(parameter_search) + '&gsc.page=1'
            list_searchvideos(url) 
        
        ###################################################################################
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def real_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.geturl()
    response.close()
    return link

def addLink(name,url,iconimage):
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
    return ok

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

    return param

params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass

try:        
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)




###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
    print ""
    CATEGORIES()

elif mode==1:
    print ""
    categories()
elif mode==3:
    print ""
    genre()
    
elif mode==2:
    print ""
    list_videos(url)

elif mode==6:
    print ""
    search()

elif mode==4:
    print ""
    list_episodes(url)
elif mode==None and len(url)>0:
    print ""
    playVideo(handle,name,iconimage,url)
    
    #player(name,url,iconimage)
    #listar_temporadas(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))