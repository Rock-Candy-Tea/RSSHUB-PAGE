
---
title: 'ORM 工具 dbVisitor 5.1.0 发布，增强 Spring_SpringBoot 整合'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5783'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 05:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5783'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#1c1e21; text-align:start">dbVisitor 是一个全功能数据库访问ORM工具，提供对象映射、丰富的类型处理、动态SQL、存储过程、 内置分页方言20+、 支持嵌套事务、多数据源、条件构造器、INSERT 策略、多语句/多结果。并兼容 Spring 及 MyBatis 用法。 它不依赖任何其它框架，因此可以很方便的和任意一个框架整合在一起使用。</p> 
<h2 style="text-align:start">依赖</h2> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span style="color:#393a34"><</span><span style="color:#00009f">dependency</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34"><</span><span style="color:#00009f">groupId</span><span style="color:#393a34">></span><span>net.hasor</span><span style="color:#393a34"></</span><span style="color:#00009f">groupId</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34"><</span><span style="color:#00009f">artifactId</span><span style="color:#393a34">></span><span>dbvisitor</span><span style="color:#393a34"></</span><span style="color:#00009f">artifactId</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span>    </span><span style="color:#393a34"><</span><span style="color:#00009f">version</span><span style="color:#393a34">></span><span>5.1.0</span><span style="color:#393a34"></</span><span style="color:#00009f">version</span><span style="color:#393a34">></span>
</span><span style="color:#393a34"><span style="color:#393a34"></</span><span style="color:#00009f">dependency</span><span style="color:#393a34">></span></span></code></pre> 
 </div> 
</div> 
<h2 style="text-align:start">新增<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2Fdocs%2Freleases%2F5.1.x%2Fv5.1.0%23%25E6%2596%25B0%25E5%25A2%259E" target="_blank">​</a></h2> 
<ul> 
 <li>新增 dbvisitor-faker 工具专注测试数据生成，5.1.0 为预览版</li> 
 <li>新增 dbvisitor-hasor 整合(基于 hasor 2.4.5)</li> 
 <li>新增 dbvisitor-guice 整合(基于 guice 5.1.0)</li> 
</ul> 
<h2 style="text-align:start">优化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2Fdocs%2Freleases%2F5.1.x%2Fv5.1.0%23%25E4%25BC%2598%25E5%258C%2596" target="_blank">​</a></h2> 
<ul> 
 <li>一些 Provider 工具由于只有 Hasor 框架才会用到，因此移动到 Hasor 项目中。</li> 
 <li>优化 SpringBoot 整合项目，方便 Idea 等编辑器对属性的识别。</li> 
 <li>修复 SqlServer 特殊表名的拼写逻辑。</li> 
 <li>表增加 catalog 纬度。</li> 
 <li>分页属性的 start, limit 两个参数 改为 long 类型。</li> 
 <li><code>ConditionSqlDialect</code><span> </span>接口增加<span> </span><code>randomQuery</code><span> </span>方法用于提供随机查询的方言</li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">相关链接</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方网站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2F" target="_blank">https://www.dbvisitor.net/</a><br> 源码地址：<a href="https://gitee.com/zycgit/dbvisitor">https://gitee.com/zycgit/dbvisitor</a><br> Spring Boot 整合手册，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2Fdocs%2Fintegration%2Fwith-springboot" target="_blank">https://www.dbvisitor.net/docs/integration/with-springboot</a><br> 快速上手：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.dbvisitor.net%2Fdocs%2Fguides%2Fquickstart" target="_blank">https://www.dbvisitor.net/docs/guides/quickstart</a></p>
                                        </div>
                                      
</div>
            