import queue
import threading
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import yaml


def load_config(path):
    f = open(path, 'r', encoding='utf-8')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    return ymllist


def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)


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


def build_md():
    source_list = []
    list_name = []
    path = 'temple/'  # 文件夹路径
    listdir(path, list_name)
    print(list_name)
    for i in list_name:
        with open(i, mode='r', encoding='utf-8') as f:
            sorce_parent = ''
            sorce_child = ''
            categories = ''
            for line in f.readlines():
                if line[0:3].count('#') == 1:
                    print(line.replace('#', '').strip())
                    categories = line.replace('#', '').strip()
                    try:
                        os.makedirs('source/_posts/' + categories)
                    except Exception as e:
                        print('已存在目录', categories)
                    sorce_parent = ''
                    sorce_child = ''
                if line[0:3].count('#') == 2:
                    print(line.replace('#', '').strip())
                    sorce_parent = line.replace('#', '').strip()
                    try:
                        os.makedirs('source/_posts/' + categories + '/' + sorce_parent)
                    except Exception as e:
                        print('已存在目录', sorce_parent)
                if line[0:3].count('#') == 3:
                    print(line.replace('#', '').strip())
                    sorce_child = line.replace('#', '').strip()
                    try:
                        os.makedirs('source/_posts/' + categories + '/' + sorce_parent + '/' + sorce_child)
                    except Exception as e:
                        print('已存在目录', sorce_child)
                if '<Route ' in line:
                    try:
                        text = BeautifulSoup(line, 'html.parser')
                        print(text.route['example'])
                        item = {"source_child": sorce_child,
                                "source_parent": sorce_parent,
                                "link": text.route['example'],
                                "categories": categories,
                                }
                        source_list.append(item)
                    except:
                        line = line + '>'
                        text = BeautifulSoup(line, 'html.parser')
                        print(text.route['example'])
                        item = {"source_child": sorce_child,
                                "source_parent": sorce_parent,
                                "link": text.route['example'],
                                "categories": categories,
                                }
                        source_list.append(item)

    list_slect = []
    config_list = load_config('temple/temple_config.yml')
    for item in source_list:
        if item['link'] in config_list['slect']:
            list_slect.append(item)
    user_config_list = load_config('user_config.yml')
    for item in user_config_list['diy']:
        list_slect.append(item)

    print(list_slect)
    print(len(list_slect))
    return list_slect


def get_data(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }
        r = requests.get(link, headers=headers, timeout=20)
        r.encoding = 'utf-8-sig'
        result = r.text

    except Exception as e:
        error_line = e.__traceback__.tb_lineno
        error_info = '第{error_line}行发生error为: {e}'.format(error_line=error_line, e=str(e))
        print(error_info)
        result = ''
    return result


def get_post(source, result, categories):
    soup = BeautifulSoup(result, 'html.parser')
    author_name = source['source_parent']
    author_child = source['source_child']
    for i in soup.find_all('item')[0:15]:
        title = ''
        text = ''
        pubdate = ''
        img = ''
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
            if (pubdate == ''):
                pubdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if (child.name == 'pubdate'):
                pubdate = child.string
            if pubdate == '' and (child.name == 'lastbuilddate'):
                pubdate = child.string
            title = re.sub(r'[:/\\?*“”<>|\[\]]', '_', title)

        try:
            with open('source/_posts/' + categories + '/' + author_name + '/' + author_child + '/' + title.replace('\n', '').replace('#', '').replace('.',
                                                                                                                   '') + '.md',
                      mode='w',
                      encoding='utf-8') as f:
                md_content = '''
---
title: {title}
categories: 
 - {categories}
 - {author_name}
 - {author_child}
headimg: '{img}'
author: {author_name}
comments: false
date: {date}
thumbnail: '{img}'
---

<div>   
{text}  
</div>
            '''
                if "'" in title:
                    title = '"' + title + '"'
                else:
                    title = "'" + title + "'"
                author_child = '| '+ author_child
                md_content = md_content.format(title=title, categories=categories, author_child=author_child,author_name=author_name, date=pubdate,
                                               text=text, img=img)
                md_content = md_content.replace('{', '&#123;')
                md_content = md_content.replace('}', '&#125;')
                print('发布时间：', pubdate)
                print('标题：', title)
                print('描述：', '已获取内容')
                print('图片：', img)
                print('---------------------------')
                f.write(md_content)
                f.close()
        except:
            pass


# 解析线程类
class Parse(threading.Thread):
    def __init__(self, number, data_list, req_thread):
        super(Parse, self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_thread = req_thread
        self.is_parse = True  # 判断是否从数据队列里提取数据

    def run(self):
        print('启动%d号解析线程' % self.number)
        while True:
            # 如何判断解析线程的结束条件
            for t in self.req_thread:
                if t.is_alive():
                    break
            else:
                if self.data_list.qsize() == 0:
                    self.is_parse = False

            if self.is_parse:  # 解析
                try:
                    data = self.data_list.get(timeout=3)
                except Exception as e:
                    data = None
                if data is not None:
                    self.parse(data)
            else:
                break
        print('退出%d号解析线程' % self.number)

    # 页面解析函数
    def parse(self, data):
        get_post(data[0], data[1], data[0]['categories'])


# 采集线程类
class Crawl(threading.Thread):
    def __init__(self, number, req_list, data_list):
        super(Crawl, self).__init__()
        self.number = number
        self.req_list = req_list
        self.data_list = data_list

    def run(self):
        print('启动采集线程%d号' % self.number)
        while self.req_list.qsize() > 0:
            url = self.req_list.get()
            requests_url = 'https://rsshub.zfe.space' + url['link']
            print('%d号线程采集：%s' % (self.number, url))
            # time.sleep(random.randint(1, 3))
            response = get_data(requests_url)
            self.data_list.put([url, response])  # 向数据队列里追加


def main():
    concurrent = 10
    conparse = 10
    try:
        os.makedirs('sourc')
    except Exception as e:
        print('已存在post目录')
    try:
        os.makedirs('source/_posts')
    except Exception as e:
        print('已存在post目录')
    # 获取rss列表
    link_list = build_md()

    # 生成请求队列
    req_list = queue.Queue()
    # 生成数据队列
    data_list = queue.Queue()

    # 填充请求数据
    # for i in range(1, 13 + 1):
    #     base_url = 'https://www.baidu.com/{}.html'.format(i)
    #     req_list.put(base_url)
    for item in link_list:
        req_list.put(item)

    # 生成N个采集线程
    req_thread = []
    for i in range(concurrent):
        t = Crawl(i + 1, req_list, data_list)  # 创造线程
        t.start()
        req_thread.append(t)

    # 生成N个解析线程
    parse_thread = []
    for i in range(conparse):
        t = Parse(i + 1, data_list, req_thread)  # 创造解析线程
        t.start()
        parse_thread.append(t)

    for t in req_thread:
        t.join()
    for t in parse_thread:
        t.join()


if __name__ == '__main__':
    main()
