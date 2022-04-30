
---
title: 'MrDoc 0.7.8 发布，类似语雀、飞书的开源在线文档系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 10:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MrDoc 是基于 Python 的 Django 框架开发并开源的在线文档系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">其功能类似于</span><strong><span style="background-color:#ffffff">国内的语雀平台、看云平台和飞书文档，国外的 GitBook 平台。</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">如果你在寻找<strong>可私有化部署的在线文档系统</strong>，那么 MrDoc 可以说是不二之选。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MrDoc 以「文档」作为系统的主要承载形式，支持用 Markdown 和富文本进行<strong>「普通文档」</strong>的写作，支持类似 Excel 的在线表格用来<strong>「表格文档」</strong>的记录。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">同时以书籍形式的<strong>结构化文集</strong>作为文档的呈现形式，非常<strong>适合个人和小型团队作为私有化的文档、笔记和知识管理工具。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-031f753fd43bb3cbeedfc7187e13ad3eb02.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">全平台多终端支持</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">浏览器扩展</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MrDoc 通过原生 Chrome 浏览器扩展（开源地址为：https://gitee.com/zmister/mrdoc-webclipper）和接入「简悦」扩展，实现了网站内容剪藏，可以化身成为互联网内容收藏神器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="238" src="https://oscimg.oschina.net/oscnet/up-31b5b724b8aae53c1037d4c902606e01931.png" width="500" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">桌面客户端</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MrDoc 还提供了基于 Electron 开发的桌面客户端，跨平台支持Windows、Linux和macOS。<br> <img alt height="425" src="https://oscimg.oschina.net/oscnet/up-7bedfe0fdc5552eb8b737bb6ee2103c800f.png" width="800" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">移动端APP</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">移动端APP 1.0版本也已经发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">总而言之，<strong>你所写的一切都在你自己的掌控之中</strong>，不用担心哪家的产品停止服务了，不用担心收藏在互联网平台上的内容被各种原因清理掉了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">根据MrDoc交流QQ群里的反馈，很多朋友用来做<strong>个人私有云笔记、团队知识库、公司产品手册、组织规章制度和办事指南</strong>等</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">今日（2022年4月30日），MrDoc 归版发布了<span style="color:#c0392b"><strong> 0.7.8 </strong></span>版本，本次版本发布带来了一大波的更新、优化和Bug修复，详细的更新内容如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[新增]个人中心文档管理「已删除文档」数量显示和跳转；</li> 
 <li>[修复]管理员导出文集MD压缩包提示「文集不存在」的问题；</li> 
 <li>[修复]部分指定文集新建文档时存在文集目录重复加载的问题；</li> 
 <li>[修复]文集页面「最新文档」选项卡中富文本文档摘要显示为None的问题；</li> 
 <li>[修复]管理员批量删除文档时部分文档删除不了的问题；</li> 
 <li>[修复]个人中心文档数量不匹配的问题；</li> 
 <li>[修复]首页新建文集的样式问题<a href="https://gitee.com/zmister/MrDoc/issues/I50XRV" target="_blank">#I50XRV</a>；</li> 
 <li>[优化]注册页面用户名输入框和用户名错误提示；</li> 
 <li>[优化]个人中心文集成员管理中用户名的显示；</li> 
 <li>[优化]用户token相关接口以适配桌面客户端0.1.9；</li> 
 <li>[优化]首页底部样式；</li> 
 <li>[优化]调整uwsgi超时时间配置；</li> 
 <li>[优化]Markdown压缩包文集导入中文处理；</li> 
 <li>[优化]系统配置默认自带移动端APP所需的跨域白名单；</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>MrDoc官网：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://mrdoc.pro</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>源码地址：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/MrDoc</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://github.com/zmister2016/MrDoc</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>浏览器扩展：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/mrdoc-webclipper</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>桌面客户端：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/mrdoc-desktop-release</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>移动APP：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/mrdoc-app-release</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>示例站点：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>http://mrdoc.zmister.com/ </u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">测试账号：test1 测试密码：123456</p> 
<p> </p>
                                        </div>
                                      
</div>
            