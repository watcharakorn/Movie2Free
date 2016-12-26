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
import httplib
import socket
import ssl
import re
import xbmcplugin
import xbmcgui
import xbmc
import xbmcaddon
import HTMLParser
#import xmltosrt
import base64
import json
import os
#from .resoucres.lib.ReplaceDialog import replace
#from .resources.lib.Tkconstants import YES
# from idlelib.ReplaceDialog import replace
# from Tkconstants import YES
h = HTMLParser.HTMLParser()
wrap_socket_orig = ssl.wrap_socket

_strings = {}

STRINGS = {
    'addontitle': 00000,
    'page': 00001,
    'back': 00002,
    'next': 00003,
    'exit': 00004,
    'nextpage': 00005,
    'img_path': 00006,
    'thai_hd': 90001,
    'thai_sd': 90002,
    'sub_hd': 90003,
    'sub_sd': 90004,    
    'download': 60000,
    'download_in_progress': 70000,
    'downloaded': 70001,
    'menu_category': 10000,
    'menu_genre': 10001,
    'menu_search': 10002,
    'menu_tv': 10003,  
    'menu_youtube': 10004,        
    'menu_serie':11001,
    'menu_addnew': 20000,
    'menu_thai': 20001,
    'menu_asia': 20002,
    'menu_international': 20003,
    'menu_sequel': 20004,
    'menu_cartoon': 20005,
    'menu_sequelcartton': 20006,
    'menu_favorite': 20007,
    'menu_newmovie': 20008,
    'menu_serie_english':21001,
    'menu_serie_korea':21002,
    'menu_serie_japan':21003,
    'menu_serie_china':21004,
    'genre_action': 30000,
    'genre_adventure': 30001,
    'genre_cartoon': 30002,
    'genre_bioghapy': 30003,
    'genre_comedy': 30004,
    'genre_crime': 30005,
    'genre_documentary': 30006,
    'genre_drama': 30007,
    'genre_family': 30008,
    'genre_fantasy': 30009,
    'genre_history': 30010,
    'genre_horror': 30011,
    'genre_musical': 30012,
    'genre_mystery': 30013,
    'genre_romance': 30014,
    'genre_scifi': 30015,
    'genre_sport': 30016,
    'genre_thiller': 30017,
    'genre_war': 30018,
    'genre_western': 30019,
    'tv_freetv': 30100,
    'tv_cartoon': 30200,
    'tv_variety': 30300,
    'tv_sport': 30400,
    'tv_knowledge': 30500,
    'tv_international': 30600,
    'tv_local': 30700,
    'tv_all': 30800,
    'no_download_path': 60001,
    'want_set_now': 60002,
    'site_unavailable': 60003,
    'try_again_later': 60004,
    'notification': 60005,
    'network_error': 70002,
    'show_my_favs': 80000,
    'add_to_my_favs': 80001,
    'del_from_my_favs': 80002,
    'no_my_favs': 80003,
    'use_context_menu': 80004,
    'to_add': 90005

}

_mResolution = ['360p', '480p','720p','1080p']

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

    addDir(_('menu_category'),'categories',1,artfolder + 'Category.jpg')
    addDir(_('menu_genre'),'genre',3,artfolder + 'Type.jpg')
    addDir(_('menu_search'),'-',6,artfolder + 'Search.jpg')
    addDir(_('menu_serie'),'serie_categories',9,artfolder + 'Serie.jpg')
    addDir(_('menu_tv'),'http://m.thaiptv.com/',8,artfolder + 'TvOnline.jpg')
    #addLink(_('menu_youtube'),'https://www.youtube.com/embed/Cl-uA0QwRgg?feature=oembed',artfolder + 'Youtube.jpg')
    
