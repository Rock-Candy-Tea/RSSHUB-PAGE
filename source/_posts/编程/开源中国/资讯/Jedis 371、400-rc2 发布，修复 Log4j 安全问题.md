
---
title: 'Jedis 3.7.1、4.0.0-rc2 发布，修复 Log4j 安全问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9053'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9053'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jedis 是 Redis 的一个 Java 客户端库。Jedis 4.0.0-rc2、3.7.1 发布，这是针对安全漏洞 CVE-2021-44228，即 Log4j 安全问题的维护版本。这个问题对 Jedis 没有影响，Log4j 只在其测试中使用。</p> 
<h3>Jedis 3.7.1：</h3> 
<ul> 
 <li>将 log4j-core 从 2.13.3 升级到 2.15.0</li> 
 <li>将 Jedis 分支 3 的 Redis 分支限制在 6.2</li> 
 <li>在测试中只使用 SENTINEL REPLICAS</li> 
 <li>XADD 参数数量错误的消息已被修改</li> 
 <li>忽略测试 "invalid multibulk length"</li> 
</ul> 
<h3>Jedis 4.0.0 RC2：</h3> 
<p><strong>维护：</strong></p> 
<ul> 
 <li>将 log4j-core 从 2.13.3 升级到 2.15.0</li> 
 <li>解决 Javadoc 的警告问题</li> 
</ul> 
<p><strong>新功能：</strong></p> 
<ul> 
 <li>为 pipeline 类提供更简单的构造函数</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Freleases" target="_blank">https://github.com/redis/jedis/releases</a></p>
                                        </div>
                                      
</div>
            