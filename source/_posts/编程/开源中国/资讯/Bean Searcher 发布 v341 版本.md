
---
title: 'Bean Searcher 发布 v3.4.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2521'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 10:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2521'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Better</h3> 
<ul> 
 <li>Bean Searcher 
  <ul> 
   <li>优化 SQL 生成逻辑：当<span> </span><code>@SearchBean</code><span> </span>注解的<span> </span><code>joinCond</code><span> </span>属性只有一个拼接参数 且 该参数值为空时，则使其不参与<span> </span><code>where</code><span> </span>子句</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐛 Bug Fixes</h3> 
<ul> 
 <li>修复<span> </span><code>DateFieldConvertor</code><span> </span>无法将<span> </span><code>java.sql.Date</code><span> </span>转换为<span> </span><code>LocalDate / LocalDateTime</code><span> </span>的问题</li> 
 <li>修复<span> </span><code>DateFieldConvertor</code><span> </span>转换<span> </span><code>LocalDate / LocalDateTime</code><span> </span>时会产生时区偏差的问题</li> 
 <li>修复<span> </span><code>DateFormatFieldConvertor</code><span> </span>无法格式化<span> </span><code>java.sql.Date / java.sql.Time</code><span> </span>的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">参见：<br> https://github.com/ejlchina/bean-searcher/releases<br> https://gitee.com/ejlchina-zhxu/bean-searcher/releases</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#4a4a4a">还不了解的同学这里都有介绍哦：</span><br> <br> <span style="background-color:#ffffff; color:#4a4a4a">我这样写代码效率提高了100倍：https://juejin.cn/post/7027733039299952676</span><br> <span style="background-color:#ffffff; color:#4a4a4a">系统教程：https://searcher.ejlchina.com/</span></p>
                                        </div>
                                      
</div>
            