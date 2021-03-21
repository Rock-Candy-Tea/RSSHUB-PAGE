# -*- coding: UTF-8 -*-
import requests


default_link = 'https://www.mxnzp.com/api/news/list?'
key = '&app_id=tkilvmkqykbpjode&app_secret=Vk0xY0hOVTN5eTh5ZVo0SzBNQ0Z2UT09'
categories_list = {
    '游戏':'515',
    '军事':'511',
    '财经':'509',
    '科技':'510',
    '娱乐':'520',
}

def get_data(link):
    try:
        r = requests.get(link, timeout=15)
        r.encoding = 'utf-8-sig'
        result = r.json()
        return result
    except:
        print('请求超过15s。')

def get_post_list(type_num):
    try:
        num = 0
        break_flag = False
        result_list = []
        for item in range(100):
            if bool(1-break_flag):
                url = default_link + 'typeId=' + type_num + '&page=' + str(num+1) + key
                num += 1
                print(num)
                try:
                    result = get_data(url)
                    for result_item in result['data']:
                        if result_item not in result_list:
                            result_list.append(result_item)
                        elif result_item == result_list[0]:
                            print('重复开头:', result_item)
                            break_flag = True
                            break
                        else:
                            pass
                        # print('重复了:',result_item)
                except Exception as e:
                    error_line = e.__traceback__.tb_lineno
                    error_info = '第{error_line}行发生error为: {e}'.format(error_line=error_line, e=str(e))
                    print(error_info)
                    print('获取不到新链接，获取结束')
                    break_flag = True

            else:
                print('获取到重复文章，获取结束')
                break
        return result_list
    except Exception as e:
        error_line = e.__traceback__.tb_lineno
        error_info = '第{error_line}行发生error为: {e}'.format(error_line=error_line, e=str(e))
        print(error_info)

def get_all_categories_list_post(categories_list):
    for item in categories_list.values():
        result = get_post_list(item)
        print(len(result))


get_all_categories_list_post(categories_list)




