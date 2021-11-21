
---
title: 'MyCms v1.5.1 拓展增强，Laravel 自媒体商城系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-69ae06fd2b2b063e3d233e860030cac20d7.png'
author: 开源中国
comments: false
date: Sun, 21 Nov 2021 11:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-69ae06fd2b2b063e3d233e860030cac20d7.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="600" src="https://oscimg.oschina.net/oscnet/up-69ae06fd2b2b063e3d233e860030cac20d7.png" width="2000" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms是一款基于Laravel开发的开源免费的自媒体博客CMS系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">软件著作权编号：2021SR1543432。MyCms基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">“天行健，君子以自强不息。”</span></strong></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">v1.5.1 更新内容</span></strong></p> 
<p>修正、获取文章链接函数<br> 修正、获取文章标签函数<br> 优化、部分变量名及方法使用<br> 新增、分类和文章获取模板方法<br> 新增、文章分类模型父级关联<br> 新增、分类拓展应用到子分类和文章<br> 新增、后台列表操作按钮新增js回调函数支持<br> 增强、文章分类更新拓展配置方法<br> 新增、CmsService新增方法<br>     1.articleMeta:获取文章拓展<br>     2.categoryMeta:获取分类拓展<br>     3.articlesForSort:根据排序获取文章</p> 
<p><strong>更新重点介绍</strong></p> 
<p>一、拓展应用到子分类</p> 
<p>子分类级分类下的文章可以继承该分类的拓展配置。</p> 
<p><img alt height="957" src="https://oscimg.oschina.net/oscnet/up-49112cd89a25358c3f010facea2fa65f29f.png" width="1600" referrerpolicy="no-referrer"></p> 
<p>二、后台列表按钮增加JS函数支持</p> 
<p>通过函数支持，可以进行自定义按钮。</p> 
<p><img alt height="715" src="https://oscimg.oschina.net/oscnet/up-a5aaaaaa7554af654ac16326793a2239997.png" width="1925" referrerpolicy="no-referrer"></p> 
<p><strong>系统功能</strong></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">后台基础功能</p> 
  <ul> 
   <li>权限管理</li> 
   <li>内容管理</li> 
   <li>商品管理</li> 
   <li>会员管理</li> 
   <li>插件管理</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">前台功能实现</p> 
  <ul> 
   <li>首页</li> 
   <li>文章分类页</li> 
   <li>文章搜索页</li> 
   <li>文章标签页</li> 
   <li>文章详情页</li> 
   <li>文章评论</li> 
   <li>商品列表页</li> 
   <li>商品详情页</li> 
   <li>会员登录/注册</li> 
   <li>会员中心</li> 
  </ul> </li> 
</ul> 
<p><strong>系统特性</strong></p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">Swoole加速</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">简洁优雅、灵活可扩展</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">对SEO优化友好的URL模式</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更优雅、符合SEO优化的分页</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">基础缓存功能及数据库索引建立</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">更具拓展性的路由监听功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">完善的插件安装/卸载机制</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">公共函数埋点更好拓展系统</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">简单易用的模板函数、制作模板更方便</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F" target="_blank">官方网站</a> : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fb386654667%2Fmycms%2Fcontent" target="_blank">文档地址</a> : https://www.kancloud.cn/b386654667/mycms/content</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/qq386654667/mycms">源码下载</a> : https://gitee.com/qq386654667/mycms</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F" target="_blank">演示前台</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.mycms.net.cn%2Fsystem%2Flogin" target="_blank">演示后台</a> : https://demo.mycms.net.cn/system/login</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台：admin / admin</p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>优秀案例</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F" target="_blank">在线计算网</a> : https://www.zaixianjisuan.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F" target="_blank">程序员导航</a> : https://nav.mycms.net.cn/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F" target="_blank">古诗词网</a> : https://www.gushici.top/</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            