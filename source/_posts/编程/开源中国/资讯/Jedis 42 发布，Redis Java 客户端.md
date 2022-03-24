
---
title: 'Jedis 4.2 发布，Redis Java 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9083'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9083'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jedis 是 Redis 的一个 Java 客户端库，旨在提高性能和易用性。Jedis 与 redis 2.8.x、3.xx 及更高版本完全兼容。</p> 
<h3>新特性</h3> 
<ul> 
 <li>支持 EXPIRETIME 和 PEXIRETIME 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2852" target="_blank">#2852</a>)</li> 
 <li>在 EXPIREAT 和 PEXPIREAT 命令中支持 [NX|XX|GT|LT] 选项 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2874" target="_blank">#2874</a>)</li> 
 <li>支持带有多个参数的 CONFIG GET 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2863" target="_blank">#2863</a>)</li> 
 <li>支持带有多个参数的 CONFIG SET 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2949" target="_blank">#2949</a>)</li> 
 <li>支持向 MODULE LOAD 命令传递参数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2918" target="_blank">#2918</a>)</li> 
 <li>支持 FUNCTION 命令(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2878" target="_blank">#2878</a>)</li> 
 <li>支持 RedisTimeSeries 模块命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2854" target="_blank">#2854</a>)</li> 
 <li>支持 RedisBloom 模块命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2875" target="_blank">#2875</a>)</li> 
 <li>支持 RedisGraph 模块命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2941" target="_blank">#2941</a>)</li> 
 <li>……</li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li>更新集群插槽策略 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2643" target="_blank">#2643</a>)</li> 
 <li>通过系统属性配置套接字缓冲区大小 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2915" target="_blank">#2915</a>)</li> 
 <li>为 DatabasePipelineCommands 添加 javadoc (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2873" target="_blank">#2873</a>)</li> 
 <li>删除未使用的接口 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2865" target="_blank">#2865</a>)</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>构造函数中只有字符串参数是一个URL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2872" target="_blank">#2872</a>)</li> 
 <li>为 strAlgoLCSKeys 修复错误的 CommandObject 调用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2859" target="_blank">#2859</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Freleases%2Ftag%2Fv4.2.0" target="_blank">https://github.com/redis/jedis/releases/tag/v4.2.0</a></p>
                                        </div>
                                      
</div>
            