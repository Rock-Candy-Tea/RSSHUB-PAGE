
---
title: 'MrDoc 0.7.0 发布，开源在线文档系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 08:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">觅思文档 MrDoc 是州的先生基于 Python 的 Django 框架开发并开源的在线文档系统。</p> 
<p style="text-align:left"><span style="background-color:#ffffff">其功能类似于</span><strong><span style="background-color:#ffffff">国内的语雀平台、看云平台，国外的 GitBook 平台。</span></strong></p> 
<p style="text-align:left"><span style="background-color:#ffffff">如果你在寻找<strong>可私有化部署的在线文档系统</strong>，那么觅道文档可以说是不二之选。</span></p> 
<p style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">觅思文档以「文档」作为系统的主要承载形式，支持用 Markdown 和富文本进行<strong>「普通文档」</strong>的写作，支持类似 Excel 的在线表格用来<strong>「表格文档」</strong>的记录。</p> 
<p style="text-align:left">同时以书籍形式的<strong>结构化文集</strong>作为文档的呈现形式，非常<strong>适合个人和小型团队作为私有化的文档、笔记和知识管理工具。</strong></p> 
<p style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-031f753fd43bb3cbeedfc7187e13ad3eb02.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">除此之外，还通过原生 Chrome 浏览器扩展和接入「简悦」扩展，实现了网站内容剪藏，可以化身成为互联网内容收藏神器。</p> 
<p style="text-align:left"><img height="238" src="https://oscimg.oschina.net/oscnet/up-31b5b724b8aae53c1037d4c902606e01931.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">总而言之，<strong>你所写的一切都在你自己的掌控之中</strong>，不用担心哪家的产品停止服务了，不用担心收藏在哪里的内容被互联网政策清理掉了。</p> 
<p style="text-align:left">根据觅思文档交流群里的反馈，很多朋友用来做<strong>个人私有云笔记、团队知识库、公司产品手册、小说网站</strong>等</p> 
<h2 style="text-align:left">更新内容</h2> 
<p style="text-align:left">今日，觅思文档归版发布了 0.6.9 版本，本次版本发布带来了一大波的更新、优化和Bug修复，详细的更新内容如下：</p> 
<ul> 
 <li>[新增]修改文档页面快捷键（Ctrl+S）保存;</li> 
 <li>[新增]文集大纲广告位4；</li> 
 <li>[修复]Editor.md编辑器标题链接不显示的问题；</li> 
 <li>[修复]Vditor编辑器文档目录显示问题；</li> 
 <li>[优化]修改文档页面「查看文档」功能；</li> 
 <li>[优化]文档浏览页面「下载文档」样式；</li> 
 <li>[优化]站内搜索logo；</li> 
 <li>[优化]启用新的产品中文名称：觅思文档；</li> 
 <li>[优化]文集列表首页底部样式；</li> 
 <li>[优化]项目配置读取逻辑；</li> 
</ul> 
<h2 style="text-align:justify"><strong>5步快速更新教程</strong></h2> 
<p style="text-align:justify">1、拉取项目代码：</p> 
<pre style="text-align:justify"><code><span style="color:#6f42c1">git</span> <span style="color:#032f62">pull</span></code></pre> 
<p style="text-align:justify">2、更新依赖库：</p> 
<pre style="text-align:justify"><code><span style="color:#6f42c1">pip</span> <span style="color:#032f62">install -r requirements.txt</span></code></pre> 
<p style="text-align:justify">3、<span style="background-color:#ffffff">生成数据库迁移：</span></p> 
<pre style="text-align:justify"><code><span style="color:#6f42c1">python</span> <span style="color:#032f62">manage.py makemigrations</span></code></pre> 
<p style="text-align:justify">4、<span style="background-color:#ffffff">执行数据库迁移：</span></p> 
<pre style="text-align:justify"><code><span style="color:#6f42c1">python</span> <span style="color:#032f62">manage.py migrate</span></code></pre> 
<p style="text-align:justify">5、重启应用</p> 
<h2 style="text-align:justify"><strong>5步极速安装体验</strong></h2> 
<pre style="text-align:justify"><code><span style="color:#6a737d">#</span> 使用 Git 工具克隆觅思文档源码</code><code>git clone https://gitee.com/zmister/MrDoc/</code><code>​</code><code><span style="color:#6a737d"># 安装依赖模块</span></code><code><span style="color:#6a737d">pip install -r requirements.txt</span></code><code><span style="color:#6a737d">​</span></code><code><span style="color:#6a737d"># 初始化数据库</span></code><code><span style="color:#6a737d">python manage.py migrate</span></code><code><span style="color:#6a737d">​</span></code><code><span style="color:#6a737d"># 创建管理员用户</span></code><code><span style="color:#6a737d">python manage.py createsuperuser</span></code><code><span style="color:#6a737d">​</span></code><code><span style="color:#6a737d"># 运行测试服务器</span></code><code><span style="color:#6a737d">python manage.py runserver</span></code></pre> 
<p style="text-align:justify"><strong>源码地址：</strong></p> 
<p style="text-align:justify"><u>https://gitee.com/zmister/MrDoc</u></p> 
<p style="text-align:justify"><u>https://github.com/zmister2016/MrDoc</u></p> 
<p style="text-align:justify"><strong>示例站点：</strong></p> 
<p style="text-align:justify"><u>http://mrdoc.zmister.com/ </u></p> 
<p style="text-align:justify">测试账号：test1 测试密码：123456</p>
                                        </div>
                                      
</div>
            