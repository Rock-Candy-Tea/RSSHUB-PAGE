
---
title: 'MyCms 自媒体 CMS 系统 v3.2.1，后台默认首页改版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 02:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1700" src="https://oscimg.oschina.net/oscnet/up-33259a8ab000bc5a915811ec265450deaa3.png" width="3164" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 是一款基于Laravel开发的开源免费的自媒体博客CMS系统，助力开发者知识技能变现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">MyCms 基于Apache2.0开源协议发布，免费且不限制商业使用，欢迎持续关注我们。</span></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>v3.2.1 </strong><strong style="color:#40485b">更新内容</strong></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">新增：后台默认首页改版 优化：获取分类函数 优化：日志插件IP字段长度 优化：管理员最后登录IP字段长度 修复：自定义页面内容长度</p> 
<p><strong>更新重点</strong></p> 
<p>一、后台默认首页改版</p> 
<p><img alt height="536" src="https://oscimg.oschina.net/oscnet/up-6b42d4f51dffb11107bce18f0d06e4a1a59.png" width="1691" referrerpolicy="no-referrer"></p> 
<p>二、分类函数优化</p> 
<p>新增获取指定分类的子分类</p> 
<pre><code class="language-php">/**
 * 分类列表
 */
if (!function_exists('categories')) &#123;
    function categories($pid = 0)
    &#123;
        $values = app('cms')->categoryTree($pid);
        return pipeline_func($values, 'categories');
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">重磅推荐</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">活码二维码工具是经过深度挖掘，制作的一款为广大运营者提供便捷的推广裂变工具。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">文档地址：https://www.mycms.net.cn/huoma</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">活码官网：https://www.huomahuoma.com/</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333"><img alt height="1031" src="https://oscimg.oschina.net/oscnet/up-a0812ec5378b22cae403ec5914a8968c4f8.png" width="1242" referrerpolicy="no-referrer"></span></p> 
<p><strong>站点地址</strong></p> 
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
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zaixianjisuan.com%2F" target="_blank">在线计算网</a> : https://www.zaixianjisuan.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnav.mycms.net.cn%2F" target="_blank">程序员导航</a> : https://nav.mycms.net.cn/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gushici.top%2F" target="_blank">古诗词网</a> : https://www.gushici.top/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.huomahuoma.com%2F" target="_blank">火马活码</a>：https://www.huomahuoma.com/</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jixunhao.com%2F" target="_blank">极讯号</a>：https://www.jixunhao.com/</li> 
</ul>
                                        </div>
                                      
</div>
            