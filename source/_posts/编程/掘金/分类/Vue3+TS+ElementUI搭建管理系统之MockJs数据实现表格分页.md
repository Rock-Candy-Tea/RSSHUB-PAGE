
---
title: 'Vue3+TS+ElementUI搭建管理系统之MockJs数据实现表格分页'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4704'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 01:31:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=4704'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">1、ts中安装mock</h5>
<pre><code class="copyable">npm install @types/mockjs -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">2、新建mock文件</h5>
<pre><code class="copyable">// src文件夹下
mock
├─index.ts
├─data
|  └table.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体接口table.ts文件</p>
<pre><code class="copyable">import &#123; Random &#125; from 'mockjs'
interface ListType &#123;
    id: number,
    name: string,
    code: number,
    province: string,
    date: string
&#125;
const dataList: Array<ListType> = [];
for (let i = 0; i < 100; i++) &#123;
    dataList.push(&#123;
        id: i,
        name: Random.cname(),
        code: Random.integer(100000, 800000),
        province: Random.province(),
        date: Random.date(),
    &#125;)
&#125;
export default &#123;
    getList: (params: any) => &#123;
        const info = JSON.parse(params.body);
        const [index, size, total] = [info.pageIndex - 1, info.pageSize, dataList.length]
        const len: any = total / size
        const totalPages: number = len - parseInt(len) >= 0 ? parseInt(len) + 1 : len
        const newDataList: Array<ListType> = dataList.slice(index * size, (index + 1) * size)
        return &#123;
            total: dataList.length,
            data: newDataList,
            totalPages: totalPages
        &#125;
    &#125;,
    update: (params: any) => &#123;
        const info = JSON.parse(params.body);
        dataList[info.index] = info.data
        return &#123;
            result: true,
            data: 'success'
        &#125;
    &#125;,
    delete: (params: any) => &#123;
        const info = JSON.parse(params.body);
        dataList.splice(info.index, 1);
        return &#123;
            result: true,
            data: 'success'
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.ts文件</p>
<pre><code class="copyable">import Mock from 'mockjs'
import table from './data/table'
​
Mock.mock('/table/getList', 'post', table.getList)
Mock.mock('/table/update', 'post', table.update)
Mock.mock('/table/delete', 'post', table.delete)
​
export default Mock
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">3、main.ts文件</h5>
<pre><code class="copyable">if (process.env.NODE_ENV === 'development') &#123;
    require ('./mock/index.ts')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">4、请求封装</h5>
<pre><code class="copyable">import request from '@/utils/request'
// 表格
export function getTableList(params: any): Promise<any> &#123;
    return request(&#123;
        url: '/table/getList',
        method: 'post',
        data: params
    &#125;)
&#125;
export function deleteTableList(params: any): Promise<any> &#123;
    return request(&#123;
        url: '/table/delete',
        method: 'post',
        data: params
    &#125;)
&#125;
export function updateTableList(params: any): Promise<any> &#123;
    return request(&#123;
        url: '/table/update',
        method: 'post',
        data: params
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">5、调用</h5>
<pre><code class="copyable">import &#123; getTableList, deleteTableList, updateTableList &#125; from "@/api/api";
getTableList() &#123;
  let params = &#123;
    pageIndex: this.pageIndex,
    pageSize: this.pageSize,
  &#125;;
  getTableList(params).then((res: any) => &#123;
    this.tableData = res.data;
    this.total = res.total;
  &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            