###################################################################################
#SUBMENU
def categories():
    addDir(_('menu_addnew'),'https://www.movie2free.com/',2,artfolder + 'NewUpdate.jpg')
    addDir(_('menu_newmovie'),'https://www.movie2free.com/category/%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AD%E0%B8%AD%E0%B8%81%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88/',2,artfolder + 'NewUpdate.jpg')
    addDir(_('menu_thai'),'https://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%84%e0%b8%97%e0%b8%a2/',2,artfolder + 'Thai.jpg')
    addDir(_('menu_asia'),'https://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%80%e0%b8%ad%e0%b9%80%e0%b8%8a%e0%b8%b5%e0%b8%a2/',2,artfolder + 'Asia.jpg')
    addDir(_('menu_international'),'https://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%9d%e0%b8%a3%e0%b8%b1%e0%b9%88%e0%b8%87/',2,artfolder + 'English.jpg')
    addDir(_('menu_sequel'),'https://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%a0%e0%b8%b2%e0%b8%84%e0%b8%95%e0%b9%88%e0%b8%ad/',2,artfolder + 'Episode.jpg')
    addDir(_('menu_cartoon'),'https://www.movie2free.com/category/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%8c%e0%b8%95%e0%b8%b9%e0%b8%99/',2,artfolder + 'Cartoon.jpg')
    addDir(_('menu_sequelcartton'),'https://www.movie2free.com/category/%e0%b8%81%e0%b8%b2%e0%b8%a3%e0%b9%8c%e0%b8%95%e0%b8%b9%e0%b8%99%e0%b8%a0%e0%b8%b2%e0%b8%84%e0%b8%95%e0%b9%88%e0%b8%ad/',2,artfolder + 'CartoonEp.jpg')
    addDir(_('menu_favorite'),'https://www.movie2free.com/%e0%b8%84%e0%b8%99%e0%b8%8a%e0%b8%ad%e0%b8%9a%e0%b8%a1%e0%b8%b2%e0%b8%81%e0%b8%97%e0%b8%b5%e0%b9%88%e0%b8%aa%e0%b8%b8%e0%b8%94/',2,artfolder + 'Like.jpg')

def genre():

    addDir(_('genre_action'),'http://www.movie2free.com/category/action/',2,artfolder + 'Action.jpg')
    addDir(_('genre_adventure'),'http://www.movie2free.com/category/adventure/',2,artfolder + 'Adventure.jpg')
    addDir(_('genre_cartoon'),'http://www.movie2free.com/category/animation/',2,artfolder + 'Animation.jpg')
    addDir(_('genre_bioghapy'),'http://www.movie2free.com/category/biography/',2,artfolder + 'Biography.jpg')
    addDir(_('genre_comedy'),'http://www.movie2free.com/category/comedy/',2,artfolder + 'Comedy.jpg')
    addDir(_('genre_crime'),'http://www.movie2free.com/category/crime/',2,artfolder + 'Crime.jpg')
    addDir(_('genre_documentary'),'http://www.movie2free.com/category/documentary/',2,artfolder + 'Documentary.jpg')
    addDir(_('genre_drama'),'http://www.movie2free.com/category/drama/',2,artfolder + 'Drama.jpg')
    addDir(_('genre_family'),'http://www.movie2free.com/category/action/',2,artfolder + 'Family.jpg')
    addDir(_('genre_fantasy'),'http://www.movie2free.com/category/fantasy/',2,artfolder + 'Fantasy.jpg')
    addDir(_('genre_history'),'http://www.movie2free.com/category/history/',2,artfolder + 'History.jpg')
    addDir(_('genre_horror'),'http://www.movie2free.com/category/horror/',2,artfolder + 'Horror.jpg')
    addDir(_('genre_musical'),'http://www.movie2free.com/category/musical/',2,artfolder + 'Musical.jpg')
    addDir(_('genre_mystery'),'http://www.movie2free.com/category/mystery/',2,artfolder + 'Mystery.jpg')
    addDir(_('genre_romance'),'http://www.movie2free.com/category/romance/',2,artfolder + 'Romance.jpg')
    addDir(_('genre_scifi'),'http://www.movie2free.com/category/sci-fi/',2,artfolder + 'Scifi.jpg')
    addDir(_('genre_sport'),'http://www.movie2free.com/category/sport/',2,artfolder + 'Sport.jpg')
    addDir(_('genre_thiller'),'http://www.movie2free.com/category/thriller/',2,artfolder + 'Thiller.jpg')
    addDir(_('genre_war'),'http://www.movie2free.com/category/war/',2,artfolder + 'War.jpg')
    addDir(_('genre_western'),'http://www.movie2free.com/category/western/',2,artfolder + 'Western.jpg')

