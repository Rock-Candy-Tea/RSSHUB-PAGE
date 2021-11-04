
---
title: 'BookStack v2.11 发布，简洁的在线文档管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.sitestack.cn/projects/help/202111/16b3bf0202d90ce8.png'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 07:54:00 GMT
thumbnail: 'https://static.sitestack.cn/projects/help/202111/16b3bf0202d90ce8.png'
---

<div>   
<div class="content">
                                                                                            <p>BookStack，基于 Mindoc、使用 Go 语言的 Beego 框架开发的功能类似 GitBook 和看云的在线文档管理系统，拥有简洁美观的页面布局，实现了文档采集、导入、电子书生成以及版本控制等强大的文档功能，并推出了配套的开源微信小程序 <a href="https://gitee.com/truthhun/BookChat">BookChat</a> 和使用 <code>uni-app</code>开发的开源手机 APP <a href="https://gitee.com/truthhun/BookChatApp">BookChatApp</a>。</p> 
<h2>升级日志</h2> 
<p>1. 支持自定义内容阅读页右上角导航栏链接。</p> 
<p>操作方式：在书籍设置页面的<code>导航栏</code> 根据提示添加相应链接，保存后，即可在书籍阅读页面右上角显示。</p> 
<p><img alt src="https://static.sitestack.cn/projects/help/202111/16b3bf0202d90ce8.png" referrerpolicy="no-referrer"></p> 
<hr> 
<p><img alt src="https://static.sitestack.cn/projects/help/202111/16b3bf1ba2159058.png" referrerpolicy="no-referrer"></p> 
<p>2. 在个人书籍列表页，支持<code>拷贝书籍</code>（适用于书籍版本迭代发布）；支持生成电子书的进度状态显示。 <img alt src="https://static.sitestack.cn/projects/help/202111/16b3bf6434c9cd62.png" referrerpolicy="no-referrer"></p> 
<p>3. 内容阅读页支持将当前内容打印为PDF</p> 
<p>4. 修改文档章节标识时，联动修改书籍内所有链接到该章节的内链。</p> 
<p>5. 在个人书籍列表页，支持个人书籍简单检索，特别是在用户创建了比较多书籍项目的时候特别有用。 <img alt src="https://static.sitestack.cn/projects/help/202111/16b3bfb8415ea329.png" referrerpolicy="no-referrer"></p> 
<p>6. 支持设置默认首页，您可以将<code>发现页</code>、<code>分类页</code>、<code>搜索页</code>或者外链等任意页面设置为首页 <img alt src="https://static.sitestack.cn/projects/help/202111/16b3bfda8558b23e.png" referrerpolicy="no-referrer"></p> 
<p>7. 优化管理后台的配置管理功能(见上图)，拆分为 <code>基础</code>、<code>界面</code>、<code>用户</code>、<code>搜索</code>、<code>内容</code>、<code>运营</code>、<code>APP/小程序</code>等配置项，便于配置和管理</p> 
<p>8. 支持宽屏(页面占满屏幕)和窄屏(页面占据80%左右居中显示)设置</p> 
<blockquote> 
 <p>在 管理后台 -> 配置管理 -> 页面 里面进行设置</p> 
</blockquote> 
<p>9. 游客阅读设置，支持设置允许未登录的游客可阅读的内容百分比（默认为100%）。</p> 
<blockquote> 
 <p>在 管理后台 -> 配置管理 -> 运营 里面设置</p> 
