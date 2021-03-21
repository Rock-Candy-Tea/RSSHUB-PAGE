import requests
import re
from bs4 import BeautifulSoup
import time

baselink ='https://rsshub.zfe.space'
link_list = [
    {"source":"3DM - 新闻中心",
"link":"/3dm/news",
"categories":"游戏",
    },
    {"source":"a9vgNews 游戏新闻",
"link":"/a9vg/a9vg",
"categories":"游戏",
    },
    {"source":"4Gamers - 遊戲資訊",
"link":"/4gamers/category/352",
"categories":"游戏",
    },
    {"source":"GameRes 游资网",
"link":"/gameres/hot",
"categories":"游戏",
    },
    {"source":"Indienova 独立游戏",
"link":"/indienova/article",
"categories":"游戏",
    },
    {"source":"小黑盒 - 游戏新闻",
"link":"/xiaoheihe/news",
"categories":"游戏",
    },
    {"source":"触乐",
"link":"/chuapp/index/daily",
"categories":"游戏",
    },
    {"source":"二柄 APP",
"link":"/erbingapp/news",
"categories":"游戏",
    },
    {"source":"奶牛关 - 奶牛精选",
"link":"/cowlevel/element/1370",
"categories":"游戏",
    },
 {"source":"GNN.tw 游戏新闻",
"link":"/gnn/gnn",
"categories":"游戏",
    },
 {"source":"游戏动力",
"link":"/vgn",
"categories":"游戏",
    },
 {"source":"游戏时光 - 新闻",
"link":"/vgtime/news",
"categories":"游戏",
    },
{"source":"游研社 - 推荐游戏",
"link":"/yystv/category/recommend",
"categories":"游戏",
    },
{"source":"游讯网",
"link":"/yxdown/recommend",
"categories":"游戏",
    },
{"source":"豆瓣 - 电影",
"link":"/douban/movie/weekly",
"categories":"社交",
    },
{"source":"豆瓣 - 图书",
"link":"/douban/book/rank/fiction",
"categories":"社交",
    },
{"source":"刷屏",
"link":"/weseepro/newest",
"categories":"社交",
    },
{"source":"微博热搜",
"link":"/weibo/search/hot",
"categories":"社交",
    },
{"source":"知乎 - 日报",
"link":"/zhihu/daily",
"categories":"社交",
    },
{"source":"知乎 - 热榜",
"link":"/zhihu/hotlist",
"categories":"社交",
    },
{"source":"简书",
"link":"/jianshu/trending/weekly",
"categories":"社交",
    },
{"source":"bilibili - 资讯",
"link":"/bilibili/partion/203",
"categories":"社交",
    },
{"source":"005 - tv",
"link":"/005tv/zx/latest",
"categories":"二次元",
    },
{"source":"Hpoi - 手办维基",
"link":"/hpoi/info/all",
"categories":"二次元",
    },
{"source":"動畫瘋",
"link":"/anigamer/new_anime",
"categories":"二次元",
    },
{"source":"Bangumi",
"link":"/bangumi/calendar/today",
"categories":"二次元",
    },
{"source":"Anitama Channel",
"link":"/anitama",
"categories":"二次元",
    },
{"source":"Animen 动漫平台",
"link":"/animen/news/zx",
"categories":"二次元",
    },
{"source":"CFD",
"link":"/cfd/div_gbp",
"categories":"财经",
    },
{"source":"DT 财经",
"link":"/dtcj/datahero",
"categories":"财经",
    },
{"source":"finviz",
"link":"/finviz/news/AAPL",
"categories":"财经",
    },
{"source":"WEEX 华尔街见闻",
"link":"/weexcn/news/1",
"categories":"财经",
    },
{"source":"财联社",
"link":"/cls/telegraph",
"categories":"财经",
    },
{"source":"富途牛牛",
"link":"/futunn/highlights",
"categories":"财经",
    },
{"source":"金十数据",
"link":"/jinshi/index ",
"categories":"财经",
    },
{"source":"麦肯锡中国",
"link":"/mckinsey/autos",
"categories":"财经",
    },
{"source":"每经网",
"link":"https://rsshub.app/nbd/daily",
"categories":"财经",
    },
{"source":"淘股吧股票论坛",
"link":"/taoguba/index",
"categories":"财经",
    },
{"source":"证券时报网",
"link":"/stcn/news",
"categories":"财经",
    },
{"source":"中证网",
"link":"/cs/news/zzkx",
"categories":"财经",
    },
]

def get_data(link):
    try:
        r = requests.get(link, timeout=20)
        r.encoding = 'utf-8-sig'
        result = r.text

    except Exception as e:
        error_line = e.__traceback__.tb_lineno
        error_info = '第{error_line}行发生error为: {e}'.format(error_line=error_line, e=str(e))
        print(error_info)
        result = ''
    return result

def get_post(source,link,categories):
    result = get_data(baselink+link)
    soup = BeautifulSoup(result, 'html.parser')
    author = source
    for i in soup.find_all('item'):
        title = ''
        text = ''
        pubdate =''
        img =''
        for child in i.children:
            if (child.name == 'title'):
                title = child.string
            if (child.name == 'description'):
                text = child.string
                soup_item = BeautifulSoup(text, 'html.parser')
                if soup_item.find('img'):
                    img = soup_item.find('img')['src']
                else:
                    img = ''
            if (child.name == 'guid'):
                pass
            if (pubdate ==''):
                pubdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if (child.name == 'pubdate'):
                pubdate = child.string
            if pubdate =='' and (child.name == 'lastbuilddate'):
                pubdate = child.string
            title = re.sub(r'[:/\\?*“”<>|\[\]]', '_',title)


        try:
            with open('post/'+title.replace('\n','').replace('#','').replace('.','')+ '.md', mode='w', encoding='utf-8') as f:
                md_content = '''
---
title: {title}
categories: 
    - {categories}
    - {author}
author: {author}
comments: false
date: {date}
thumbnail: {img}
---
  
<div>   
{text}  
</div>
            '''
                md_content = md_content.format(title=title, categories=categories,author=author,date=pubdate,text=text,img=img)
                print('发布时间：', pubdate)
                print('标题：', title)
                print('描述：', '已获取内容')
                print('图片：', img)
                print('---------------------------')
                f.write(md_content)
                f.close()
        except:
            pass


for item in link_list:
    get_post(item['source'], item['link'], item['categories'])