def list_tvchannel(url):
    html = open_url(url)
    html = html.replace('\n','')
    #print html
    #tvchannel = re.compile('<td width="13%" valign="top" bgcolor="#DCDFE7">.+?<a href="(.+?)">.+?src="(.+?)".+?<a href="(.+?)">(.+?)"</a></span><br>').findall(html)
    tvchannel = re.compile('<td width="13%" valign="top" bgcolor="#DCDFE7"><a href="(.+?)"><img alt="TVLOGO" border="0" height="92" src="(.+?)" width="92"/></a></td>.+?<a target="_top" href="(.+?)">(.+?)</a>').findall(html)
    a = []                                                                                                                                      

    temp = ['http://edge1.psitv.tv:1935/liveedge/292277227873_300/playlist.m3u8','http://www.onlinethailand.net/tv_online/images/workpoint-tv.jpg','Workpoint TV'];
    a.append(temp)
    
    for y in range(0, len(tvchannel)):
        temp = [tvchannel[y][0],tvchannel[y][1],tvchannel[y][3]]; 
        a.append(temp)
        
    total = len(a)
    for url2, img, title in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '') 	        
        addLink(title,url2,img)


def list_videos(url):
    html = open_url(url)
    html = html.replace('\n','')
    
    moviefilm = re.compile('<div class="movie-box">.+?<a href="(.+?)">.+?<span>(.+?)</span>.+?<img src="(.+?)"').findall(html)

    a = []

    for y in range(0, len(moviefilm)):
        temp = [moviefilm[y][0],moviefilm[y][1],moviefilm[y][2]]; 
        a.append(temp)
        
    total = len(a)
    for url2, title, img in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '') 	
        addDir(title,url2,4,img,True,total)

    page = re.compile('<div class="navigation">.+?<ul>(.+?)</ul>').findall(html)
    if len(page)>0:
        navigation = page[0]
        page = re.compile('<a href="(.+?)"(.+?)</a>').findall(navigation)
        for x in range(0, len(page)):
            if page[x][1]=='>ต่อไป':
                addDir(_('nextpage')+' >>',page[x][0],2,artfolder + 'Next.jpg')
                break



