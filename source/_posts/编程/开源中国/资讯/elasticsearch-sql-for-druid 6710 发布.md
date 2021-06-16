
---
title: 'elasticsearch-sql-for-druid 6.7.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6741'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 17:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6741'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start">介绍</h4> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNLPchina%2Felasticsearch-sql" target="_blank">elasticsearh-sql 6.7.1</a> 版本对新版本druid 1.2.5+版本支持,原始版本不支持新版本的druid,因后续版本的druid底层类库改动较大。</p> 
<h4 style="text-align:start">软件架构</h4> 
<p>问题记录</p> 
<ul> 
 <li>貌似兼容后不支持 index/type 方式搜索,比如: select * from index/type。但是可以改成 select * from index 使用</li> 
</ul> 
<p>修改内容说明:</p> 
<ol> 
 <li>SQLParensIdentifierExpr 增加clone</li> 
 <li>parseTableSourceRest 改成public</li> 
 <li>MySqlExtractExpr->SQLExtractExpr</li> 
 <li>MySqlMatchAgainstExpr->SQLMatchAgainstExpr</li> 
 <li>dbType -> dbTypeName</li> 
</ol> 
<p>后续:</p> 
<ol> 
 <li>整理相关包引用和版本</li> 
 <li>阅读细节代码重写实现</li> 
</ol> 
<p>使用</p> 
<div style="text-align:start"> 
 <div> 
  <pre><groupId>org.nlpcn</groupId>
<artifactId>elasticsearch-sql-for-druid</artifactId>
<version>6.7.1.0</version>
</dependency></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            