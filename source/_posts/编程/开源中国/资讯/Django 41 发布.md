
---
title: 'Django 4.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6452'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6452'
---

<div>   
<div class="content">
                                                                                            <p>Django 4.1 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fweblog%2F2022%2Faug%2F03%2Fdjango-41-released%2F" target="_blank">发布</a>，<span style="background-color:#ffffff; color:#0c3c26">支持 Python 3.8、3.9 和 3.10。</span>一些亮点更新内容如下：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F%23asynchronous-orm-interface" target="_blank">ORM</a> 的异步接口，以及在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F%23asynchronous-handlers-for-class-based-views" target="_blank">基于类的视图上</a>定义异步处理程序的能力。</li> 
</ul> 
<pre><strong>import</strong> <strong>asyncio</strong>
<strong>from</strong> <strong>django.http</strong> <strong>import</strong> <span>HttpResponse</span>
<strong>from</strong> <strong>django.views</strong> <strong>import</strong> <span>View</span>

<strong>class</strong> <strong>AsyncView</strong><span>(</span><span>View</span><span>):</span>
    <strong>async</strong> <strong>def</strong> <span style="color:#0000ff">get</span><span>(</span><span style="color:#008000">self</span><span>,</span> <span>request</span><span>,</span> <span style="color:#666666">*</span><span>args</span><span>,</span> <span style="color:#666666">**</span><span>kwargs</span><span>):</span>
        <em># Perform view logic using await.</em>
        <strong>await</strong> <span>asyncio</span><span style="color:#666666">.</span><span>sleep</span><span>(</span><span style="color:#666666">1</span><span>)</span>
        <strong>return</strong> <span>HttpResponse</span><span>(</span><span style="color:#ba2121">"Hello async world!"</span><span>)</span></pre> 
<ul> 
 <li>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F%23validation-of-constraints" target="_blank">模型验证中使用 ORM 定义的数据库约束</a>。</li> 
 <li>更好的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F%23form-rendering-accessibility" target="_blank">表单渲染可访问性</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F%23forms" target="_blank">输出样式自定义</a>。</li> 
</ul> 
<p><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fdownload%2F" target="_blank">可从下载页面</a>或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.python.org%2Fpypi%2FDjango%2F4.1" target="_blank">Python Package Index</a> 获取 Django 4.1 。此版本使用的 PGP key ID 是 Carlton Gibson：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcarltongibson.gpg" target="_blank">E17DF5C82B4F9D00</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span style="color:#000000">公告指出，随着 Django 4.1 的发布，Django 4.0 已经到了主流支持的尽头；最后的一个小错误修复版本 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fstable%2Freleases%2F4.0.7%2F" target="_blank"><span style="color:#000000">4.0.7</span></a><span style="color:#000000"> 也已发布。在 2023 年 4 月之前，Django 4.0 都将提供安全和数据丢失修复支持。官方鼓励所有用户在此之前升级，以继续接收安全问题修复。</span></p> 
<p>参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fdownload%2F%23supported-versions" target="_blank">下载页面</a>以获取支持的版本表和未来的发布时间表。</p> 
<p>更多详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.1%2Freleases%2F4.1%2F" target="_blank">release notes</a><span style="color:#0c3c26">。</span></p>
                                        </div>
                                      
</div>
            