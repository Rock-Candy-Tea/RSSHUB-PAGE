
---
title: 'MyCms 自媒体 CMS 系统 v3.2.2，广告插件优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 12:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1700" src="https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png" width="3164" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 是一款基于Laravel开发的开源免费的自媒体博客CMS系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><strong>v3.2.2<span> </span></strong><strong style="color:#40485b">更新内容</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">新增:广告类型细分</span><br> <span style="background-color:#ffffff; color:#40485b">新增:文章状态控制</span><br> <span style="background-color:#ffffff; color:#40485b">新增:推送插件兼容文章状态</span><br> <span style="background-color:#ffffff; color:#40485b">新增:后台添加和更新后操作埋点</span><br> <span style="background-color:#ffffff; color:#40485b">修复:首次启用广告插件出错问题</span><br> <span style="background-color:#ffffff; color:#40485b">修复:上传组件因命名产生的异常</span></p> 
<p><strong>更新重点</strong></p> 
<p>一、广告插件优化</p> 
<p>新增图片广告和文本链接。</p> 
<pre><code class="language-php">//调用方法

@foreach(ad('link') as $ad)
<a href="&#123;&#123;$ad['url']&#125;&#125;">&#123;&#123;$ad['text']&#125;&#125;</a>
@endforeach

@foreach(ad('image') as $ad)
<a href="&#123;&#123;$ad['url']&#125;&#125;"><img src="&#123;&#123;$ad['path']&#125;&#125;"></a>
@endforeach</code></pre> 
<p><img alt height="557" src="https://oscimg.oschina.net/oscnet/up-bdd5b5f155e02a158fa47f200559510b77b.png" width="788" referrerpolicy="no-referrer"></p> 
<p>二、文章状态控制</p> 
<p><img alt height="254" src="https://oscimg.oschina.net/oscnet/up-7b24e7a50d14fa270cb035e137da0c22eef.png" width="1699" referrerpolicy="no-referrer"></p> 
<p><img alt height="612" src="https://oscimg.oschina.net/oscnet/up-44893b8c8496e73a3245837d8a04c67452f.png" width="811" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">重磅推荐</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">活码二维码工具是经过深度挖掘，制作的一款为广大运营者提供便捷的推广裂变工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">文档地址：https://www.mycms.net.cn/huoma</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">活码官网：https://www.huomahuoma.com/</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><img alt height="1031" src="https://oscimg.oschina.net/oscnet/up-a0812ec5378b22cae403ec5914a8968c4f8.png" width="1242" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>站点地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">官方网站 : https://www.mycms.net.cn/</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用手册：https://www.mycms.net.cn/shouce</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">API文档：https://www.mycms.net.cn/api-doc</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">模板下载：https://www.mycms.net.cn/muban</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">源码下载 : https://gitee.com/qq386654667/mycms</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台 : https://demo.mycms.net.cn/system/login</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">演示后台：admin / admin</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>优秀案例</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F" target="_blank">在线计算网</a><span> </span>: https://www.zaixianjisuan.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F" target="_blank">程序员导航</a><span> </span>: https://nav.mycms.net.cn/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F" target="_blank">古诗词网</a><span> </span>: https://www.gushici.top/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.huomahuoma.com%2F" target="_blank">火马活码</a>：https://www.huomahuoma.com/</li> 
</ul>
                                        </div>
                                      
</div>
            