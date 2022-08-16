
---
title: 'Bouyei.DbFactory 22.8.16 数据库中间件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=893'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 16:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=893'
---

<div>   
<div class="content">
                                                                                            <p>.net(framework,.net 6,net standard)多种数据库类型支持的ORM数据库中间件，兼容ADO原生脚本执行。</p> 
<p>1、新增支持oracle分页。</p> 
<p>2、支持增加、修改、查询的动态对象查询返回。</p> 
<p>2.1、查询：</p> 
<p>var qrt = dbProvider.QueryOrderBy(x => true, c => new &#123; c.uname, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fc.id" target="_blank">c.id</a> &#125;, orderbyColumn, SortType.Desc, 0, 10);</p> 
<p>2.2、修改:</p> 
<p>var urt = dbProvider.Update(x => new &#123; uname = "bouyei_hello" &#125;, w => <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fw.id" target="_blank">w.id</a> == 11);</p> 
<p>2.3、插入：</p> 
<p>var irt= dbProvider.Insert(x => new  &#123; uname="hello", id=11&#125;);</p>
                                        </div>
                                      
</div>
            