
---
title: 'MyCms v1.9.0 开启用户 API、双标题，开源自媒体系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eaaffe862c261a1cc14b93af13c3b0c85e7.png'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 09:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eaaffe862c261a1cc14b93af13c3b0c85e7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="1694" src="https://oscimg.oschina.net/oscnet/up-eaaffe862c261a1cc14b93af13c3b0c85e7.png" width="3168" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms是一款基于Laravel开发的开源免费的自媒体博客CMS系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">软件著作权编号：2021SR1543432。MyCms基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p><strong>“心之所向，素履以往”</strong></p> 
<p><strong>v1.9.0 [更新内容]</strong></p> 
<p>新增：API-文章评论列表接口<br> 新增：API-文章评论发布接口<br> 新增：API-会员登录接口<br> 新增：API-会员注册接口<br> 新增：API-会员信息接口<br> 新增：文章双标题<br> 新增：文章分类双标题<br> 优化：网站地图插件<br> 优化：插件列表显示</p> 
<p><strong>更新重点</strong></p> 
<p>一、用户接口</p> 
<p>二、文章双标题</p> 
<p><strong>接口签名方法</strong></p> 
<ol> 
 <li>获取所有 post 内容，不包括字节类型参数，如文件、字节流，剔除 sign 字段；</li> 
 <li>按照第一个字符的键值 ASCII 码递增排序（字母升序排序），如果遇到相同字符则按照第二个字符的键值 ASCII 码递增排序，以此类推；</li> 
 <li>将排序后的参数与其对应值，组合成 参数=参数值 的格式，并且把这些参数用<span> </span><code>&</code><span> </span>字符连接起来，此时生成的字符串为待签名字符串。</li> 
 <li>待签名字符串拼接自己设置的密钥，然后md5加密即可获得签名字符串。</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统功能</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>后台基础功能 
  <ul> 
   <li>权限管理</li> 
   <li>内容管理</li> 
   <li>商品管理</li> 
   <li>会员管理</li> 
   <li>插件管理</li> 
  </ul> </li> 
 <li>前台功能实现 
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
   <li>文章评论列表接口</li> 
   <li>文章评论发布接口</li> 
   <li>商品分类列表接口</li> 
   <li>商品分类详情接口</li> 
   <li>商品列表接口</li> 
   <li>商品详情接口</li> 
   <li>会员登录接口</li> 
   <li>会员注册接口</li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>系统特性</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持Swoole加速</li> 
 <li>简易安装程序</li> 
 <li>简洁优雅、灵活可扩展</li> 
 <li>完善的插件安装/卸载机制</li> 
 <li>对SEO优化友好的URL模式</li> 
 <li>公共函数埋点更好拓展系统</li> 
 <li>更具拓展性的路由监听功能</li> 
 <li>更优雅、符合SEO优化的分页</li> 
 <li>基础缓存功能及数据库索引建立</li> 
 <li>简单易用的模板函数、制作模板更方便</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F%3Fv1.9.0" target="_blank">官方网站</a> : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2Fshouce%3Fv1.9.0" target="_blank">使用手册</a>：https://www.mycms.net.cn/shouce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2Fapi-doc%3Fv1.9.0" target="_blank">API文档</a>：https://www.mycms.net.cn/api-doc</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/qq386654667/mycms">源码下载</a> : https://gitee.com/qq386654667/mycms</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mycms.net.cn%2F" target="_blank">演示前台</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.mycms.net.cn%2Fsystem%2Flogin" target="_blank">演示后台</a> : https://demo.mycms.net.cn/system/login</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台：admin / admin</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>优秀案例</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F%3Fv1.9.0" target="_blank">在线计算网</a> : https://www.zaixianjisuan.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F%3Fv1.9.0" target="_blank">程序员导航</a> : https://nav.mycms.net.cn/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F%3Fv1.9.0" target="_blank">古诗词网</a> : https://www.gushici.top/</li> 
</ul>
                                        </div>
                                      
</div>
            