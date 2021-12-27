
---
title: 'MyBatis 3.5.9 发布，Java 数据持久层框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=606'
author: 开源中国
comments: false
date: Sun, 26 Dec 2021 23:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=606'
---

<div>   
<div class="content">
                                                                                            <p>MyBatis 3.5.9 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.mybatis.org%2F2021%2F12%2Fmybatis-359-released.html" target="_blank">已发布</a>，MyBatis 的前身为 iBatis，是一个数据持久层（ORM）框架，它提供的持久层能力包括 SQL Maps 和 Data Access Objects（DAO）。</p> 
<p>主要更新内容：</p> 
<ul style="margin-left:.5em; margin-right:.5em"> 
 <li>将<code>nullable</code><span>添加至</span><code><collection /></code>。如果启用此配置项，当 collection 为<code>null</code><span>时，</span>它会<span>跳过迭代，而不是抛出异常。如需</span>在全局范围内启用此功能，则要在配置中设置 nullableOnForEach=true <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%2F1883" target="_blank">#1883</a></li> 
</ul> 
<p>此外，新版本还将 Log4J 依赖项的版本更新为 2.17.0。</p> 
<p>请注意，MyBatis 的 pom.xml 中 Log4J 依赖的范围是“可选的”，这意味着：</p> 
<ul style="margin-left:.5em; margin-right:.5em"> 
 <li>可以在没有 Log4J 的情况下使用 MyBatis</li> 
 <li>将 MyBatis 添加到项目的依赖项中不会隐式引入 Log4J</li> 
 <li>更新 MyBatis 版本不会使您的项目更安全，因为它不会影响您项目中的 Log4J 版本</li> 
 <li>无论使用的是哪个 MyBatis 版本，都可以/必须独立更新 Log4J 版本</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">发布公告还写道，自 3.5.8 以来，此版本没有任何已知的向后不兼容变化，完整变更内容查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fissues%3Fq%3Dis%253Aclosed%2Bmilestone%253A3.5.9" target="_blank">3.5.9 milestone 页面</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下载地址</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Freleases%2Ftag%2Fmybatis-3.5.9" target="_blank">https://github.com/mybatis/mybatis-3/releases/tag/mybatis-3.5.9</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Forg.mybatis%2Fmybatis%2F3.5.9" target="_blank">https://mvnrepository.com/artifact/org.mybatis/mybatis/3.5.9</a></p>
                                        </div>
                                      
</div>
            