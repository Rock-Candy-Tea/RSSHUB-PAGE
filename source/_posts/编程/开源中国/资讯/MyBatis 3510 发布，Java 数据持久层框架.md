
---
title: 'MyBatis 3.5.10 发布，Java 数据持久层框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9693'
author: 开源中国
comments: false
date: Fri, 27 May 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9693'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.mybatis.org%2F2022%2F05%2Fmybatis-3510-released.html" target="_blank">MyBatis 3.5.10 已发布</a>，MyBatis 的前身为 iBatis，是一个数据持久层（ORM）框架，它提供的持久层能力包括 SQL Maps 和 Data Access Objects（DAO）。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>主要变化</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#222222">Bugfix</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 `test` 表达式中调用方法时出现意外的非法反射访问警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2392" target="_blank">#2392</a></li> 
 <li><span style="color:#222222">自动映射 Records 时出现 IllegalAccessException </span>(JEP-359) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2195" target="_blank">#2195</a></li> 
 <li>当 `PooledConnection#getConnection()` 被中断时，无法自动设置 'interrupted' 状态 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2503" target="_blank">#2503</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">功能增强</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加新选项 `argNameBasedConstructorAutoMapping`，启用后，构造函数参数名称用于在自动映射时查找列 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2192" target="_blank">#2192</a></li> 
 <li>在 `<constructor />`中，`<idArg />` 支持被排列在 `<arg />` 后面 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2541" target="_blank">#2541</a></li> 
 <li>为 `JdbcTransactionFactory` 添加新属性 `skipSetAutoCommitOnClose`。跳过 `setAutoCommit()` 调用可以提升某些驱动程序的性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F2426" target="_blank">#2426</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">发布公告还写道，自 3.5.9 以来，此版本没有任何已知的向后不兼容变化，完整变更内容查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%3Fq%3Dis%253Aclosed%2Bmilestone%253A3.5.10" target="_blank">3.5.10 milestone 页面</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>下载地址</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Freleases%2Ftag%2Fmybatis-3.5.10" target="_blank">https://github.com/mybatis/mybatis-3/releases/tag/mybatis-3.5.10</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Forg.mybatis%2Fmybatis%2F3.5.10" target="_blank">https://mvnrepository.com/artifact/org.mybatis/mybatis/3.5.10</a></p>
                                        </div>
                                      
</div>
            