def list_episodes(url):
    html = open_url(url)
    html = html.replace('\n','') 
    
    movieinfo = re.compile('<div class="movie-header">.+?<img src="(.+?)".+?<strong>(.+?)</strong>').findall(html)
    movie_img =''
    movie_name =''
    episode = ''
    if len(movieinfo) > 0:
        movie_img = movieinfo[0][0]
        movie_name  = movieinfo[0][1]
        #movie_name = movie_name.replace('&#8211;',"-").replace('&#8217;',"'")
    a = []    
    #TH - HD
    #episode = re.compile('jwplayer\("fileTH_HD"\).setup\({.+?sources: s\((.+?)\)').findall(html)
    #episode = re.compile('jwplayer\("player-th"\).setup\({.+?sources: (.+?)}]').findall(html)
    episodelink = re.compile('create\("(.+?)", "#btn-swtich-th"').findall(html)
    
    
    for y in range(0, len(episodelink)):
        if len(episodelink[y])>0:
            episodelink[y] = episodelink[y].replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
            episode = open_url(episodelink[y]) 
    
    if len(episode) > 0:
                    
        if episode.find('"sources":') >=0:
            #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
            episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
            #episode = '[' + episode +'}]'                
            json_data = json.loads(episode)
            for sources in json_data['sources']:
                url = str(sources['url'])
                title = movie_name + ' (' + _('thai_hd') +' ' + str(sources['quality']) +')'
                stype = str(sources['type'])
                if len(url)>0:
                    temp = [url,title,movie_img,stype] 
                    a.append(temp)
    else:
        episodelink = re.compile('create\(\[(.+?), "#btn-swtich-th"').findall(html)
        for y in range(0, len(episodelink)):
            if len(episodelink[y])>0:
                episode = '{"sources":[' + episodelink[y] + '}'
                if episode.find('"file":') >=0:
                    #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
                    episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')               
                    json_data = json.loads(episode)
                    for sources in json_data['sources']:
                        url = str(sources['file'])
                        title = movie_name + ' (' + _('thai_hd') +' ' + str(sources['label']) +')'
                        stype = str(sources['type'])
                        if len(url)>0:
                            temp = [url,title,movie_img,stype] 
                            a.append(temp)
        
    episodelink = re.compile('create\("(.+?)", "#btn-swtich-en"').findall(html)
    episode = ''
    
    for y in range(0, len(episodelink)):
        if len(episodelink[y])>0:
            episodelink[y] = episodelink[y].replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
            episode = open_url(episodelink[y]) 
    
    if len(episode) > 0:
                    
        if episode.find('"sources":') >=0:
            #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
            episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
            #episode = '[' + episode +'}]'                
            json_data = json.loads(episode)
            for sources in json_data['sources']:
                url = str(sources['url'])
                title = movie_name + ' (' + _('sub_hd') +' ' + str(sources['quality']) +')'
                stype = str(sources['type'])
                if len(url)>0:
                    temp = [url,title,movie_img,stype] 
                    a.append(temp)               
    else:
        episodelink = re.compile('create\(\[(.+?), "#btn-swtich-en"').findall(html)
        for y in range(0, len(episodelink)):
            if len(episodelink[y])>0:
                episode = '{"sources":[' + episodelink[y] + '}'
                if episode.find('"file":') >=0:
                    #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
                    episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')               
                    json_data = json.loads(episode)
                    for sources in json_data['sources']:
                        url = str(sources['file'])
                        title = movie_name + ' (' + _('sub_hd') +' ' + str(sources['label']) +')'
                        stype = str(sources['type'])
                        if len(url)>0:
                            temp = [url,title,movie_img,stype] 
                            a.append(temp)


    episodelink = re.compile('var \$data = (.+?)"}]};').findall(html)
    
    if len(episodelink) >0:
        episodelink[0] = episodelink[0]+'"}]}'
        json_movie = json.loads(episodelink[0])
        episode_title = json_movie['title']
        for datas in json_movie['data']:
            episodelnk = str(datas['data'])            
            subtitle = datas['title']
            
            if len(episodelnk)>0 and episodelnk<>'None':                
                episodelnk.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
                episode = open_url(episodelnk)
        
                if len(episode) > 0:
                                
                    if episode.find('"sources":') >=0:
                        #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
                        episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/')
                        #episode = '[' + episode +'}]'                
                        json_data = json.loads(episode)
                        for sources in json_data['sources']:
                            url = str(sources['url'])
                            title = episode_title + ' (' + subtitle +' ' + str(sources['quality']) +')'
                            stype = str(sources['type'])
                            if len(url)>0:
                                temp = [url,title,movie_img,stype] 
                                a.append(temp)

                             
    for url2, title, img, stype in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '') 
        if len(title)>0 and len(url2)>0:    
            addLink(title,url2,img)

def list_search(url):
    html = open_url(url)
    json_data = json.loads(html)
    a = []
    if json_data['responseStatus'] == 200:
        for serachresult in json_data['responseData']['results']:
            movie_url = serachresult['richSnippet']['metatags']['ogUrl']
            movie_title = serachresult['richSnippet']['metatags']['ogTitle']
            movie_img = serachresult['richSnippet']['cseImage']['src']
            exist = False
            for i in range(0,len(a)):
                if movie_url==a[i][0]:
                    exist = True
                    break
            if exist == False:
                #movie_name,movie_img = get_movieinfo(moviefilm[y][0])
                #movie_name = link[3]
                #movie_img = ''
                temp = [movie_url,movie_title,movie_img]; 
                a.append(temp)            
            
            
        #total = int(json_data['responseData']['cursor']['resultCount'])  
        total = len(a)      
        for url1, title, img in a:
              
            if len(title)>0 and len(url1)>0: 
                url2 = url1.encode('utf-8')
                title2 = title.encode('utf-8')   
                img2 = img.encode('utf-8') 
                title2 = title2.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace(' - เว็บดูหนังออนไลน์ HD Movie2free.com ฟรี','').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '')
                if title2 <> 'คนชอบมากที่สุด' and title2 <> 'คนดูมากที่สุด':
                    addDir(title2,url2,4,img2,True,total)
                
        if (int(json_data['responseData']['cursor']['currentPageIndex']) *20 +20) < 100:
            if int(json_data['responseData']['cursor']['currentPageIndex']+1)*20 < int(json_data['responseData']['cursor']['resultCount']):
                page = url.replace('start=' + str(json_data['responseData']['cursor']['currentPageIndex'] * 20),'start=' + str(json_data['responseData']['cursor']['currentPageIndex']*20+20))
                addDir(_('nextpage')+' >>',page,7,artfolder + 'Next.jpg')
          
                                                                     
