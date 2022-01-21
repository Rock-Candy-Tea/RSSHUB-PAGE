
---
title: 'Bean Searcher 发布 v3.3.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://lf3-cdn-tos.bytescm.com/obj/static/xitu_juejin_web/img/jj_emoji_2.cd1e2bd.png'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 19:34:00 GMT
thumbnail: 'https://lf3-cdn-tos.bytescm.com/obj/static/xitu_juejin_web/img/jj_emoji_2.cd1e2bd.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Features</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">Bean Searcher</p> 
  <ul> 
   <li>新增<span> </span><code>FieldOp</code><span> </span>接口，用户可用之扩展自己的字段运算符</li> 
   <li>新增<span> </span><code>FieldOpPool</code><span> </span>类，用户可用之定制一套全新的字段运算符</li> 
   <li>内置新增<span> </span><code>NotIn</code><span> </span>/<span> </span><code>ni</code><span> </span>与<span> </span><code>NotBetween</code><span> </span>/<span> </span><code>nb</code><span> </span>运算符</li> 
   <li>内置运算符<span> </span><code>MultiValue</code><span> </span>/<span> </span><code>mv</code><span> </span>重命名为<span> </span><code>InList</code><span> </span>/<span> </span><code>il</code><span> </span>(原运算符仍可使用)</li> 
   <li><code>DefaultDbMapping</code><span> </span>新增<span> </span><code>redundantSuffixes</code><span> </span>属性，可配置 在实体类自动映射表名时 统一去除类名中的冗余后缀（比如 VO、DTO 等）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bean Searcher Boot Starter</p> 
  <ul> 
   <li>新增<span> </span><code>bean-searcher.sql.default-mapping.redundant-suffixes</code><span> </span>配置项，可配置多个冗余后缀</li> 
   <li>支持直接声明一个<span> </span><code>FieldOp</code><span> </span>类型的 Spring Bean 来扩展一个新的字段运算符</li> 
   <li>支持直接声明一个<span> </span><code>FieldOpPool</code><span> </span>类型的 Spring Bean 来定制一套全新的字符运算符</li> 
  </ul> </li> 
</ul> 
<p>详细请见：</p> 
<p>https://github.com/ejlchina/bean-searcher<br> https://gitee.com/ejlchina-zhxu/bean-searcher<br> http://searcher.ejlchina.com/</p> 
<p>还没点 Star 的小伙伴赏一颗 Star 吧 <img alt="[呲牙]" height="20" src="https://lf3-cdn-tos.bytescm.com/obj/static/xitu_juejin_web/img/jj_emoji_2.cd1e2bd.png" width="20" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            