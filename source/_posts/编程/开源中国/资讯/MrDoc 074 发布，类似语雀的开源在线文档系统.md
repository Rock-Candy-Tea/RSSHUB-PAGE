
---
title: 'MrDoc 0.7.4 发布，类似语雀的开源在线文档系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
author: 开源中国
comments: false
date: Thu, 30 Dec 2021 11:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-52e0524eae217a33a79eafbdaa70e060cae.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MrDoc 是「州的先生」基于 Python 的 Django 框架开发并开源的在线文档系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff">其功能类似于</span><strong><span style="background-color:#ffffff">国内的语雀平台、看云平台，国外的 GitBook 平台。</span></strong></p> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">总而言之，<strong>你所写的一切都在你自己的掌控之中</strong>，不用担心哪家的产品停止服务了，不用担心收藏在哪里的内容被互联网政策清理掉了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">同时，移动端APP 也在开发中，预计 2022年初发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">根据觅思文档交流群里的反馈，很多朋友用来做<strong>个人私有云笔记、团队知识库、公司产品手册、小说网站</strong>等</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">今日，MrDoc 归版发布了 0.7.4 版本，本次版本发布带来了一大波的更新、优化和Bug修复，详细的更新内容如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[新增]接口对桌面客户端的支持；</li> 
 <li>[修复]文集导出解析文档图片导致导出失败的问题；</li> 
 <li>[修复]版本检测更新异常的问题；</li> 
 <li>[修复]@符号导致Markdown链接解析异常的问题；</li> 
 <li>[优化]取消框架层级的数据上传大小限制；</li> 
 <li>[优化]登录错误次数超过6次将锁定10分钟；</li> 
 <li>[优化]更新依赖库版本；</li> 
 <li>[优化]优化后台管理图片管理图片预览；</li> 
</ul> 
<p><strong>MrDoc官网：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://mrdoc.pro</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>源码地址：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/MrDoc</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://github.com/zmister2016/MrDoc</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>浏览器扩展：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/mrdoc-webclipper</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>桌面客户端：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>https://gitee.com/zmister/mrdoc-desktop</u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>示例站点：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><u>http://mrdoc.zmister.com/ </u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">测试账号：test1 测试密码：123456</p>
                                        </div>
                                      
</div>
            