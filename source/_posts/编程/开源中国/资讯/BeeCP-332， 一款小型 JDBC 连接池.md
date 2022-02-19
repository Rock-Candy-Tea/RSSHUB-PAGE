
---
title: 'BeeCP-3.3.2， 一款小型 JDBC 连接池'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/32663325/153597592-c7d36f14-445a-454b-9db4-2289e1f92ed6.png'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 22:32:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/32663325/153597592-c7d36f14-445a-454b-9db4-2289e1f92ed6.png'
---

<div>   
<div class="content">
                                                                                            <p><strong> 一：产品简介</strong><br> 小蜜蜂连接池（BeeCP）是一款利用Java语言(计算机语言)开发的JDBC连接池,  以基础组件的角色可存在于各类数据库应用中，是J2EE应用通向数据库的纽带。</p> 
<p><strong>二：产品特点</strong><br> BeeCP是作者多年的倾心之作，它是<a href="https://my.oschina.net/">中国开源社区</a>中高质量代表性开源作品，具有性能高，代码轻，稳定好的特点。</p> 
<p>1：Java语言开发，具有跨平台的优点</p> 
<p>2：基于参数驱动，支持多种参数设置， 支持配置文件导入</p> 
<p>3：适用多种数据库驱动（截止当前，主流数据库均可适配）</p> 
<p>4：支持本地事务与分布式事务</p> 
<p>5：产品采用JUC技术开发，具有单点缓存，信号量控制，队列复用，非移动等待，自旋控制， 连接和异常的传递，异步候补，安全关闭等亮点</p> 
<p>6： 提供日志输出和监控工具</p> 
<p>7：健壮性好，敏捷应对意外情况（如断网，数据库服务崩溃）</p> 
<p>8：良好的接口扩展性</p> 
<p><strong>三：产品功能图</strong></p> 
<p><img alt="图片" src="https://user-images.githubusercontent.com/32663325/153597592-c7d36f14-445a-454b-9db4-2289e1f92ed6.png" referrerpolicy="no-referrer"></p> 
<p><strong>四：本次升级内容</strong></p> 
<ul> 
 <li>增加连接密文解密类，供外部扩展</li> 
 <li>连接上Catlog与Schema的默认值空，归还时则无复位操作</li> 
 <li>移除连接上Commit脏标记检查</li> 
</ul> 
<p><strong>五：软件包下载</strong><span style="color:#333333"><strong>(Java7或更高版本)</strong></span></p> 
<pre><<span>dependency</span>>
   <<span>groupId</span>>com.github.chris2018998</<span>groupId</span>>
   <<span>artifactId</span>>beecp</<span>artifactId</span>>
   <<span>version</span>>3.3.2</<span>version</span>>
</<span>dependency</span>></pre> 
<p><strong>六：项目地址</strong></p> 
<ul> 
 <li>国内地址： <a href="https://gitee.com/mirrors/BeeCP">https://gitee.com/mirrors/BeeCP</a></li> 
 <li>国外地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FChris2018998%2FBeeCP" target="_blank">https://github.com/Chris2018998/BeeCP</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            