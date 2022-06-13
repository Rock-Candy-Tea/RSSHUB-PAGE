
---
title: 'ERD Online 4.0.1 发布啦！增加常用的数据源驱动'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9383'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 14:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9383'
---

<div>   
<div class="content">
                                                                                            <p>由于大量用户反馈新版本4.0.0-beta版本，内置的数据源驱动不够使用，所以官方配置了常用的五种数据源驱动，发布4.0.1版本，供大家使用！</p> 
<div style="text-align:start"> 
 <h1>JDBC驱动版本</h1> 
 <div> 
  <div> 
   <p>TIP</p> 
  </div> 
  <div> 
   <p>ERD Online 内置了常用的几个JDBC数据源，分别是Mysql、Oracle、Sqlserver、Postgresql、DB2。<br> 内置的JDBC驱动版本，均为各数据源使用量最大的版本，如果和你们现有的数据源版本不一致，可以走<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fbenefit-profit%23vip-%25E9%2580%259A%25E9%2581%2593%25E5%25BE%25AE%25E4%25BF%25A1%25E6%2589%25AB%25E6%258F%258F%25E4%25B8%258B%25E6%2596%25B9%25E4%25BA%258C%25E7%25BB%25B4%25E7%25A0%2581" target="_blank">VIP通道</a>定制，请备注（定制）。</p> 
  </div> 
 </div> 
 <h2>Mysql<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fquick-start%2Fjdbc%23mysql" target="_blank">​</a></h2> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span><dependency></span>
</span><span style="color:#393a34"><span>    <groupId>mysql</groupId></span>
</span><span style="color:#393a34"><span>    <artifactId>mysql-connector-java</artifactId></span>
</span><span style="color:#393a34"><span>    <version>8.0.13</version></span>
</span><span style="color:#393a34"><span></dependency></span>
</span></code></pre> 
  </div> 
 </div> 
 <h2>Oracle<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fquick-start%2Fjdbc%23oracle" target="_blank">​</a></h2> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span><dependency></span>
</span><span style="color:#393a34"><span>    <groupId>com.oracle.database.jdbc</groupId></span>
</span><span style="color:#393a34"><span>    <artifactId>ojdbc8</artifactId></span>
</span><span style="color:#393a34"><span>    <version>21.1.0.0</version></span>
</span><span style="color:#393a34"><span></dependency></span>
</span></code></pre> 
  </div> 
 </div> 
 <h2>Sqlserver<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fquick-start%2Fjdbc%23sqlserver" target="_blank">​</a></h2> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span><dependency></span>
</span><span style="color:#393a34"><span>    <groupId>com.microsoft.sqlserver</groupId></span>
</span><span style="color:#393a34"><span>    <artifactId>mssql-jdbc</artifactId></span>
</span><span style="color:#393a34"><span>    <version>7.4.0.jre12</version></span>
</span><span style="color:#393a34"><span></dependency></span>
</span>
</code></pre> 
  </div> 
 </div> 
 <h2>Postgresql<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fquick-start%2Fjdbc%23postgresql" target="_blank">​</a></h2> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span><dependency></span>
</span><span style="color:#393a34"><span>    <groupId>org.postgresql</groupId></span>
</span><span style="color:#393a34"><span>    <artifactId>postgresql</artifactId></span>
</span><span style="color:#393a34"><span>    <version>42.2.5</version></span>
</span><span style="color:#393a34"><span></dependency></span>
</span></code></pre> 
  </div> 
 </div> 
 <h2>DB2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fportal.zerocode.net.cn%2Fdocs%2Fquick-start%2Fjdbc%23db2" target="_blank">​</a></h2> 
 <div> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#393a34"><span><dependency></span>
</span><span style="color:#393a34"><span>    <groupId>com.ibm.db2</groupId></span>
</span><span style="color:#393a34"><span>    <artifactId>jcc</artifactId></span>
</span><span style="color:#393a34"><span>    <version>11.5.0.0</version></span>
</span><span style="color:#393a34"><span></dependency></span>
</span></code></pre> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            