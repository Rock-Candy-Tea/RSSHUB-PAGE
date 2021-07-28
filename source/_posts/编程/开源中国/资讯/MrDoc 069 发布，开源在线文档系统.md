
---
title: 'MrDoc 0.6.9 发布，开源在线文档系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-74fb6a85d8daddd9c32dbc1812d034f6eda.png'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 10:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-74fb6a85d8daddd9c32dbc1812d034f6eda.png'
---

<div>   
<div class="content">
                                                                                            <p>觅道文档 MrDoc 是州的先生基于 Python 的 Django 框架开发并开源的在线文档系统。</p> 
<p><span style="background-color:#ffffff">其功能类似于</span><strong><span style="background-color:#ffffff">国内的语雀平台、看云平台，国外的 GitBook 平台</span></strong><span style="background-color:#ffffff">，如果你在寻找<strong>可私有化部署的在线文档系统</strong>，那么觅道文档可以说是不二之选。</span></p> 
<p><img height="212" src="https://oscimg.oschina.net/oscnet/up-74fb6a85d8daddd9c32dbc1812d034f6eda.png" width="500" referrerpolicy="no-referrer"></p> 
<p>觅道文档以「文档」作为系统的主要承载形式，支持用 Markdown 和富文本进行<strong>「普通文档」</strong>的写作，支持类似 Excel 的在线表格用来<strong>「表格文档」</strong>的记录。</p> 
<p>同时以书籍形式的<strong>结构化文集</strong>作为文档的呈现形式，非常<strong>适合个人和小型团队作为私有化的文档、笔记和知识管理工具。</strong></p> 
<p><img height="238" src="https://oscimg.oschina.net/oscnet/up-8b40cec83a23cdb36d546ecc8bff7750872.png" width="500" referrerpolicy="no-referrer"></p> 
<p>除此之外，还通过原生 Chrome 浏览器扩展和接入「简悦」扩展，实现了网站内容剪藏，可以化身成为互联网内容收藏神器。</p> 
<p><img height="238" src="https://oscimg.oschina.net/oscnet/up-31b5b724b8aae53c1037d4c902606e01931.png" width="500" referrerpolicy="no-referrer"></p> 
<p>总而言之，<strong>你所写的一切都在你自己的掌控之中</strong>，不用担心哪家的产品停止服务了，不用担心收藏在哪里的内容被互联网政策清理掉了。</p> 
<p>根据觅道文档交流群里的反馈，很多朋友用来做<strong>个人私有云笔记、团队知识库、公司产品手册、小说网站</strong>等</p> 
<h2>更新内容</h2> 
<p>近日，觅道文档归版发布了 0.6.9 版本，本次版本发布带来了一大波的更新、优化和Bug修复，详细的更新内容如下：</p> 
<ul> 
 <li> <p>[新增]后台管理中心的<strong>图片管理和附件管理</strong>功能。</p> </li> 
 <li> <p>[新增]站点搜索中文档搜索支持<strong>「全文搜索」和「匹配搜索」</strong>功能和切换开关。</p> </li> 
 <li> <p>[新增]后台文档管理<strong>文档历史记录页面和接口。</strong></p> </li> 
 <li> <p>[修复]<strong>vditor编辑器粘贴多图片</strong>文本时图片只有一张图的问题。</p> </li> 
 <li> <p>[修复]<strong>找回密码邮件发送失败</strong>的问题。</p> </li> 
 <li> <p>[修复]后台管理用户管理<strong>用户无法搜索</strong>的问题。</p> </li> 
 <li> <p>[修复]<strong>文档访问权限可绕过</strong>的问题。</p> </li> 
 <li> <p>[修复]MySQL数据库下<strong>文档删除失败</strong>的问题。</p> </li> 
 <li> <p>[优化]个人中心我协作的文集页面及功能。</p> </li> 
 <li> <p>[优化]后台<strong>邮件服务器配置</strong>逻辑和页面展示。</p> </li> 
 <li> <p>[优化]文档<strong>发布和修改的异常</strong>判断和处理。</p> </li> 
 <li> <p>[优化]首页移动端控制栏样式。</p> </li> 
 <li> <p>[优化]文集内<strong>搜索文档</strong>。</p> </li> 
 <li> <p>[优化]后台文档管理文档编辑模式显示。</p> </li> 
 <li> <p>[优化]后台图片管理<strong>图片预览</strong>功能。</p> </li> 
 <li> <p>[优化]文档历史记录对比接口。</p> </li> 
 <li> <p>[优化]403页面。</p> </li> 
 <li> <p>[优化]图片上传格式处理。</p> </li> 
</ul> 
<h2 style="text-align:justify"><strong>5步快速更新教程</strong></h2> 
<p style="text-align:justify">1、拉取项目代码：</p> 
<pre style="text-align:justify"><code>git pull</code></pre> 
<p style="text-align:justify">2、更新依赖库：</p> 
<pre style="text-align:justify"><code>pip install -r requirements.txt</code></pre> 
<p style="text-align:justify">3、<span style="background-color:#ffffff">生成数据库迁移：</span></p> 
<pre style="text-align:justify"><code>python manage.py makemigrations</code></pre> 
<p style="text-align:justify">4、<span style="background-color:#ffffff">执行数据库迁移：</span></p> 
<pre style="text-align:justify"><code>python manage.py migrate</code></pre> 
<p style="text-align:justify">5、重启应用</p> 
<h2 style="text-align:justify"><strong>5步极速安装体验</strong></h2> 
<pre style="text-align:justify"><code># 使用 Git 工具克隆觅道文档源码</code><code>git clone https://gitee.com/zmister/MrDoc/</code><code>​</code><code># 安装依赖模块</code><code>pip install -r requirements.txt</code><code>​</code><code># 初始化数据库</code><code>python manage.py migrate</code><code>​</code><code># 创建管理员用户</code><code>python manage.py createsuperuser</code><code>​</code><code># 运行测试服务器</code><code>python manage.py runserver</code></pre> 
<p style="text-align:justify"><strong>源码地址：</strong></p> 
<p style="text-align:justify"><u>https://gitee.com/zmister/MrDoc</u></p> 
<p style="text-align:justify"><u>https://github.com/zmister2016/MrDoc</u></p> 
<p style="text-align:justify"><strong>示例站点：</strong></p> 
<p style="text-align:justify"><u>http://mrdoc.zmister.com/ </u></p> 
<p style="text-align:justify">测试账号：test1 测试密码：123456</p>
                                        </div>
                                      
</div>
            