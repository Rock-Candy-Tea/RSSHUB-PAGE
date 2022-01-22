
---
title: 'Bean Searcher 发布 v3.3.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4742'
author: 开源中国
comments: false
date: Sat, 22 Jan 2022 11:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4742'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Features</h3> 
<ul> 
 <li>Bean Searcher 
  <ul> 
   <li><code>MapBuilder</code><span> </span>新增<span> </span><code>op(Class<? extends FieldOp> op)</code><span> </span>方法</li> 
   <li>优化<span> </span><code>DateValueCorrector</code>, 可配置支持的运算符</li> 
  </ul> </li> 
 <li>Bean Searcher Boot Starter 
  <ul> 
   <li>新增<span> </span><code>bean-searcher.sql.use-date-value-corrector</code><span> </span>配置项，默认为<span> </span><code>true</code>，表示是否使用日期值纠正器</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">✨ Better</h3> 
<ul> 
 <li>Bean Searcher 
  <ul> 
   <li>优化字段运算符的匹配逻辑：使用严格模式</li> 
   <li>优化<span> </span><code>Operator</code><span> </span>常量，使其可以直接作为<span> </span><code>@DbField.onlyOn</code><span> </span>的值（兼容以前版本，便于升级）</li> 
  </ul> </li> 
 <li>Bean Searcher Boot Starter 
  <ul> 
   <li>优化自动配置机制，不再强依赖于<span> </span><code>DataSourceAutoConfiguration</code><span> </span>与 Spring 容器中的<span> </span><code>DataSource</code><span> </span>Bean</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐛 Bug Fixes</h3> 
<ul> 
 <li>修复当用户对同一个运算符 new 很多次时可能会导致<span> </span><code>FieldOpPool</code><span> </span>膨胀的问题</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            