</blockquote> 
<p><img alt src="https://static.sitestack.cn/projects/help/202111/16b3e13545ff07b0.png" referrerpolicy="no-referrer"></p> 
<p>10. 修复书籍分类数量统计不正确的问题</p> 
<p>11. 修复一个安全问题（<strong>建议先行版用户升级到当前 v2.11 版本，普通版本用户升级到 v2.10 版本</strong>）</p> 
<p>12. 支持章节内容评论以及回复评论(均需要后台审核方可显示)</p> 
<p><img alt src="https://static.sitestack.cn/projects/help/202111/16b3c146028d8fd4.png" referrerpolicy="no-referrer"></p> 
<p>13. 根据依赖安装情况屏蔽相关功能:</p> 
<table> 
 <thead> 
  <tr> 
   <th>依赖</th> 
   <th>作用</th> 
   <th>关联功能</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>calibre</td> 
   <td>生成 pdf、epub、mobi等电子书</td> 
   <td>未安装该依赖，屏蔽电子书生成按钮</td> 
  </tr> 
  <tr> 
   <td>git</td> 
   <td>导入 gitee、github 等git托管平台的电子书</td> 
   <td>未安装该依赖，屏蔽 git clone 方式的电子书导入</td> 
  </tr> 
  <tr> 
   <td>chrome 或 puppeteer</td> 
   <td>内容采集和渲染的导入内容</td> 
   <td>未安装该依赖，屏蔽所有书籍导入相关页面功能</td> 
  </tr> 
 </tbody> 
</table> 
<p><strong>温馨提示</strong>：</p> 
<ol> 
 <li>升级部署前，请自行对旧版本程序以及数据库进行备份。</li> 
 <li>本次升级，数据库表结构有变动，升级时务必执行数据初始化命令(不会影响现存数据)：</li> 
</ol> 
<pre><code>./BookStack install
</code></pre> 
<ol start="3"> 
 <li>详细 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bookstack.cn%2Fread%2Fhelp%2FUbuntu.md" target="_blank">安装部署文档</a></li> 
</ol> 
<h2>鸣谢</h2> 
<ol> 
 <li>上述升级日志中第 1~4 点功能，由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstudy.sf.163.com%2F" target="_blank">网易有数</a> 赞助开发</li> 
 <li>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fb1nslashsh" target="_blank">@b1nslashsh</a> 反馈的安全问题。</li> 
</ol> 
<h2>BookStack（书栈）变更开源方式说明</h2> 
<p>变更开源方式不是变更开源协议。详见 <a href="https://my.oschina.net/u/2009560/blog/4276247">《BookStack（书栈）变更开源方式说明》</a></p> 
<h2>相关地址</h2> 
<p><strong>BookStack 官网</strong></p> 
<ul> 
 <li>书栈网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bookstack.cn" target="_blank">https://www.bookstack.cn</a></li> 
 <li>手机APP下载体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bookstack.cn%2Fapp" target="_blank">https://www.bookstack.cn/app</a></li> 
</ul> 
<p><strong>BookStack 开源地址</strong></p> 
<ul> 
 <li>Gitee (码云): <a href="https://gitee.com/truthhun/BookStack">https://gitee.com/truthhun/BookStack</a></li> 
 <li>GitHub 开源: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTruthHun%2FBookStack" target="_blank">https://github.com/TruthHun/BookStack</a></li> 
</ul> 
<p><strong>BookStack 先行版地址</strong></p> 
<ul> 
 <li>Gitee (码云): <a href="https://gitee.com/truthhun/bookstack-x">https://gitee.com/truthhun/bookstack-x</a></li> 
 <li>GitHub 开源: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTruthHun%2FBookStack-X" target="_blank">https://github.com/TruthHun/BookStack-X</a></li> 
</ul> 
<p><strong>配套手机APP BookChatApp 开源地址</strong></p> 
<ul> 
 <li>Gitee (码云)：<a href="https://gitee.com/truthhun/BookChatApp">https://gitee.com/truthhun/BookChatApp</a></li> 
 <li>GitHub 开源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftruthhun%2FBookChatApp" target="_blank">https://github.com/truthhun/BookChatApp</a></li> 
</ul> 
<p><strong>配套微信小程序 BookChat 开源地址</strong></p> 
<ul> 
 <li>Gitee (码云)：<a href="https://gitee.com/truthhun/BookChat">https://gitee.com/truthhun/BookChat</a></li> 
 <li>GitHub 开源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftruthhun%2FBookChat" target="_blank">https://github.com/truthhun/BookChat</a></li> 
</ul>
                                        </div>
                                      
</div>
            