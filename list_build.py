import requests
import re
from bs4 import BeautifulSoup
import os

error=[]
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
            sorce_base = ''
            sorce_all = ''
            categories = ''
            for line in f.readlines():
                if line[0:3].count('#') == 1:
                    print(line.replace('#', '').strip())
                    categories = line.replace('#', '').strip()
                    sorce_base = ''
                    sorce_all = ''
                if line[0:3].count('#') == 2:
                    print(line.replace('#', '').strip())
                    sorce_base = line.replace('#', '').strip()
                if line[0:3].count('#') == 3:
                    print(line.replace('#', '').strip())
                    sorce_all = sorce_base + ' - ' + line.replace('#', '').strip()
                if '<Route ' in line:
                    try:
                        text = BeautifulSoup(line, 'html.parser')
                        print(text.route['example'])
                        item = {"source": sorce_all,
                            "link": text.route['example'],
                            "categories": categories,
                            }
                        source_list.append(item)
                    except:
                        line = line + '>'
                        text = BeautifulSoup(line, 'html.parser')
                        print(text.route['example'])
                        item = {"source": sorce_all,
                                "link": text.route['example'],
                                "categories": categories,
                                }
                        source_list.append(item)
                        error.append(item)

    print(source_list)
    print(len(source_list))

build_md()
print(error)