def list_searchvideos(url):
    
    html = open_url(url)
    html = html.replace('\n','')
    
    moviefilm = re.compile('<a class="l" href="(.+?)".+?">(.+?)</a>').findall(html)

    a = []

    for y in range(0, len(moviefilm)):
        link = moviefilm[y][0].split('/')
        title = moviefilm[y][1]
        if len(link)==5:
            if link[0]=='http:' and link[2]=='www.movie2free.com' and len(link[3])>0 and len(link[4])==0 and link[3]<>'checktrailer':
                exist = False
                for i in range(0,len(a)):
                    if moviefilm[y][0]==a[i][0]:
                        exist = True
                        break
                if exist == False:
                    movie_name,movie_img = get_movieinfo(moviefilm[y][0])
                    #movie_name = link[3]
                    #movie_img = ''
                    temp = [moviefilm[y][0],movie_name,movie_img]; 
                    a.append(temp)
    total = len(a)        
    for url2, title, img in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '')  
        if len(title)>0 and len(url2)>0:     
            addDir(title,url2,4,img,True,total)
                

def get_movieinfo(url):
    html = open_url(url)
    html = html.replace('\n','')
    movieinfo = re.compile('<div class="filmaltiimg">.+?<img src="(.+?)".+?alt="(.+?)" height=').findall(html)
    movie_img =''
    movie_name =''
    if len(movieinfo) > 0:
        movie_img = movieinfo[0][0]
        movie_name  = movieinfo[0][1]
        movie_name = movie_name.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '')  
    return movie_name,movie_img

    
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
            qplus = qplus + '+-page+-tag+-category+-checktrailer'
            url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&cx=000233484462069881809%3Aqzqsq4rpiy0&q=' + str(qplus) + '&start=0&rsz=20'
            list_search(url)
        
        ###################################################################################
############################################################################################
# SERIES
############################################################################################
def serie_categories():    
    addDir(_('menu_serie_korea'),'https://www.doseries.com/%E0%B8%94%E0%B8%B9%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B9%8C%E0%B9%80%E0%B8%81%E0%B8%B2%E0%B8%AB%E0%B8%A5%E0%B8%B5/1.html?page=1',10,artfolder + 'serie_korea.jpg')    
    addDir(_('menu_serie_english'),'https://www.doseries.com/%E0%B8%94%E0%B8%B9%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B9%8C%E0%B8%9D%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%87/2.html?page=1',10,artfolder + 'serie_eng.jpg')    
    addDir(_('menu_serie_china'),'https://www.doseries.com/%E0%B8%94%E0%B8%B9%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B9%8C%E0%B8%88%E0%B8%B5%E0%B8%99-%E0%B9%84%E0%B8%95%E0%B9%89%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%99/3.html?page=1',10,artfolder + 'serie_china.jpg')
    addDir(_('menu_serie_japan'),'https://www.doseries.com/%E0%B8%94%E0%B8%B9%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B9%8C%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99/4.html?page=1',10,artfolder + 'serie_japan.jpg')
    #addDir(_('menu_serie_english'),'http://www.doolunla.com/category/%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B9%8C%E0%B8%9D%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%87%E0%B8%9E%E0%B8%B2%E0%B8%81%E0%B8%A2%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2/',10,artfolder + 'serie_eng.jpg')
    #addDir(_('menu_serie_korea'),'http://www.doolunla.com/category/%E0%B8%8B%E0%B8%B5%E0%B8%A3%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B9%8C%E0%B9%80%E0%B8%81%E0%B8%B2%E0%B8%AB%E0%B8%A5%E0%B8%B5%E0%B8%9E%E0%B8%B2%E0%B8%81%E0%B8%A2%E0%B9%8C%E0%B9%84%E0%B8%97%E0%B8%A2/',10,artfolder + 'serie_korea.jpg')
    
    

