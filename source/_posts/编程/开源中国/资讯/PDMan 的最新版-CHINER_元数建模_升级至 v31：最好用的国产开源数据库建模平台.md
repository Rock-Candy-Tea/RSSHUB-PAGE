
---
title: 'PDMan 的最新版-CHINER_元数建模_升级至 v3.1：最好用的国产开源数据库建模平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e3794a2a705fffff946cc52332cd5249b56.png'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 09:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e3794a2a705fffff946cc52332cd5249b56.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>chiner,发音:[kaɪˈnər]</p> 
</blockquote> 
<h1 style="text-align:left">1 背景说明</h1> 
<p style="text-align:left">几经磨练，历时三年，一点一滴积累，于大约20天之前(7月17日），我们发布了CHINER元数建模的第一个版本:CHINER[元数建模]v3.0。发布于：<a href="https://my.oschina.net/skymozn/blog/5134881">PDMan升级换代至->CHINER[元数建模]v3.0：最好用的国产开源数据库建模平台</a></p> 
<p style="text-align:left">通过近三周的使用，一大批忠实用户提供了非常多有用的建议，我们评估后，根据实际情况，采纳了一批建议，并且修复了一大批缺陷。先后发布了两个修复版本。</p> 
<p style="text-align:left">本次更新升级至3.1，除了修复缺陷外，我们还增加了非常多实用的功能，大致如下：</p> 
<h1 style="text-align:left">2 升级内容清单</h1> 
<hr> 
<ol> 
 <li>关系图中的节点支持ctrl+c/v复制</li> 
 <li>修复左侧菜单拖动和展开收起图标在某些场景下需要滚动才可见的问题</li> 
 <li>数据库导入时已选择区支持多选移除和多选设置分组</li> 
 <li>修复默认word模板数据字典显示错误的问题</li> 
 <li>修复模板库中模板多个空行的问题</li> 
 <li>修复关系图保存后颜色消失的问题</li> 
 <li>新增自动保存功能以及自动保存设置</li> 
 <li>优化代码生成界面体验，优化性能等</li> 
 <li>概念模型设计关系图时，矩形和圆角矩形内容支持Markdown格式</li> 
 <li>新建视图时选择数据表支持搜索</li> 
 <li>关系图支持小地图</li> 
 <li>首页增加用户手册</li> 
 <li>程序代码模板增加C#</li> 
 <li>数据库增加加国产DM(达梦)数据库支持（生成DDL以及逆向导入）</li> 
 <li>解决表数量过多（超过200张），导出WORD出错问题</li> 
</ol> 
<hr> 
<h1 style="text-align:left">3 典型升级内容介绍</h1> 
<p style="text-align:left">针对其中的典型功能，我们作简要介绍，内容如下：</p> 
<h2 style="text-align:left">3.1 关系图数据表复制</h2> 
<p style="text-align:left">在关系图上就地复制数据表，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e3794a2a705fffff946cc52332cd5249b56.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.2 自动保存</h2> 
<p style="text-align:left">系统增加自动保存功能，通过系统设置自动保存时间，实现自动保存，解决部分用户忘记手动保存的问题，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-f747e92f667e6e701b4d967c0cf87b47844.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.3 形状内容支持Markdown</h2> 
<p style="text-align:left">通过拖动形状至关系图，然后建立形状和形状的关联，最后在形状内填写业务信息，完成业务对象的高阶设计，但是单纯的单行文字在表达业务对象时，显得不足，因此我们引入Markdown，支持更多种形式的表达，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-6c61f2f5a1cfc0f6e58a4c20fc234b551e4.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">形状的编辑状态如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-62c1950305e653141ee2a7dd9892f96a745.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.4 关系图小地图</h2> 
<p style="text-align:left">通过ctrl/Command+M打开或关闭小地图，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-26293972752baee2766f0df3ed7a680f3f0.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">有小地图的设计界面：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-56b43d7e1f1f1a010cf21575065631fd2e3.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.5 首页链接用户手册</h2> 
<p style="text-align:left">我们完成了元数建模的用户操作手册，并且导入至语雀，系统首页提供查看链接，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-967f596e0b25b72d921663c3503fd0dbd1b.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">语雀查看地址：(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fchiner%2Fdocs%2Fmanual" target="_blank">https://www.yuque.com/chiner/docs/manual</a>)</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-327f80b53c2a0f12dd4ac19c53dd4dd84c8.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.6 支持国产达梦数据库</h2> 
<p style="text-align:left">随着国产数据库的崛起，越来越多的用户开始使用国产数据库，我们首先支持了国产达梦数据库（DM8版本），支持数据库的DDL，逆向解析等。在将来，我们会逐步增加其他国产数据库的支持。 达梦数据库支持，DDL如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-2f84af8690672a06bfd4d6665609f9b9726.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">逆向解析以及数据库驱动已内置达梦8，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-4b68b0fdcc7711d889cb1d19770d3cb2e38.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.7 代码模板增加C#支持</h2> 
<p style="text-align:left">我们还增加了C#的Bean代码模板，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-b583fd407b3d0e0e901fbab72c5152df14e.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">生成的代码，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-36184243b701ba7796cad06f543aaf4295d.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">3.8 字段UI建议</h2> 
<p style="text-align:left">有用户提出，我们的表结构文件可以被解析后，生成部分前端界面代码，因此，我们将PDMan中的UI建议部分加上了，而且用户可以自己设置自己的类型，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-ff401c7439e01fe600d4156a6b1dab9c3fb.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">数据表字段设置UI建议，如下图：</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a959f07f6234346c5d354abbe8650c88b66.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">4 下载以及后续升级说明</h1> 
<p style="text-align:left">我们将长期维护CHINER元数建模的升级，并及时采纳合理的用户建议。</p> 
<p style="text-align:left">下载点位于Gitee的发布版，<a href="https://gitee.com/robergroup/chiner/releases">下载链接</a></p>
                                        </div>
                                      
</div>
            