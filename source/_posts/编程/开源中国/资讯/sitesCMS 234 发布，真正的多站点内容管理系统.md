
---
title: 'sitesCMS 2.3.4 发布，真正的多站点内容管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-07d487d9165fa23c5edd91dae4f1c132d9c.png'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 21:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-07d487d9165fa23c5edd91dae4f1c132d9c.png'
---

<div>   
<div class="content">
                                                                                            <p>sitesCMS v2.3.4发布，优化部分功能，同时我们发布了cds和admin拆分版，实现真正的多站点内容管理。</p> 
<p><a href="https://gitee.com/xhhxb/sitescms4admin">sitesCMS4Admin</a> 是sitesCMS管理端拆分版，拆分的同时提升了内容管理内里，切换站点后不需要重新登录就可以直接管理多站点数据，比sitesCMS本身更加灵活轻便。</p> 
<p><a href="https://gitee.com/xhhxb/sitescms4cds">sitesCMS4cds</a> 是sitesCMS展示端拆分版，拆分的同时适配了sitesCMS4Admin，可以很好的实现文件/图片的管理，同时相比sitesCMS更加轻便，没有了后端管理功能，实现单纯的内容展示。</p> 
<p>下面通过一个图片介绍sitesCMS多站点内容管理方案，注意其中的附件/图片的处理，这个完全可以使用第三方平台，目前这么做单纯的是因为简便。</p> 
<p><img alt height="829" src="https://oscimg.oschina.net/oscnet/up-07d487d9165fa23c5edd91dae4f1c132d9c.png" width="2332" referrerpolicy="no-referrer"></p> 
<p>下面回顾下进几次的更新内容：</p> 
<h2 style="margin-left:0; margin-right:0">v2.3.4 2021-12-21</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【优化】权限不足时的提示信息；</li> 
 <li>【优化】权限管理界面布局；</li> 
 <li>【优化】异步数据交互；</li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<h2 style="margin-left:0; margin-right:0">v2.3.3 2021-12-16</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【优化】优化viewColLastArt方法，添加文章点击数统计。</li> 
</ul> 
<p style="margin-left:0; margin-right:0"> </p> 
<h2 style="margin-left:0; margin-right:0">v2.3.1 2021-12-05</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【新增】锁定站点功能，禁止后台切换站点；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.2.1 2021-11-07</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【优化】优化表单token更新机制，用户体验更加友好；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.2.0 2021-11-04</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【新增】新增公司信息模块；</li> 
 <li>【优化】文章模块新增子标题、作者、来源、属性、标签、关键字字段；</li> 
 <li>【优化】站点模块新增SEO标题、SEO关键字、IPC备案号、公安备案字段；</li> 
 <li>【优化】重写静态页生成模块；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.1.1 2021-08-18</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【优化】优化静态页生成功能</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.1.0 2021-08-14</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【新增】首页支持自动生成静态页</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.6 2021-06-16</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【升级】Layui升级到2.0.8版；</li> 
 <li>【升级】wangEditor升级到4.7.1版；</li> 
 <li>【优化】cms端数据分页大小由8改到10；</li> 
 <li>【优化】数据库表的编码统一改为utf8mb4，升级为utf8的超集；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.5 2021-03-28</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【新增】新增cds跳转方法，页面跳转更加灵活；</li> 
 <li>【新增】新增栏目文章获取加强版指令，可指定排序方式；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.4 2021-03-21</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【修复】栏目管理bug；</li> 
 <li>【修复】站点管理bug；</li> 
 <li>【新增】栏目可指定排序；</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.3 2021-03-11</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【优化】优化站点管理功能；</li> 
 <li>【优化】调整SiteInfo在模板引擎中共享对象名称为SiteInfo，涉及页面较多，请注意。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.2 2021-03-08</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【修复】文章内容不保存字体大小的问题；</li> 
 <li>【优化】默认站点参数取值调整。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"> </h2> 
<h2 style="margin-left:0; margin-right:0">v2.0.1 2021-03-02</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>【修复】调整用户角色权限报错问题；</li> 
 <li>【优化】发布端口改到undertow.txt文件；</li> 
</ul>
                                        </div>
                                      
</div>
            