def serie_list_videos(url):
    html = open_url(url)
    html = html.replace('\n','')
    
    #moviefilm = re.compile('<div class="moviefilm"><a href="(.+?)"><img src="(.+?)".+?<div class="movief"><a href=".+?">(.+?)</a></div>').findall(html)
    moviefilm = re.compile('<div class="thumbnail thumbnail_01">.+?<img src="(.+?)".+?<a href="(.+?)">(.+?)</a>').findall(html)
    
    a = []

    for y in range(0, len(moviefilm)):
        temp = [moviefilm[y][0],'https://www.doseries.com'+moviefilm[y][1],moviefilm[y][2]]; 
        a.append(temp)
        
    total = len(a)
    for img ,url2, title in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '')     
        addDir(title,url2,11,img,True,total)

    pagination = re.compile('<ul class="pagination pagination-lg">(.+?)</li></ul>').findall(html)
    if len(pagination)>0:
        page = re.compile('<a href="(.+?)">(.+?)</a>').findall(pagination[0])
        for y in range(0, len(page)):
            if (page[y][1]=='Next'):
                navigation = page[y][0]
                addDir(_('nextpage')+' >>',navigation,10,artfolder + 'Next.jpg')
        

def serie_list_episodes(url,img):    
    html = open_url(url)
    html = html.replace('\n','')
    movieinfo = re.compile('<td class="size-01">.+? href="(.+?)".+?<td class="size-01">(.+?)</td>').findall(html)

    a = []
    
    for y in range(0, len(movieinfo)):
        temp = [movieinfo[y][0],movieinfo[y][1]]; 
        a.append(temp)
    
    total = len(a)
        
    for url2 , title in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '').replace('&#3637;', 'ี').replace('&#3656;', '่')
        #serie_play(url2,title,img)     
        addDir(title,url2,12,img,True,total)
        #addLink(title,url2,img)


def serie_play(url,name,img):            
    html = open_url(url)
    html = html.replace('\n','').replace('\'','"')    
    movieinfo = re.compile('<source src="(.+?)720.mp4" type="video/mp4"/>').findall(html)
    movie_img = img
    movie_name =''
    
    total = len(movieinfo)
    if total > 0 :
        for y in range(0, len(movieinfo)):
            movie_name = name
            episode = movieinfo[y]
            
            episode_link = episode+'360.mp4'            
            addLink(movie_name+' 360p',episode_link,movie_img)
            episode_link = episode+'480.mp4'            
            addLink(movie_name+' 480p',episode_link,movie_img)
            episode_link = episode+'720.mp4'            
            addLink(movie_name+' 720p',episode_link,movie_img)
    else:
        movieinfo = re.compile('<source src="(.+?)" type="video/mp4"/>').findall(html)
        total = len(movieinfo)
        if total > 0 :
            for y in range(0, len(movieinfo)):
                movie_name = name
                episode = movieinfo[y]
                addLink(movie_name,episode,movie_img)
        else:
            movieinfo = re.compile('<button class="btn btn-success" onclick="window.open\("(.+?)"').findall(html)
            total = len(movieinfo)
            if total > 0 :
                for y in range(0, len(movieinfo)):
                    movie_name = name
                    episode = movieinfo[y]
                    addDir(movie_name,episode,21,img,True,total)
                    

