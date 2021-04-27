
---
title: 'BeeCP-3.1.8 发布，高性能 JDBC 池（Java 当前最快）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3092e65a77a8a8c91059bef8fc55ccd4f14.png'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 21:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3092e65a77a8a8c91059bef8fc55ccd4f14.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">小蜜蜂连接池：一款创新式JDBC连接池，具有性能高，代码轻，稳定性好的特点。</p> 
<p style="text-align:start"><strong>1：亮点</strong> </p> 
<ul> 
 <li style="text-align:start">CAS锁与队列</li> 
 <li style="text-align:start">连接对象单缓存</li> 
 <li style="text-align:start">独创CAS自旋式算法(池化领域独一无二的创新）</li> 
</ul> 
<p style="text-align:start"><strong>2：性能对比</strong></p> 
<p style="text-align:start"><img height="626" src="https://oscimg.oschina.net/oscnet/up-3092e65a77a8a8c91059bef8fc55ccd4f14.png" width="1418" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">CPU：I5-4430，OS：Win7_64  内存：8G</p> 
<p style="text-align:left"><strong>3：版本下载(java7)</strong></p> 
<pre style="text-align:left"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
   <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.github.chris2018998<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
   <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>beecp<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
   <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>3.1.8<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span></span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></pre> 
<p style="text-align:left"><strong>4：更新内容</strong></p> 
<ul> 
 <li style="text-align:left"><span style="color:#24292e">重构闲置连接的定时扫描线程</span></li> 
 <li style="text-align:left"><span style="color:#24292e">优化连接池退出CAS</span></li> 
 <li style="text-align:left">连接初始化时增加针对setNetworkTimeout方法的检测</li> 
</ul> 
<p style="text-align:left"><strong>5：Springboot启动器同步更新</strong></p> 
<pre style="text-align:start"><span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span>
   <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>com.github.chris2018998<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>
   <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>beecp-spring-boot-starter<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>
   <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>1.5.4<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>
<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></pre> 
<p style="text-align:left"><strong>6：项目地址</strong></p> 
<ul> 
 <li style="text-align:left">国内地址： <a href="https://gitee.com/mirrors/BeeCP">https://gitee.com/mirrors/BeeCP</a></li> 
 <li style="text-align:left">国外地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChris2018998%2FBeeCP" target="_blank">https://github.com/Chris2018998/BeeCP</a></li> 
</ul> 
<p style="text-align:left"><strong>补充说明</strong></p> 
<p>对于此作品(BeeCP,BeeOP) 个人付出了巨大心血， 因此视此作品为个人编程生涯的两枚勋章。</p> 
<p>可以看，可以学，也可以用(仅Jar包)，唯独不可以拿走此作品的核心代码与核心思想并应用在他处，</p> 
<p>天下独此一份，违者将追究法律责任。</p> 
<p>更多信息请查看附加条款说明：<a href="https://my.oschina.net/u/3918073/blog/5005030">https://my.oschina.net/u/3918073/blog/5005030</a></p>
                                        </div>
                                      
</div>
            