
---
title: 'Bean Searcher 发布 v3.5.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1616'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 19:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1616'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Features</h3> 
<ul> 
 <li>Bean Searcher 
  <ul> 
   <li>新增<span> </span><code>GroupResolver</code>、<code>ExprParser</code><span> </span>等组件，实现参数分组与逻辑关系的表达、运算、智能化简与解析的能力<br> 参见：<a href="https://gitee.com/ejlchina-zhxu/bean-searcher/issues/I4J229">#I4J229:如何实现 更加复杂 的 or 条件分组查询</a></li> 
   <li><code>DefaultParamResolver</code><span> </span>新增<span> </span><code>gexprName</code>、<code>groupSeparator</code><span> </span>属性，用于指定组参数名的形式</li> 
   <li><code>MapBuilder</code>（参数构建器）新增<span> </span><code>group(String group)</code><span> </span>方法，用于构建字段参数组</li> 
   <li><code>MapBuilder</code><span> </span>新增<span> </span><code>groupExpr(String expr)</code><span> </span>方法，用于指定参数组间的逻辑关系</li> 
   <li>新增<span> </span><code>TimeFieldConvertor</code>，支持<span> </span><code>java.sql.Time</code><span> </span>与<span> </span><code>LocalTime</code><span> </span>之间的转换</li> 
   <li>注解<span> </span><code>@DbField</code><span> </span>注解新增<span> </span><code>alias</code><span> </span>属性，支持手动指定字段别名（不指定则自动生成）</li> 
  </ul> </li> 
 <li>Bean Searcher Boot Starter 
  <ul> 
   <li>新增<span> </span><code>bean-searcher.params.group.enable</code><span> </span>配置键，可在配置文件中指定是否使用参数组功能，默认为<span> </span><code>true</code></li> 
   <li>新增<span> </span><code>bean-searcher.params.group.expr-name</code><span> </span>配置键，可在配置文件中指定组表达式参数名，默认为<span> </span><code>gexpr</code></li> 
   <li>新增<span> </span><code>bean-searcher.params.group.expr-cache-size</code><span> </span>配置键，可在配置文件中指定组表达式解析缓存的大小，默认为<span> </span><code>50</code><span> </span>个</li> 
   <li>新增<span> </span><code>bean-searcher.params.group.separator</code><span> </span>配置键，可在配置文件中指定参数组分隔符，默认为<span> </span><code>.</code></li> 
   <li>新增<span> </span><code>bean-searcher.field-convertor.use-time</code><span> </span>配置项，表示是否自动添加<span> </span><code>TimeFieldConvertor</code>，默认<span> </span><code>true</code></li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">参见：<br> https://github.com/ejlchina/bean-searcher/releases<br> https://gitee.com/ejlchina-zhxu/bean-searcher/releases</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#4a4a4a">还不了解的同学这里都有介绍哦：</span><br> <br> <span style="background-color:#ffffff; color:#4a4a4a">我这样写代码效率提高了100倍：https://juejin.cn/post/7027733039299952676</span><br> <span style="background-color:#ffffff; color:#4a4a4a">系统教程：https://searcher.ejlchina.com/</span></p>
                                        </div>
                                      
</div>
            