def list_mthai_episodes(url,movie_name,movie_img):
    html = open_url(url)
    html = html.replace('\n','').replace('\t',' ') 
    
    episode = ''
    a = []    
    
    episodelink = re.compile('var sources_temp = (.+?);').findall(html)
    if len(episodelink)>0:
        for y in range(0, len(episodelink)):
            if len(episodelink[y])>0:
                episode = episodelink[y] 
                #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
                episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/').replace('sources:','"sources":').replace('file:','"file":').replace('label:','"label":')
                episode = '{"sources": '  + episode + '}'                
                json_data = json.loads(episode)
                for sources in json_data['sources']:
                    url = str(sources['file'])
                    title = movie_name + ' ('  + str(sources['label']) +'p)'
                    stype = ''
                    if len(url)>0:
                        temp = [url,title,movie_img,stype] 
                        a.append(temp)               
    else:    
        episodelink = re.compile('playlist: \[(.+?)\]').findall(html)
        
        
        for y in range(0, len(episodelink)):
            if len(episodelink[y])>0:
                episode = episodelink[y] 
        
            if episode.find('sources:') >=0:
                #episode[y] = episode[y].replace('[','').replace('{','').replace(')','').replace('\r','').replace('\t','').replace("file",'"file"').replace("label",'"label"').replace("type",'"type"').replace("provider",'"provider"').replace('bitrate','"bitrate"').replace("'",'\"').replace('\/','/')
                episode = episode.replace(')','').replace('\r','').replace('\t','').replace("'",'\"').replace('\/','/').replace('sources:','"sources":').replace('file:','"file":').replace('label:','"label":')
                episode = episode +']}'                
                json_data = json.loads(episode)
                for sources in json_data['sources']:
                    url = str(sources['file'])
                    title = movie_name + ' ('  + str(sources['label']) +'p)'
                    stype = ''
                    if len(url)>0:
                        temp = [url,title,movie_img,stype] 
                        a.append(temp)               
    
                             
    for url2, title, img, stype in a:
        title = title.replace('&#8211;',"-").replace('&#8217;',"'").replace('&amp;', '&').replace('&#038;', '&').replace('&#8230;', '...').replace('&#8216;', '\'').replace('&nbsp;', '') 
        if len(title)>0 and len(url2)>0:    
            addLink(title,url2,img)

        
############################################################################################

def open_url(url):
    if (url[:5]=='https') :
        #print ssl.OPENSSL_VERSION
        #httplib.HTTPSConnection.connect = connect_patched
        #ssl.wrap_socket = wrap_socket_patched
        #req = urllib2.Request(url=url)
        #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        #response = urllib2.urlopen(req)
        
        
        
        opener = urllib2.OpenerDirector()
        opener.add_handler(urllib2.HTTPSHandler())
        opener.add_handler(urllib2.HTTPDefaultErrorHandler())
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')]
        fetch_timeout = 100
        response = opener.open(url, None, fetch_timeout)
    else :   
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
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
    return ok

############################################################################################################
def _(string_id):
    if string_id in STRINGS:
        return get_string(STRINGS[string_id])
    else:
        #plugin.log.warning('Movie2Free error => String is missing: %s' % string_id)
        return string_id
    
def get_string(stringid):
    '''Returns the localized string from strings.xml for the given
    stringid.
    '''
    stringid = int(stringid)
#     if not hasattr(self, '_strings'):
#         _strings = {}
    if not stringid in _strings:
        _strings[stringid] = selfAddon.getLocalizedString(stringid).encode('utf-8')
    return _strings[stringid]

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

version = '2.0.2'
addon_id = 'plugin.video.movie2free'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = os.path.join(selfAddon.getAddonInfo('path'),'')
libfolder = os.path.join(addonfolder, 'lib', '')
artfolder = os.path.join(addonfolder, 'resources', 'img' , _('img_path'),'')
fanart = addonfolder + 'fanart.jpg'

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

print (sys.version)

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
    print "Search"
    search()
    
elif mode==7:
    print "Search next"
    list_search(url)

elif mode==8:
    print "TV Online"
    list_tvchannel(url)
    
elif mode==4:
    print ""
    list_episodes(url)
elif mode==9:
    #serie catagory
    serie_categories()
    
elif mode==10:
    #serie list
    serie_list_videos(url)
elif mode==11:
    #serie episodes
    serie_list_episodes(url,iconimage)
elif mode==12:
    #play serie
    print "play serie"
    serie_play(url,name,iconimage)
    
elif mode==13:
    #serie search
    print "serie search"
elif mode==14:
    #serie search next
    print "serie list search"
elif mode==21:
    #serie search next
    print "serie mthai"
    list_mthai_episodes(url,name,iconimage)
    
elif mode==100:
    #line do nothing
    print "line"    
elif mode==None and len(url)>0:
    print "Play video"
    #playVideo(handle,name,iconimage,url)
    
    #player(name,url,iconimage)
    #listar_temporadas(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
