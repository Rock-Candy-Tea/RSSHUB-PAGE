
---
title: 'MyCms v1.7.0 开放 API，开源 Laravel 自媒体 CMS 系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0774c5b508494891b0a69e47ac0ec7bea87.png'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 11:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0774c5b508494891b0a69e47ac0ec7bea87.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="600" src="https://oscimg.oschina.net/oscnet/up-0774c5b508494891b0a69e47ac0ec7bea87.png" width="2000" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms是一款基于Laravel开发的开源免费的自媒体博客CMS系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">软件著作权编号：2021SR1543432。MyCms基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p><strong>“仍然是我有我，在兑现我梦与想。来环游我世界，这一切自由自创”</strong></p> 
<p><strong>v1.7.0 [开放API]</strong></p> 
<p>[更新内容]<br> 新增：API模块<br> 新增：API-签名验证中间件<br> 新增：API-请求Accept中间件<br> 新增：API-获取系统时间接口<br> 新增：API-获取文章列表接口<br> 新增：API-获取文章详情接口<br> 新增：API-获取文章分类列表接口<br> 新增：API-获取文章分类详情接口<br> 新增：API-查询结果转返回字段方法<br> 新增：加载模板自定义路由<br> 新增：加载模板自定义函数<br> 新增：增加成功/失败响应方法<br> 新增：后台获取树形菜单方法（下拉框）<br> 新增：获取请求参数方法增加默认值选项<br> 新增：获取文章详情/增加文章浏览次数/分类详情方法<br> 优化：优化缓存读取系统配置<br> 优化：SEO插件公共函数<br> 优化：模板头部样式</p> 
<p><strong>更新重点</strong></p> 
<p>一、新增API模块</p> 
<p>API文档：https://www.mycms.net.cn/api-doc</p> 
<p>二、模板自定义路由/函数</p> 
<p>模板可以新增自定义路由及函数。</p> 
<p>自定义路由路径：Template/模板名/routes/web.php</p> 
<p>自定义函数路径：Template/模板名/helpers/functions.php</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统功能</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>后台基础功能 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>权限管理</li> 
   <li>内容管理</li> 
   <li>商品管理</li> 
   <li>会员管理</li> 
   <li>插件管理</li> 
  </ul> </li> 
 <li>前台功能实现 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
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
 <li>API接口 
  <ul> 
   <li>签名加密</li> 
   <li>系统时间接口</li> 
   <li>文章分类列表接口</li> 
   <li>文章分类详情接口</li> 
   <li>文章列表接口 
    <ul> 
     <li>整站最新、最热文章</li> 
     <li>分类最新、最热文章</li> 
     <li>标签关联文章列表</li> 
     <li>搜索文章列表</li> 
    </ul> </li> 
   <li>文章详情接口</li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统特性</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持Swoole加速</li> 
 <li>简洁优雅、灵活可扩展</li> 
 <li>完善的插件安装/卸载机制</li> 
 <li>对SEO优化友好的URL模式</li> 
 <li>公共函数埋点更好拓展系统</li> 
 <li>更具拓展性的路由监听功能</li> 
 <li>更优雅、符合SEO优化的分页</li> 
 <li>基础缓存功能及数据库索引建立</li> 
 <li>简单易用的模板函数、制作模板更方便</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F" target="_blank">官方网站</a> : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2Fshouce" target="_blank">使用手册</a>：https://www.mycms.net.cn/shouce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2Fapi-doc" target="_blank">API文档</a>：https://www.mycms.net.cn/api-doc</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/qq386654667/mycms">源码下载</a> : https://gitee.com/qq386654667/mycms</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F" target="_blank">演示前台</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.mycms.net.cn%2Fsystem%2Flogin" target="_blank">演示后台</a> : https://demo.mycms.net.cn/system/login</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台：admin / admin</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>优秀案例</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F" target="_blank">在线计算网</a> : https://www.zaixianjisuan.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F" target="_blank">程序员导航</a> : https://nav.mycms.net.cn/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F" target="_blank">古诗词网</a> : https://www.gushici.top/</li> 
</ul>
                                        </div>
                                      
</div>
            